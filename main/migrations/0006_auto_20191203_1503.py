# Generated by Django 2.2.1 on 2019-12-03 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_resena'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resenas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Lugar')),
            ],
        ),
        migrations.DeleteModel(
            name='Resena',
        ),
    ]
