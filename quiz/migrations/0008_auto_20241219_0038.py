# Generated by Django 3.0.5 on 2024-12-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20241216_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='negative_marks',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='question',
            name='marks',
            field=models.PositiveIntegerField(default=4),
        ),
    ]
