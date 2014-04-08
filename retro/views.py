from rest_framework import generics, permissions
from retro.serializers import StickerSerializer, BoardSerializer, BoardContainerSerializer
from retro.models import Sticker, Board
from core.permissions import IsOwnerOrReadOnly
from objects import BoardContainer


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


class BoardDetailsContainer(generics.RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardContainerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, queryset=None):
        board = generics.RetrieveAPIView.get_object(self, queryset)
        return BoardContainer(board)
