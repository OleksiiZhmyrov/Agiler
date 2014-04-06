from rest_framework import serializers
from retro.models import Sticker, Board
from model_choices import *
from core.models import Sprint, Team
from core.serializers import TeamSerializer, SprintSerializer
from retro.objects import RetroBoardContainer


class StickerSerializer(serializers.Serializer):
    pk = serializers.Field()
    summary = serializers.CharField(required=True, max_length=1024)
    type = serializers.ChoiceField(choices=STICKER_TYPE_CHOICES, default=STICKER_TYPE_GOOD)
    status = serializers.ChoiceField(choices=STICKER_STATUS_CHOICES, default=STICKER_STATUS_CREATED)
    owner = serializers.Field(source='owner.username')

    def restore_object(self, attrs, instance=None):
        if instance:
            for attr, value in attrs.items():
                setattr(instance, attr, value)
            return instance
        return Sticker(**attrs)

    class Meta:
        model = Sticker
        fields = ('pk', 'summary', 'status', 'type', 'owner',)


class BoardSerializer(serializers.Serializer):
    pk = serializers.Field()
    isActive = serializers.BooleanField(required=False, default=False)
    voteLimit = serializers.IntegerField(required=False, default=3)
    owner = serializers.Field(source='owner.username')

    # sprint = serializers.PrimaryKeyRelatedField(many=False, queryset=Sprint.objects.all())
    sprint = serializers.Field(source='sprint.number')
    team = TeamSerializer(many=False)

    stickers = StickerSerializer(many=True, required=False)

    def restore_object(self, attrs, instance=None):
        if instance:
            for attr, value in attrs.items():
                setattr(instance, attr, value)
            return instance
        return Board(**attrs)

    class Meta:
        model = Board
        fields = ('pk', 'isActive', 'voteLimit', 'owner', 'sprint', 'team', 'stickers',)


class RetroBoardContainerSerializer(serializers.Serializer):
    was_good = StickerSerializer(many=True, required=False)
    need_to_change = StickerSerializer(many=True, required=False)
    action_point = StickerSerializer(many=True, required=False)
    is_active = serializers.BooleanField(required=False, default=False)
    vote_limit = serializers.IntegerField(required=False, default=3)
    team = serializers.Field()
    sprint = serializers.Field()

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.was_good = attrs.get('was_good', instance.was_good)
            instance.need_to_change = attrs.get('need_to_change', instance.need_to_change)
            instance.action_point = attrs.get('action_point', instance.action_point)
            instance.is_active = attrs.get('is_active', instance.is_active)
            instance.vote_limit = attrs.get('vote_limit', instance.vote_limit)
            instance.team = attrs.get('team', instance.team)
            instance.sprint = attrs.get('sprint', instance.sprint)
            return instance
        return RetroBoardContainer(**attrs)
