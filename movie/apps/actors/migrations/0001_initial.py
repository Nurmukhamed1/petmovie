# Generated by Django 4.1.4 on 2022-12-27 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('age', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='actors/')),
            ],
            options={
                'verbose_name': 'Actors and producers',
                'verbose_name_plural': 'Actors and producers',
            },
        ),
    ]
