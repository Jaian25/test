from django.shortcuts import render
from rest_framework.response import Response
from .models import Project , Location
from .serializers import ProjectSerializer , LocationSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend
class ProjectAPI(APIView):
    
    
    # filter_backends = [SearchFilter]
    # search_fields = ['project_name' ]
    
    
    def get(self, request, pk=None, format=None):
        
        # test = {"name" : "jaian" , "age" : "18"}
        # return Response(test)
        # print(request.query_params.get('category'))
        category = request.query_params.get('category')
        project_name= request.query_params.get('project_name')
        affiliated_agency= request.query_params.get('affiliated_agency')
        project_start_time= request.query_params.get('project_start_time')
        project_completion_time= request.query_params.get('categproject_completion_timeory')
        total_budget= request.query_params.get('total_budget')
        id = pk
        if id is not None:
            project = Project.objects.get(id=id)
            serializer = ProjectSerializer(project)
            return Response({'data': serializer.data, 'success': True})
        projects = Project.objects.all()
        if category is not None and len(category)>0:
            projects = projects.filter(category = category)
        if project_name is not None and len(project_name)>0:
            projects = projects.filter(project_name = project_name)
        if affiliated_agency is not None and len(affiliated_agency)>0:
            projects = projects.filter(affiliated_agency = affiliated_agency)
        if project_start_time is not None and len(project_start_time)>0:
            projects = projects.filter(project_start_time = project_start_time)
        if project_completion_time is not None and len(project_completion_time)>0:
            projects = projects.filter(project_completion_time = project_completion_time)
        if total_budget is not None and len(total_budget)>0:
            projects = projects.filter(total_budget = total_budget)
        
            
        serializer = ProjectSerializer(projects, many=True)
        return Response({'data': serializer.data, 'success': True})

    def post(self, request, format=None):
            
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            
            locations = request.data['location_coordinates']
            for location in locations:
                location['project'] = obj.id
                print(location)
                loc_serializer = LocationSerializer(data=location)
                if loc_serializer.is_valid():
                    loc_serializer.save()
                
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        stu = Project.objects.get(pk=id)
        serializer = ProjectSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)

    # def delete(self, request, pk, format=None):
    #     id = pk
    #     stu = Project.objects.get(pk=id)
    #     stu.delete()
    #     return Response({'msg': 'Data Deleted'})
