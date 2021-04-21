# Generated by Django 3.2 on 2021-04-19 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0003_auto_20210414_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardgame_id', models.IntegerField()),
                ('date', models.DateField(null=True)),
                ('winning_player_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='boardgame',
            name='edition',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='boardgame',
            name='max_players',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='boardgame',
            name='min_players',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='boardgame',
            name='year_published',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Play_To_Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boardgames.play')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boardgames.player')),
            ],
        ),
        migrations.CreateModel(
            name='Boardgame_Has_Designer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardgame_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boardgames.boardgame')),
                ('designer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boardgames.designer')),
            ],
        ),
    ]
