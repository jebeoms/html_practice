# Generated by Django 4.2.3 on 2023-07-28 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_options_alter_post_author_alter_post_body_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='이름')),
                ('body', models.TextField(verbose_name='본문')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.post', verbose_name='포스트')),
            ],
            options={
                'verbose_name': '댓글',
                'verbose_name_plural': '댓글들',
            },
        ),
    ]
