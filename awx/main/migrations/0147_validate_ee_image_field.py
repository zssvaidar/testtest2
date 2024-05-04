# Generated by Django 2.2.16 on 2021-06-15 02:49

import awx.main.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0146_add_insights_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executionenvironment',
            name='image',
            field=models.CharField(
                help_text='The full image location, including the container registry, image name, and version tag.',
                max_length=1024,
                validators=[awx.main.validators.validate_container_image_name],
                verbose_name='image location',
            ),
        ),
    ]