# Generated by Django 2.2.16 on 2020-10-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comname', models.CharField(max_length=20)),
                ('groupname', models.CharField(max_length=20)),
                ('usercode', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=10)),
                ('postcode', models.CharField(max_length=3)),
            ],
        ),
    ]