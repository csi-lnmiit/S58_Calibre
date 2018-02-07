# Generated by Django 2.0.1 on 2018-01-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20180116_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=1200)),
                ('question', models.ManyToManyField(to='quiz.Question')),
            ],
        ),
    ]