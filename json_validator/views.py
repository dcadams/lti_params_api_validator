import json

from django.shortcuts import render
from django.views import View
from django.conf import settings
import traceback


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
        json_data = json.loads(request.body)
        conf = get_configuration()
        validation = {}
        for block in json_data:
            vald = self.validate_block(block, conf)
            if vald:
                validation[block['block_key']] = vald

        print(validation)

    def validate_block(self, block, conf):
        error_lst = []
        if not block['launch_url'] in conf['LAUNCH_URL']:
            error_lst.append('launch_url')
        if not block['tool_id'] in conf['TOOL_ID']:
            error_lst.append('tool_id')
        if not block['send_email'] == conf['SEND_EMAIL']:
            error_lst.append('tool_id')
        if not block['send_name'] == conf['SEND_NAME']:
            error_lst.append('send_name')
        
        return error_lst
