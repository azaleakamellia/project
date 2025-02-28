# Generated by Django 5.0.7 on 2024-07-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilsapp', '0007_remove_row_docid_remove_row_docname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='row',
            name='length',
        ),
        migrations.AddField(
            model_name='mh',
            name='bearing',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='mh',
            name='color',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mh',
            name='enclosed_a',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='mh',
            name='linetype',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='mh',
            name='linewt',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mh',
            name='lyrfrzn',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mh',
            name='lyron',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='row',
            name='docname',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='row',
            name='doctype',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='row',
            name='docver',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='row',
            name='lyrhandle',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
