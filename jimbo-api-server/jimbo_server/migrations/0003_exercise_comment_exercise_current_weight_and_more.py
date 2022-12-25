# Generated by Django 4.1.4 on 2022-12-25 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jimbo_server', '0002_rename_muscles_muscle'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='comment',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='current_weight',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='target_weight',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='video_link',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='jimbo_server.section'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='jimbo_server.workout'),
        ),
        migrations.AlterField(
            model_name='section',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='jimbo_server.workout'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('order', models.IntegerField()),
                ('slug', models.SlugField(max_length=250, unique_for_date='published')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day', to='jimbo_server.workout')),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
        migrations.AddField(
            model_name='exercise',
            name='day',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='jimbo_server.day'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='day',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='section', to='jimbo_server.day'),
            preserve_default=False,
        ),
    ]
