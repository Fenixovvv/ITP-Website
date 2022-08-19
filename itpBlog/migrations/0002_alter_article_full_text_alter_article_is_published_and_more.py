# Generated by Django 4.0.5 on 2022-07-31 18:01

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('itpBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='full_text',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(help_text='Check the box if you want the post to appear on the blog page'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(help_text='Readable link to the article, example:\nfirst_article', max_length=255, unique=True),
        ),
    ]
