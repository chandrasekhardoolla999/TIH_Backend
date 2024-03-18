# Generated by Django 4.1.13 on 2024-02-04 07:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0026_blog_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='upvoted_users',
            field=models.ManyToManyField(related_name='upvoted_blogs', to=settings.AUTH_USER_MODEL),
        ),
    ]
