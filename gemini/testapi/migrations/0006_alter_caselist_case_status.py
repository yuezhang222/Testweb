# Generated by Django 3.2.6 on 2021-10-13 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0005_alter_caselist_case_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caselist',
            name='case_status',
            field=models.BooleanField(default=True, verbose_name='Execution status'),
        ),
    ]