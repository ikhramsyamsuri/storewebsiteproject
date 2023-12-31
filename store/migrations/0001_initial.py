# Generated by Django 4.2.8 on 2023-12-11 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id_kategori', models.AutoField(primary_key=True, serialize=False)),
                ('nama_kategori', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id_status', models.AutoField(primary_key=True, serialize=False)),
                ('nama_status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_produk', models.IntegerField()),
                ('nama_produk', models.CharField(max_length=255)),
                ('harga', models.IntegerField()),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.kategori')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.status')),
            ],
        ),
    ]
