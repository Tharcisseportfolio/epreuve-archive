# Generated by Django 5.0.6 on 2024-07-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='epreuve',
            name='link',
            field=models.FileField(default='', upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='epreuve',
            name='type',
            field=models.CharField(choices=[('Q', 'Questionnaire'), ('A', 'Answers')], default='Q', max_length=1),
        ),
    ]