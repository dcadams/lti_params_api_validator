import json

from django.shortcuts import render
from django.views import View

class ValidateData(View):
    def post(self, request):
        json_data = json.loads(request.body)
        for block in json_data:
            self.validate_block(block)

    def validate_block(self, block):
        pass
