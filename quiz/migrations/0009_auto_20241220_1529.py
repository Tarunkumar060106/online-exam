# Generated by Django 3.0.5 on 2024-12-20 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20241219_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Objectives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='section_id',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_option',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=50)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.Section'),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Difficulty'),
        ),
        migrations.AlterField(
            model_name='question',
            name='objective',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Objectives'),
        ),
    ]