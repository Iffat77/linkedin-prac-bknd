from rest_framework import viewsets, permissions

from .serializers import ProfileSerializer, ProjectsSerializer
from .models import Profile, Projects

class ProfileViewSet(viewsets.ModelViewSet):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer
  permission_classes = [permissions.IsAuthenticated]

class ProjectsViewSet(viewsets.ModelViewSet):
  queryset = Projects.objects.all()
  serializer_class = ProjectsSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]



