# Generated by Django 5.1.7 on 2025-03-08 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verses', '0004_alter_verse_options_remove_verse_verse_name'),
        ('versetexts', '0002_versetext_verse_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='versetext',
            unique_together={('verse',)},
        ),
    ]
