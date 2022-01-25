# Generated by Django 3.0.3 on 2022-01-25 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20220125_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='galery_category',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='is_galery_graphic',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='is_galery_icon',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='is_galery_web',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Category'),
        ),
    ]
