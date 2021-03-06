# Generated by Django 2.2.17 on 2021-01-02 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Committente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cognome', models.CharField(max_length=100)),
                ('indirizzo', models.CharField(max_length=200)),
                ('luogo', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('cellulare', models.CharField(max_length=20)),
                ('email1', models.EmailField(max_length=100)),
                ('email2', models.EmailField(max_length=100)),
                ('codfisc', models.CharField(max_length=16)),
                ('piva', models.CharField(max_length=11)),
                ('referente', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Committenti',
            },
        ),
        migrations.CreateModel(
            name='Progetto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anno', models.DateField(verbose_name='%Y')),
                ('nome', models.CharField(max_length=200)),
                ('luogo', models.CharField(max_length=100)),
                ('committente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regore.Committente')),
            ],
            options={
                'verbose_name_plural': 'Progetti',
            },
        ),
        migrations.CreateModel(
            name='Preventivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('descrizione', models.TextField()),
                ('importo', models.FloatField()),
                ('progetto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regore.Progetto')),
            ],
            options={
                'verbose_name_plural': 'Preventivi',
            },
        ),
        migrations.CreateModel(
            name='Ore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('ora_inizio', models.TimeField()),
                ('ora_fine', models.TimeField()),
                ('note', models.TextField()),
                ('progetto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regore.Progetto')),
            ],
            options={
                'verbose_name_plural': 'Ore',
            },
        ),
        migrations.CreateModel(
            name='Fattura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr', models.IntegerField()),
                ('data', models.DateField()),
                ('descrizione', models.TextField()),
                ('importo', models.FloatField()),
                ('progetto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regore.Progetto')),
            ],
            options={
                'verbose_name_plural': 'Fatture',
            },
        ),
    ]
