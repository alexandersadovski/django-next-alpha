# Generated by Django 5.1.3 on 2024-12-04 12:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInteraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.BooleanField()),
                ('target_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions_received', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions_made', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'target_user')},
            },
        ),
    ]
