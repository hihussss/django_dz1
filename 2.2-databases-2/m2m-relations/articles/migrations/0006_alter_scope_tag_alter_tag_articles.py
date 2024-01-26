# Generated by Django 5.0 on 2023-12-14 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_tag_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(through='articles.Scope', to='articles.article'),
        ),
    ]
