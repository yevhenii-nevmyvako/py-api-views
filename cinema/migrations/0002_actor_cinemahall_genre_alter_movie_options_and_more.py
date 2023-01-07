# Generated by Django 4.1.5 on 2023-01-07 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=70)),
                ("last_name", models.CharField(max_length=70)),
            ],
            options={
                "ordering": ["first_name"],
            },
        ),
        migrations.CreateModel(
            name="CinemaHall",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=70)),
                ("rows", models.IntegerField()),
                ("seats_in_row", models.IntegerField()),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=70, unique=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.AlterModelOptions(
            name="movie",
            options={"ordering": ["title"]},
        ),
        migrations.AddField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(to="cinema.actor"),
        ),
        migrations.AddField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(to="cinema.genre"),
        ),
    ]