# Generated by Django 2.2.9 on 2020-02-01 12:47

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0007_auto_20191118_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='notes',
            field=markdownx.models.MarkdownxField(blank=True, help_text='Extra build notes'),
        ),
    ]
