from django.shortcuts import render
from rest_framework import viewsets
from datetime import datetime 
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class PingViewset(APIView): 
    def get(self,request):
        context ={}
        date = datetime.now()
        formatted_date_1 = date.strftime("%Y-%m-%d")  
    
    def post(self,request):
        url=request.POST.get("ping/")
        date = datetime.now()
        formatted_date_2 = date.strftime("%Y-%m-%d") 
        return Response({'key': 'value'}, status=status.HTTP_200_OK)

    
   
    def result(self,request,formatted_date_1,formatted_date_2):
         if formatted_date_1 == formatted_date_2:
                return Response({'key': 'value'}, status=status.HTTP_200_OK)


