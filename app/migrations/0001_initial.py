# Generated by Django 2.2.14 on 2020-08-20 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gitft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='imgaes/')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
