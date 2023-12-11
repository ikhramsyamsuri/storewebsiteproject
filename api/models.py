from django.db import models

class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=255)

class Status (models.Model):
    id_status = models.AutoField(primary_key=True)
    nama_status = models.CharField(max_length=255)

class Produk(models.Model):
    id_produk = models.IntegerField ()
    nama_produk = models.CharField (max_length=255)
    harga = models.IntegerField ()
    kategori = models.ForeignKey (Kategori, on_delete=models.CASCADE)
    status = models.ForeignKey (Status, on_delete=models.CASCADE)