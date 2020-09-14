# Generated by Django 3.0.10 on 2020-09-13 15:40

from django.db import migrations, models
import django.db.models.deletion
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('hectares', models.DecimalField(decimal_places=2, max_digits=12)),
                ('point', djgeojson.fields.PointField()),
            ],
        ),
        migrations.CreateModel(
            name='Rain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('precipitation', models.DecimalField(decimal_places=3, max_digits=6)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rains', to='floor.Floor')),
            ],
        ),
    ]
