# Generated by Django 5.0.7 on 2024-07-14 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilsapp', '0006_mh_row_delete_osmb_delete_osmpop_delete_osmrd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='row',
            name='docid',
        ),
        migrations.RemoveField(
            model_name='row',
            name='docname',
        ),
        migrations.RemoveField(
            model_name='row',
            name='doctype',
        ),
        migrations.RemoveField(
            model_name='row',
            name='docver',
        ),
    ]
