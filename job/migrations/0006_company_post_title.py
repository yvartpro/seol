# Generated by Django 4.2.11 on 2024-11-15 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_company_post_deadline_alter_company_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_post',
            name='title',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
