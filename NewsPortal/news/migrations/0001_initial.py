# Generated by Django 4.0.3 on 2022-04-13 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratingAuthor', models.FloatField(default=0.0)),
                ('authorUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryType', models.CharField(choices=[('NS', 'новость'), ('AR', 'статья')], default='NS', max_length=2)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('postTitle', models.CharField(max_length=128)),
                ('postText', models.TextField()),
                ('rating', models.FloatField(default=0.0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
                ('postThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='postCategory',
            field=models.ManyToManyField(through='news.PostCategory', to='news.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentText', models.CharField(max_length=255)),
                ('commentDate', models.DateTimeField(auto_now_add=True)),
                ('rating', models.FloatField(default=0.0)),
                ('commentPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
