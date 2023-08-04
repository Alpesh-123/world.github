# Generated by Django 4.2.3 on 2023-08-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='percentage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='total_marks',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
    ]
