# Generated by Django 3.2 on 2022-03-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book/image'),
        ),
    ]