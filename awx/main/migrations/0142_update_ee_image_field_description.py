# Generated by Django 2.2.16 on 2021-05-12 20:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0141_remove_isolated_instances'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executionenvironment',
            name='image',
            field=models.CharField(
                help_text='The full image location, including the container registry, image name, and version tag.',
                max_length=1024,
                verbose_name='image location',
            ),
        ),
    ]