# Generated by Django 5.0.2 on 2024-03-21 15:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=0, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='materials.course', verbose_name='course'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='url'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='подписчики', to='materials.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='подписки', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'подписка',
                'verbose_name_plural': 'подписки',
                'unique_together': {('user', 'course')},
            },
        ),
    ]