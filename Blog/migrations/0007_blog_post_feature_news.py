# Generated by Django 3.2 on 2022-03-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_blog_post_home_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='feature_news',
            field=models.BooleanField(default=False),
        ),
    ]
