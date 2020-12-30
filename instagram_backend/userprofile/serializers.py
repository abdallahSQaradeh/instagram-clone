from userprofile.models import *
from rest_framework import serializers, routers, viewsets
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['user_fullname', 'posts', 'user_name', 'bio', 'user']

    def get_posts(self, obj):
        return obj.posts()

    def get_user_name(self, obj):
        return obj.user_name()
