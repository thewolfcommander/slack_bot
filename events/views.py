import json
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class Events(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data.get('data')
        webhook = request.data.get('webhook')
        print(type(data))
        print(type(webhook))
        resp = requests.post(webhook, json.dumps(data))
        return Response(resp)