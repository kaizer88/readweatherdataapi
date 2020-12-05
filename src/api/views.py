import os, pathlib as p
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status as st
import json


# Create your views here.


class ReadDataApi(APIView):

    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.ReadSerializer

    def post(self, request, *args, **kwargs):
        """ Requested weather results"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            city = serializer.validated_data.get('city')
            numberOfDays = serializer.validated_data.get('numberOfDays')

            path = settings.DATA
            filename = 'data.json'
            file_path = p.Path("{0}/{1}".format(path, filename))

            with open(file_path, 'r') as f:
                data = json.load(f)
            f.close()

            output = []
            for i in range(len(data['weatherdata']['location'])):
                if city in data['weatherdata']['location'][i]['name']:
                    output.append(data['weatherdata']['location'][i]['forecast']['days'][:numberOfDays])

            data = {
                "city":city,
                "output":output
            }

            return Response(data)

        else:
            return Response(serializer.errors,
                            status=st.HTTP_400_BAD_REQUEST
                            )