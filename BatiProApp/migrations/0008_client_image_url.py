# Generated by Django 5.1.2 on 2024-12-01 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BatiProApp', '0007_alter_professional_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='image_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
