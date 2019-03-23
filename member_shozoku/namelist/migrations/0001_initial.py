# Generated by Django 2.1.7 on 2019-03-23 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year_of_birth', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Syozoku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('home', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='member',
            name='syozoku',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='namelist.Syozoku'),
        ),
    ]
