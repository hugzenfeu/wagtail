# Generated by Django 5.1.3 on 2024-11-17 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin_url', models.URLField(blank=True, verbose_name='LinkedIn URL')),
                ('github_url', models.URLField(blank=True, verbose_name='GitHub URL')),
                ('mastodon_url', models.URLField(blank=True, verbose_name='Mastodon URL')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]