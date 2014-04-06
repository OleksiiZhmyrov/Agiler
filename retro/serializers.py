from rest_framework import serializers
from retro.models import Sticker, Board
from model_choices import *
from core.models import Sprint, Team
from core.serializers import TeamSerializer, SprintSerializer


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
