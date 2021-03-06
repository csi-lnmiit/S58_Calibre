# Generated by Django 2.0.1 on 2018-01-14 12:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for a particular Exam', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('figure', models.ImageField(blank=True, null=True, upload_to='')),
                ('question_type', models.CharField(choices=[('text', 'text'), ('radio', 'radio'), ('select-multiple', 'Select Multiple')], default='radio', max_length=20)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Exam')),
            ],
        ),
    ]
