# Generated by Django 4.1.13 on 2024-02-04 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_blog_dummy_is_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='dummy_is_featured',
        ),
    ]
