# Generated by Django 4.2.4 on 2023-08-04 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0005_alter_comment_table_alter_post_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="imgfile",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]