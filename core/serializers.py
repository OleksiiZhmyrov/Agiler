from rest_framework import serializers
from core.models import Team, Sprint
from core.objects import ApplicationSettings
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    stickers = serializers.PrimaryKeyRelatedField(many=True)
    boards = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'stickers', 'boards')


class TeamSerializer(serializers.Serializer):
    pk = serializers.Field()
    name = serializers.CharField(required=True, max_length=32)
    label = serializers.CharField(required=True, max_length=32)

    boards = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def restore_object(self, attrs, instance=None):
        if instance:
            for attr, value in attrs.items():
                setattr(instance, attr, value)
            return instance
        return Team(**attrs)

    class Meta:
        model = Team
        fields = ('pk', 'name', 'label', 'boards',)


class SprintSerializer(serializers.Serializer):
    pk = serializers.Field()
    number = serializers.IntegerField(required=True)
    start_date = serializers.DateTimeField()
    finish_date = serializers.DateTimeField()

    boards = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def restore_object(self, attrs, instance=None):
        if instance:
            for attr, value in attrs.items():
                setattr(instance, attr, value)
            return instance
        return Sprint(**attrs)

    class Meta:
        model = Sprint
        fields = ('pk', 'number', 'start_date', 'finish_date', 'boards',)


class ApplicationSettingsSerializer(serializers.Serializer):
    users_count = serializers.IntegerField()
    sprints_count = serializers.IntegerField()
    teams_count = serializers.IntegerField()

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.users_count = attrs.get('users_count', instance.users_count)
            instance.sprints_count = attrs.get('sprints_count', instance.sprints_count)
            instance.teams_count = attrs.get('teams_count', instance.teams_count)
            return instance
        return ApplicationSettings(**attrs)
