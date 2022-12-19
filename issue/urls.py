from django.urls import path
from .views import IssueAPI

urlpatterns = [
    path('', IssueAPI.as_view()),
    path('<int:pk>/', IssueAPI.as_view())
]
