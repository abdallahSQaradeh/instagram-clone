from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from userprofile.models import *
from .serializers import *
from .models import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    filter_backends = [filters.SearchFilter,
                       filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['user__username']
    lookup_fields = ['user__username', 'id', 'i']


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class StoryViewSet(ModelViewSet):
    serializer_class = StorySerializer
    queryset = Story.objects.all()
