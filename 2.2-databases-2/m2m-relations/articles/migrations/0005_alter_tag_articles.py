# Generated by Django 5.0 on 2023-12-14 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_options_alter_scope_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(related_name='scopes', through='articles.Scope', to='articles.article'),
        ),
    ]
