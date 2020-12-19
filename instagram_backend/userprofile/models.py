from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    phone_number = PhoneNumberField()
    private = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'userprofile'


class Post(models.Model):
    text = models.CharField(max_length=2000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.ImageField(upload_to='static/userprofile/', blank=True)
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)
    posts_liked_by_users = models.ManyToManyField(
        UserProfile, related_name='user_likes_on_posts', blank=True)
    post_Saved_by = models.ManyToManyField(
        UserProfile, related_name='post_saved_by_users', blank=True)
    tagged_users = models.ManyToManyField(
        UserProfile, related_name='users_tagged_in_post', blank=True)

    def __str__(self):
        return f' {self.user.user.username } -  {self.text}'


class Comment(models.Model):
    text = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_liked_by_users = models.ManyToManyField(
        UserProfile, related_name="liked_by_users", blank=True)
    tagged_users = models.ManyToManyField(
        UserProfile, related_name='users_tagged_in_comment', blank=True)

    def __str__(self):
        return f' {self.user.user.username} -  {self.text}'


class Story(models.Model):

    text = models.CharField(max_length=2000)
    image_url = models.ImageField(
        upload_to='static/userprofile/', default="None")
    background_color = models.CharField(max_length=100, default="black")
    link = models.URLField(blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    tagged_users = models.ManyToManyField(
        UserProfile, related_name='users_tagged_in_story', blank=True)

    def __str__(self):
        return f'{self.user.user.username} - {self.text}'
