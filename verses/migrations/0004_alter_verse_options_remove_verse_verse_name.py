# Generated by Django 5.1.7 on 2025-03-08 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verses', '0003_alter_verse_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='verse',
            options={'ordering': ['verse_number'], 'verbose_name': 'Verse', 'verbose_name_plural': 'Verses'},
        ),
        migrations.RemoveField(
            model_name='verse',
            name='verse_name',
        ),
    ]
