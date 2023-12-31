# Generated by Django 4.2.2 on 2023-11-05 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('code_postal', models.CharField(max_length=255)),
                ('ville', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('points_fidelite', models.IntegerField()),
                ('adresses', models.ManyToManyField(to='myservice.adresse')),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('montant', models.FloatField()),
                ('etat', models.CharField(max_length=255)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myservice.client')),
            ],
        ),
        migrations.CreateModel(
            name='ModePaiement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('prix', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RetourProduit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantite', models.IntegerField()),
                ('etat', models.CharField(max_length=255)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myservice.produit')),
            ],
        ),
        migrations.CreateModel(
            name='LigneCommande',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantite', models.IntegerField()),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myservice.commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myservice.produit')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='modes_paiement',
            field=models.ManyToManyField(to='myservice.modepaiement'),
        ),
    ]
