import logging

from django.shortcuts import render
from django.http import JsonResponse 
from rest_framework.decorators import APIView  
from rest_framework import status 
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from .serializers import TestSerializers
from .models import Student 
from newpro import global_msg 


logger = logging.getLogger('django')

class FirstApiTestView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request):
        try:
            students = Student.objects.all() 
            serializer = TestSerializers(students, many=True)
            return JsonResponse({"responseCode":global_msg.SUCCESS_RESPONSE_CODE, "response":"success", "data": serializer.data},status=status.HTTP_200_OK) 
        except Exception as e: 
            logger.info(str(e), exc_info = True) 
            return JsonResponse({"responseCode":global_msg.UNSUCCESS_RESPONSE_CODE, "response":"Data not Found"}, status=status.HTTP_404_NOT_FOUND) 
    def post(self, request):
        if not request.body: 
            return JsonResponse({"responseCode":global_msg.UNSUCCESS_RESPONSE_CODE,"response":"Request Body Can not be Blank."}, status=status.HTTP_404_NOT_FOUND) 
        serializer = TestSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save() 
            return JsonResponse({"responseCode":global_msg.SUCCESS_RESPONSE_CODE, "response":"success"},status=status.HTTP_200_OK) 
        return JsonResponse({"responseCode":global_msg.UNSUCCESS_RESPONSE_CODE,"response":"Something went Wrong", "error":serializer.errors}, status=status.HTTP_404_NOT_FOUND) 