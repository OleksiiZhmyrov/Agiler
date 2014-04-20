from rest_framework import serializers

from retro.models import Sticker, Board
from model_choices import *
from core.serializers import TeamSerializer, SprintSerializer
from retro.objects import BoardContainer


class StickerSerializer(serializers.Serializer):
    pk = serializers.Field()
    summary = serializers.CharField(required=True, max_length=1024)
    type = serializers.ChoiceField(choices=STICKER_TYPE_CHOICES, default=STICKER_TYPE_GOOD)
    rating = serializers.IntegerField(required=False, default=0)
    advanced_status = serializers.Field(source='advanced_status.name')
    owner = serializers.Field(source='owner.username')

    def restore_object(self, attrs, instance=None):
        if instance:
            for attr, value in attrs.items():
                setattr(instance, attr, value)
            return instance
        return Sticker(**attrs)

    class Meta:
        model = Sticker
        fields = ('pk', 'summary', 'advanced_status', 'type', 'owner', 'rating',)


class BoardSerializer(serializers.Serializer):
    pk = serializers.Field()
    isActive = serializers.BooleanField(required=False, default=False)
    voteLimit = serializers.IntegerField(required=False, default=3)
    owner = serializers.Field(source='owner.username')
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


class BoardContainerSerializer(serializers.Serializer):
    was_good = StickerSerializer(many=True, required=False)
    need_to_change = StickerSerializer(many=True, required=False)
    action_point = StickerSerializer(many=True, required=False)
    is_active = serializers.BooleanField(required=False, default=False)
    vote_limit = serializers.IntegerField(required=False, default=3)
    team = serializers.Field(source='team.name')
    sprint = SprintSerializer(many=False)

    def restore_object(self, attrs, instance=None):
        if instance:
            for attr, value in attrs.items():
                setattr(instance, attr, value)
            return instance
        return BoardContainer(**attrs)
