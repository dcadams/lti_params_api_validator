"""
Views for the json_validator app.
"""
import json
import traceback

from django.conf import settings
from django.shortcuts import render
from django.views import View


def get_configuration():
    """
    Returns JSON object as a dictionary.
    """
    try:
        with open(settings.CONFIG_PATH, encoding='utf-8') as conf_file:
            conf_json = json.load(conf_file)
    except Exception:   # pylint: disable=W0703
        traceback.print_exc()

    return conf_json


class ValidateData(View):
    """
    Class for validating course configurations.
    """
    def post(self, request):
        """
        It will process post request on /validator/ and will return
         JSON data and a string of line numbers having errors.
        """
        json_data = request.POST.get('jsontxtarea')
        parsed_json = json.loads(json_data)
        conf = get_configuration()
        error_lines_lst = []
        curr_pos = 2
        error_lines = ''

        for block in parsed_json:
            block_error_lines = self.validate_block(block, conf, curr_pos)
            if block_error_lines:
                error_lines_lst.extend(block_error_lines)
            curr_pos += 18

        if error_lines_lst:
            error_lines = ', '.join(map(str, error_lines_lst))
            msg = 'There are some issues with course configurations which are highlighted below'
        else:
            msg = 'Course configurations looks fine'
        return render(
            request,
            "result.html",
            {
                'json_data': json.dumps(parsed_json, indent=6, ensure_ascii=False),
                'error_lines': error_lines,
                'message': msg
            }
        )

    def validate_block(self, block, conf, curr_pos):
        """
        This method will validate various fields from the json block
         and returns line numbers having errors for that block.
        """
        pos_lst = []

        if not block['launch_url'] in conf['LAUNCH_URL']:
            pos_lst.append(4 + curr_pos)
        if not block['tool_id'] in conf['TOOL_ID']:
            pos_lst.append(5 + curr_pos)
        if not block['send_email'] == conf['SEND_EMAIL']:
            pos_lst.append(15 + curr_pos)
        if not block['send_name'] == conf['SEND_NAME']:
            pos_lst.append(16 + curr_pos)
        if not block['custom_parameters'][1] in conf['VERSION']:
            pos_lst.append(8 + curr_pos)
        if not block['custom_parameters'][2] in conf['LANGUAGE']:
            pos_lst.append(9 + curr_pos)
        if not block['custom_parameters'][4] == conf['APP']:
            pos_lst.append(11 + curr_pos)
        if not block['custom_parameters'][5] == conf['LAUNCH']:
            pos_lst.append(12 + curr_pos)
        if block['custom_parameters'][3] == "module=pre-assess":
            if not block['lti_display_name'] == "knowledge_check":
                pos_lst.append(3 + curr_pos)

        return pos_lst
