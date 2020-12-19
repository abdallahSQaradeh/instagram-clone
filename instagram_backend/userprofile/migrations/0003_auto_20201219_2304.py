# Generated by Django 3.1.3 on 2020-12-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20201219_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posts_liked_by_users',
            field=models.ManyToManyField(blank=True, related_name='user_likes_on_posts', to='userprofile.UserProfile'),
        ),
    ]