from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token),
    path('users/', include('users.urls')),
    path('projects/', include('project.urls')),
    path('issues/', include('issue.urls'))
]
