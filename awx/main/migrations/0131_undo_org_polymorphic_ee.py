# Generated by Django 2.2.16 on 2021-03-11 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0130_ee_polymorphic_set_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='default_environment',
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text='The default execution environment for jobs run by this organization.',
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='main.ExecutionEnvironment',
            ),
        ),
    ]