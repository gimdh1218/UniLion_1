# Generated by Django 2.2.14 on 2020-08-26 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_notice_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='create_at',
            field=models.DateTimeField(null=True),
        ),
    ]
