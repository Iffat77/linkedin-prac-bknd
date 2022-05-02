from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from linkedinapp.views import ProfileViewSet, ProjectsViewSet


router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'projects', ProjectsViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('', include('user_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
  
]
