import json
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings


SLACK_BOT_USER_TOKEN = getattr(settings,                          #2
'SLACK_BOT_USER_TOKEN', None)       
SLACK_CHANNEL = '#general'
SLACK_ICON_URL = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuGqps7ZafuzUsViFGIremEL2a3NR0KO0s0RTCMXmzmREJd5m4MA&s'

SLACK_USER_NAME = 'easyeats'



class Events(APIView):
    def post(self, request, *args, **kwargs):
        text = request.data.get('text', None)

        resp = requests.post('https://slack.com/api/chat.postMessage', {
            'token': SLACK_BOT_USER_TOKEN,
            'channel': SLACK_CHANNEL,
            'text': text,
            'icon_url': SLACK_ICON_URL,
            'username': SLACK_USER_NAME
        }).json()

        return Response(resp)