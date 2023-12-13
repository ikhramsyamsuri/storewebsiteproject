from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from datetime import datetime, timedelta
from rest_framework.response import Response
from .models import Produk, Kategori , Status
import requests
import hashlib

# Display the landing page. 
# when button has click, it will seeding API to MySQL and display data in 'index.html'
def landingpage(request):
    retrieve_data_from_api()
    template = loader.get_template("landing_page.html")
    return HttpResponse(template.render({}, request))

# Display the table
# Include ID, Name, Category, Status Product
def renderhtml(request):
    produk = Produk.objects.all().filter(status=1)
    template = loader.get_template("index.html")
    context = {
        "products": produk,
    }
    
    return HttpResponse(template.render(context, request))

# Display Add Page
# To input data Manualy
def add(request):
    kategori = Kategori.objects.all().values()
    status = Status.objects.all().values()
    template = loader.get_template("add.html")
    context = {
        "categories": kategori,
        "statuses": status,
    }
    return HttpResponse(template.render(context, request))

# To delete data manualy
def delete (request, id):
    produk = Produk.objects.get(id=id)
    produk.delete()
    return HttpResponseRedirect(reverse('produk'))

# To input data to database MySQL
def addrecord(request):
    data_id_produk = request.POST["id"]
    data_nama_produk = request.POST["name"]
    data_id_kategori = request.POST["category"]
    data_harga = request.POST["price"]
    data_id_status = request.POST["status"]
    db = Produk(
        id_produk=data_id_produk,
        nama_produk=data_nama_produk,
        harga=data_harga,
        kategori_id=data_id_kategori,
        status_id=data_id_status,
    )
    db.save()
    return HttpResponseRedirect(reverse('produk'))

# Display Update Page
def edit (request, id):
    produk = Produk.objects.get(id=id)
    kategori = Kategori.objects.all().values()
    status = Status.objects.all().values()
    template = loader.get_template("edit.html")
    context = {
        'product' : produk,
        'categories': kategori,
        'statuses': status,
    }
    return HttpResponse (template.render(context, request))

# Updating data to database
def edited (request, id):
    data_id_produk = request.POST["id"]
    data_nama_produk = request.POST["name"]
    data_id_kategori = request.POST["category"]
    data_harga = request.POST["price"]
    data_id_status = request.POST["status"]
    produk = Produk.objects.get(id=id)
    produk.id_produk = data_id_produk
    produk.nama_produk = data_nama_produk
    produk.kategori_id = data_id_kategori
    produk.harga = data_harga
    produk.status_id = data_id_status
    produk.save()
    return HttpResponseRedirect(reverse('produk'))

# make username dynamic to login API
def dynamic_username():
    now = datetime.now()+ timedelta(hours=1)

    username = "tesprogrammer"
    tanggal = now.strftime("%d")
    bulan = now.strftime("%m")
    tahun = now.strftime("%y")
    jam = now
    return username + tanggal + bulan + tahun + "C" + jam.strftime("%H")

# make password dynamic to login API
def dynamic_password():
    now = datetime.now() + timedelta(hours=1)

    password = "bisacoding"
    tanggal = now.strftime("%d")
    bulan = now.strftime("%m")
    tahun = now.strftime("%y")
    endcoded_password = password + "-" + tanggal + "-" + bulan + "-" + tahun
    return hashlib.md5(endcoded_password.encode()).hexdigest()

# Get API data using request method
def retrieve_data_from_api():
    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
    response = requests.post(
        url, {"username": dynamic_username(), "password": dynamic_password()}
    )
    if response.status_code == 200:
        api_data = response.json()
        produk_data(api_data)
        return api_data
    else:
        return None

def produk_data(api_data):
    for data in api_data["data"]:

        # Insert Data To Table Category
        find_categories = Kategori.objects.filter(nama_kategori=data['kategori']).first()
        if find_categories :
            kategori_id = find_categories.id_kategori
        else:
            db = Kategori(nama_kategori=data['kategori'])
            db.save ()
            kategori_id = db.id_kategori

        # Insert Data To Table Status  
        find_status = Status.objects.filter(nama_status=data['status']).first()
        if find_status :
            status_id = find_status.id_status
        else:
            db = Status(nama_status=data['status'])
            db.save ()
            status_id = db.id_status

        # Insert Data To Table Product
        db = Produk(
            id_produk=data["id_produk"],
            nama_produk=data["nama_produk"],
            harga=data["harga"],
            kategori_id=kategori_id,
            status_id=status_id,
        )
        db.save()
