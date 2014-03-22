from rest_framework import generics, permissions

from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer

from core.serializers import TeamSerializer, SprintSerializer, UserSerializer, ApplicationSettingsSerializer
from core.permissions import IsOwnerOrReadOnly
from core.objects import ApplicationSettings
from core.models import Sprint, Team


class TeamsList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TeamDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class SprintsList(generics.ListCreateAPIView):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SprintDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ApplicationSettings(View):
    @staticmethod
    def get(request):
        application_settings = ApplicationSettings(
            users_count=User.objects.all().count(),
            sprints_count=Sprint.objects.all().count(),
            teams_count=Team.objects.all().count()
        )
        serializer = ApplicationSettingsSerializer(application_settings)
        json = JSONRenderer().render(serializer.data)
        return HttpResponse(json, content_type="application/json")
