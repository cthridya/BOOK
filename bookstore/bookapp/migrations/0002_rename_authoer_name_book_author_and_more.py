# Generated by Django 5.1.2 on 2024-10-13 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authoer_name',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_title',
            new_name='title',
        ),
    ]
