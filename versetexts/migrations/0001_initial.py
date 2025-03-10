# Generated by Django 5.1.7 on 2025-03-08 00:59

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('verses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerseText',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('reference', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('text', models.TextField()),
                ('verse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to='verses.verse')),
            ],
            options={
                'verbose_name': 'Verse Text',
                'verbose_name_plural': 'Verse Texts',
                'unique_together': {('verse', 'text')},
            },
        ),
    ]
