from django.shortcuts import render
from api.models import Idea, Vote
from api.models import Commentary, Image
from .serializers import GetIdIdeaSerializer, GetVoteSerializer
from .serializers import GetCommentarySerializer, GetImageSerializer, GetIdeaSerializer
from .serializers import PostIdeaSerializer, PostCommentarySerializer, PostVoteSerializer
from rest_framework import viewsets
from rest_framework import filters


class IdeaViewSet(viewsets.ModelViewSet):
    serializer_class = GetIdeaSerializer
    queryset = Idea.objects.all()


class VoteViewSet(viewsets.ModelViewSet):
    serializer_class = GetVoteSerializer
    queryset = Vote.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('idea', 'idea__id',)


class CommentaryViewSet(viewsets.ModelViewSet):
    serializer_class = GetCommentarySerializer
    queryset = Commentary.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('idea', 'idea__id',)


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = GetImageSerializer
    queryset = Image.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('idea', 'idea__id',)


class PostIdeaViewSet(viewsets.ModelViewSet):
    serializer_class = PostIdeaSerializer
    queryset = Idea.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostCommentaryViewSet(viewsets.ModelViewSet):
    serializer_class = PostCommentarySerializer
    queryset = Commentary.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostVoteViewSet(viewsets.ModelViewSet):
    serializer_class = PostVoteSerializer
    queryset = Vote.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
