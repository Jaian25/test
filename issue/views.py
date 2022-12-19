from django.shortcuts import render
from rest_framework.response import Response
from .models import Issue
from .serializers import IssueSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView


class IssueAPI(APIView):
    
    
    def get(self, request, pk=None, format=None):
        
        # test = {"name" : "jaian" , "age" : "18"}
        # return Response(test)
        
        id = pk
        if id is not None:
            project = Issue.objects.get(id=id)
            serializer = IssueSerializer(project)
            return Response({'data': serializer.data, 'success': True})

        projects = Issue.objects.all()
        serializer = IssueSerializer(projects, many=True)
        return Response({'data': serializer.data, 'success': True})

    def post(self, request, format=None):
            
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
                
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        stu = Issue.objects.get(pk=id)
        serializer = IssueSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)
