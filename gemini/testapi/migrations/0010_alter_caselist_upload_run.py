# Generated by Django 3.2.6 on 2021-10-14 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0009_auto_20211014_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caselist',
            name='upload_run',
            field=models.FileField(help_text='用来运行的文件', unique=True, upload_to='./testapi/case/', verbose_name='运行文件'),
        ),
    ]