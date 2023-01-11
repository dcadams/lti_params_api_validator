"""
Tests for lti_params_api_validator
"""
import json
from django.test import TestCase
from django.urls import reverse


class TestLTIParamsAPIValidator(TestCase):
    """
    Test for lti_params_api_validator
    """
    def test_lti_params_api_validator(self):
        """
        Test method for validating erroneous line numbers and message from dummy data.
        """
        dummy_data = { 'jsontxtarea' : json.dumps([
                {
                    "display_name": "Кібербезпека загрози, вразливості та атаки",
                    "block_key": "block-v1:R_org+R1+May22+type@lti_advantage_consumer+block@da7e7f8353f54fa49aeeded858ab7c7f",
                    "lti_display_name": "nowledge_check",
                    "launch_url": "https://hub-dev.netacad.com/kernel/lti/launch?client_id=824811",
                    "tool_id": "None",
                    "custom_parameters": [
                        "course=varmir",
                        "version=1.1",
                        "lang=en-US",
                        "module=pre-assess",
                        "app=sgp",
                        "launch=adl"
                    ],
                    "scored": True,
                    "send_email": True,
                    "send_name": True
                },
                {
                    "display_name": "Network Security Testing",
                    "block_key": "block-v1:R_org+R1+May22+type@lti_advantage_consumer+block@581379bb42274369abfc9b48dbc31e87",
                    "lti_display_name": "LTI Advantage Consumer",
                    "launch_url": "https://hub-dev.netacad.com/kernel/lti/launch?client_id=824811",
                    "tool_id": "19",
                    "custom_parameters": [
                        "course=varmir",
                        "version=1.0",
                        "lang=en-US",
                        "module=m1",
                        "app=sgp",
                        "launch=adl"
                    ],
                    "scored": True,
                    "send_email": False,
                    "send_name": True
                },
                {
                    "display_name": "Threat Intelligence",
                    "block_key": "block-v1:R_org+R1+May22+type@lti_advantage_consumer+block@fb663db96954435a9914a66409a3ae4f",
                    "lti_display_name": "LTI Advantage Consumer",
                    "launch_url": "https://hub-dev.netacad.com/kernel/lti/launch?client_id=824811",
                    "tool_id": "11",
                    "custom_parameters": [
                        "course=varmir",
                        "version=1.0",
                        "lang=en-US",
                        "module=m2",
                        "app=sgp",
                        "launch=adl"
                    ],
                    "scored": True,
                    "send_email": True,
                    "send_name": True
                },
                {
                    "display_name": "Endpoint Vulnerability Assessment",
                    "block_key": "block-v1:R_org+R1+May22+type@lti_advantage_consumer+block@a0f5774253724885b366618fedbb64c7",
                    "lti_display_name": "LTI Advantage Consumer",
                    "launch_url": "https://hub-dev.netacad.com/kernel/lti/launch?client_id=8248",
                    "tool_id": "11",
                    "custom_parameters": [
                        "course=varmir",
                        "version=1.0",
                        "lang=en-UK",
                        "module=m3",
                        "app=sgp2",
                        "launch=adl"
                    ],
                    "scored": True,
                    "send_email": True,
                    "send_name": True
                },
                {
                    "display_name": "Risk Management and Security Controls",
                    "block_key": "block-v1:R_org+R1+May22+type@lti_advantage_consumer+block@ef5f4ad4af3d4b099cd536e72514b5f5",
                    "lti_display_name": "LTI Advantage Consumer",
                    "launch_url": "https://hub-dev.netacad.com/kernel/lti/launch?client_id=824811",
                    "tool_id": "11",
                    "custom_parameters": [
                        "course=varmir",
                        "version=1.0",
                        "lang=en-US",
                        "module=m4",
                        "app=sgp",
                        "launch=adlr"
                    ],
                    "scored": True,
                    "send_email": True,
                    "send_name": True
                },
                {
                    "display_name": "Cyber Threat Management (CyberTM) Module 1 - 5 Group Exam",
                    "block_key": "block-v1:R_org+R1+May22+type@lti_advantage_consumer+block@559a0cd9f4f643f6b42b4d6f599de866",
                    "lti_display_name": "LTI Advantage Consumer",
                    "launch_url": "https://hub-dev.netacad.com/kernel/lti/launch?client_id=24811",
                    "tool_id": "11",
                    "custom_parameters": [
                        "course=varmir",
                        "version=1.0",
                        "lang=en-US",
                        "module=mge1",
                        "app=sgp",
                        "launch=adl"
                    ],
                    "scored": True,
                    "send_email": True,
                    "send_name": True
                },
                {
                    "display_name": "Digital Forensics and Incident Analysis and Response",
                    "block_key": "block-v1:R_org+R1+May22+type@lti_advantage_consumer+block@b1f8570ee0434ff29b008d282a3bedba",
                    "lti_display_name": "LTI Advantage Consumer",
                    "launch_url": "https://hub-dev.netacad.com/kernel/lti/launch?client_id=824811",
                    "tool_id": "11",
                    "custom_parameters": [
                        "course=varmir",
                        "version=1.0",
                        "lang=en-US",
                        "module=m5",
                        "app=sgp",
                        "launch=adl"
                    ],
                    "scored": True,
                    "send_email": True,
                    "send_name": False
                },
                {
                    "display_name": "Cyber Threat Management (CyberTM) Module 6 Group Exam",
                    "block_key": "block-v1:R_org+R1+May22+type@lti_advantage_consumer+block@59430a68734c4525ae0f3ab30e4e8654",
                    "lti_display_name": "LTI Advantage Consumer",
                    "launch_url": "https://hub-dev.netacad.com/kernel/lti/launch?client_id=824811",
                    "tool_id": "11",
                    "custom_parameters": [
                        "course=varmir",
                        "version=7.0",
                        "lang=en-US",
                        "module=mge2",
                        "app=sgp",
                        "launch=adl"
                    ],
                    "scored": True,
                    "send_email": True,
                    "send_name": True
                },
                {
                    "display_name": "Cyber Threat Management (CyberTM) Course Final Exam",
                    "block_key": "block-v1:R_org+R1+May22+type@lti_advantage_consumer+block@90f9e7a83d9a41d5a207c77b1afafb0b",
                    "lti_display_name": "LTI Advantage Consumer",
                    "launch_url": "https://hub-dev.netacad.com/kernel/lti/launch?client_id=824811",
                    "tool_id": "11",
                    "custom_parameters": [
                        "course=varmir",
                        "version=1.0",
                        "lang=en-US",
                        "module=final-exam",
                        "app=sgp",
                        "launch=adl"
                    ],
                    "scored": True,
                    "send_email": True,
                    "send_name": True
                }
            ])
        }

        validator_response = self.client.post(reverse('validate_data'), dummy_data)

        self.assertEqual(validator_response.context['error_lines'], '7, 10, 5, 25, 35, 60, 65, 67, 86, 96, 126, 136')
        self.assertEqual(validator_response.context['message'], 'There are some issues with course configurations which are highlighted below')
