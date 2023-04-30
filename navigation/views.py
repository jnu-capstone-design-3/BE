from django.shortcuts import render
from rest_framework.views import APIView


class Index(APIView):
    def post(self, request, *args, **kwargs):
        return ("Heelloo,")