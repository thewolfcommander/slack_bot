import json
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class Events(APIView):
    def post(self, request, *args, **kwargs):
        text = request.data.get('text', None)
        SLACK_BOT_USER_TOKEN = request.data.get('token')
        SLACK_CHANNEL = request.data.get('channel')
        SLACK_ICON_URL = request.data.get('icon_url')
        SLACK_USER_NAME = request.data.get('username')

        resp = requests.post('https://slack.com/api/chat.postMessage', {
            'token': json.dumps(SLACK_BOT_USER_TOKEN),
            'channel': json.dumps(SLACK_CHANNEL),
            'text': text,
            'icon_url': json.dumps(SLACK_ICON_URL),
            'username': json.dumps(SLACK_USER_NAME)
        }).json()

        return Response(resp)