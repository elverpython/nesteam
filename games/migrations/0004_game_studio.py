# Generated by Django 4.2.3 on 2023-08-16 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_genre_game_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='Studio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='games.studio'),
        ),
    ]