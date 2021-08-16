# Generated by Django 3.2.6 on 2021-08-16 00:55

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('createdat', models.CharField(blank=True, db_column='createdAt', max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('id', models.CharField(default=posts.models.assignId, max_length=255, primary_key=True, serialize=False)),
                ('main_id', models.IntegerField()),
                ('depth', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('createdat', models.CharField(blank=True, db_column='createdAt', max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('main_id', models.IntegerField()),
                ('hotscore', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('image', models.CharField(blank=True, max_length=400, null=True)),
            ],
            options={
                'db_table': 'posts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.CharField(default=posts.models.assignId, max_length=36, primary_key=True, serialize=False)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('uid', models.CharField(blank=True, max_length=255, unique=True)),
            ],
            options={
                'db_table': 'votes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.CharField(default=posts.models.assignId, max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=255)),
                ('username', models.CharField(blank=True, max_length=255, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'django_users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
