# Generated by Django 3.2.6 on 2021-09-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caselist',
            fields=[
                ('user_name', models.CharField(max_length=30)),
                ('iterm', models.CharField(max_length=30)),
                ('release', models.CharField(max_length=30)),
                ('modules', models.CharField(max_length=30)),
                ('case_name', models.CharField(max_length=100)),
                ('case_id', models.AutoField(primary_key=True, serialize=False)),
                ('case_time', models.DateTimeField(auto_now_add=True)),
                ('upload_py', models.FileField(upload_to='./case/')),
                ('upload_json', models.FileField(upload_to='./case/')),
                ('upload_run', models.FileField(upload_to='./case/')),
                ('upload_core', models.FileField(upload_to='./case/')),
                ('case_status', models.BooleanField(null=True)),
            ],
            options={
                'verbose_name': 'case',
                'verbose_name_plural': 'caselist',
            },
        ),
    ]
