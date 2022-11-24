import json
import traceback

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def get_configuration():
    """
    Returns JSON object as a dictionary.
    """
    try:
        with open(settings.CONFIG_PATH, encoding='utf-8') as conf_file:
            conf_json = json.load(conf_file)
    except Exception:
        traceback.print_exc()

    return conf_json


class ValidateData(View):
    def post(self, request):
        """
        It will process post request on /validator/ and will
         return errors with block keys.
        """
        json_data = json.loads(request.body)
        conf = get_configuration()
        issues = {}
        for block in json_data:
            block_errors = self.validate_block(block, conf)
            if block_errors:
                issues[block['block_key']] = block_errors

        print(issues)
        return HttpResponse(json.dumps(issues))

    def validate_block(self, block, conf):
        """
        This method will validate various fields from the json block.
        """
        error_lst = []

        if not block['launch_url'] in conf['LAUNCH_URL']:
            error_lst.append('launch_url')
        if not block['tool_id'] in conf['TOOL_ID']:
            error_lst.append('tool_id')
        if not block['send_email'] == conf['SEND_EMAIL']:
            error_lst.append('tool_id')
        if not block['send_name'] == conf['SEND_NAME']:
            error_lst.append('send_name')
        if not block['custom_parameters'][1] in conf['VERSION']:
            error_lst.append('version')
        if not block['custom_parameters'][2] in conf['LANGUAGE']:
            error_lst.append('language')
        if not block['custom_parameters'][4] == conf['APP']:
            error_lst.append('app')
        if not block['custom_parameters'][5] == conf['LAUNCH']:
            error_lst.append('launch')
        if block['custom_parameters'][3] == "module=pre-assess":
            if not block['lti_display_name'] == "knowledge_check":
                error_lst.append('lti_display_name')

        return error_lst
