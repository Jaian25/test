from rest_framework import serializers

from .models import Project,Location
from  issue.models import Issue
from issue.serializers import IssueSerializer
import datetime
import time
class ProjectSerializer(serializers.ModelSerializer):
    
    locations = serializers.SerializerMethodField(read_only = True)
    completion_percentage = serializers.SerializerMethodField(read_only = True)
    issues = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Project
        fields = ['id', 'project_name','category','affiliated_agency','description','project_start_time','project_completion_time','completion_percentage','total_budget', 'locations','issues']
        
    def get_locations(self, object):
        return LocationSerializer(Location.objects.filter(project=object.id), many=True).data
    def get_completion_percentage(self , object):
        start_date_timestamp = time.mktime(object.project_start_time.timetuple())
        end_date_timestamp = time.mktime(object.project_completion_time.timetuple())
        current_date_timestamp = time.mktime(datetime.date.today().timetuple())
        print(current_date_timestamp , start_date_timestamp , end_date_timestamp)
        try:
            percentage = min(100 , 100*(current_date_timestamp - start_date_timestamp)/(end_date_timestamp - start_date_timestamp))
        except:
            percentage = 0.0
        return round(percentage,2)
    def get_issues(self, object):
        return IssueSerializer(Issue.objects.filter(project=object.id), many=True).data
        
class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['id', 'x_coor', 'y_coor', 'project']
