from rest_framework import generics, permissions
from retro.serializers import StickerSerializer, BoardSerializer, RetroBoardContainerSerializer
from retro.models import Sticker, Board
from core.permissions import IsOwnerOrReadOnly
from django.views.generic import View
from model_choices import *
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


class StickersList(generics.ListCreateAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class StickerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class BoardsList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class BoardDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class RetroBoardContainer(View):
    @staticmethod
    def get(request, pk):
        board = Board.objects.get(pk=pk)
        stickers = Sticker.objects.filter(board__pk=pk)
        retroboard_container = RetroBoardContainer(
            was_good=stickers.filter(type=STICKER_TYPE_GOOD),
            need_to_change=stickers.filter(type=STICKER_TYPE_CHANGE),
            action_point=stickers.filter(type=STICKER_TYPE_ACTION),
            is_active=board.isActive,
            vote_limit=board.voteLimit,
            team=board.team,
            sprint=board.sprint
        )
        serializer = RetroBoardContainerSerializer(retroboard_container)
        json = JSONRenderer().render(serializer.data)
        return HttpResponse(json, content_type="application/json")
