# Generated by Django 5.1.4 on 2025-01-28 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rst', '0003_grade_level_semester_session_alter_result_grade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='ca_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='exam_score',
            field=models.IntegerField(null=True),
        ),
    ]
