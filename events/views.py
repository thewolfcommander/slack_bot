import json
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class Events(APIView):
    def post(self, request, *args, **kwargs):
        text = request.data.get('text', None)

        resp = requests.post('https://slack.com/api/chat.postMessage', {
            'token': "xoxb-1234958449984-1211347637395-EX8IKUZ9EmewbbYRXIPfLed3",
            'channel': "#website",
            'text': text,
            'icon_url': "https://mycocosoul.s3.amazonaws.com/static/img/logo.png",
            'username': "easyeats"
        }).json()

        return Response(resp)