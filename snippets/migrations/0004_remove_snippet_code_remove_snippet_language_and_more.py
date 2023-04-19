# Generated by Django 4.1.4 on 2022-12-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_alter_snippet_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='code',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='language',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='linenos',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='style',
        ),
        migrations.AddField(
            model_name='snippet',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
