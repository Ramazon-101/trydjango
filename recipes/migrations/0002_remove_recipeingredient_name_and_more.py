# Generated by Django 4.1 on 2022-08-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredient',
            name='name',
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='ingredient_name',
            field=models.CharField(help_text='kamroq soz bilan tarifla', max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.FloatField(),
        ),
    ]
