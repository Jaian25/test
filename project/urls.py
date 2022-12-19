from django.urls import path
from .views import ProjectAPI

urlpatterns = [
    path('', ProjectAPI.as_view()),
    path('<int:pk>/', ProjectAPI.as_view())
]
