from rest_framework import serializers

from .models import Issue
from users.serializers import UserSerializer
# from project.serializers import ProjectSerializer

class IssueSerializer(serializers.ModelSerializer):
    
    user_data = serializers.SerializerMethodField(read_only = True)
    project_data = serializers.SerializerMethodField(read_only = True)
    
    class Meta:
        model = Issue
        fields = ['id', 'user','project','issue', 'user_data' , 'project_data']
    # def get_completion_percentage(self , object):
    def get_user_data(self , object):
        return UserSerializer(object.user).data
    def get_project_data(self , object):
        # return ProjectSerializer(object.project).data
        return {"project_name": object.project.project_name}