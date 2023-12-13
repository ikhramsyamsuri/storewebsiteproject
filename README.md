# Django Product Table With Database 

    This is a simple Django 3.0+ project CRUD, use MySQL as databease. The database is seeded from External API

## Project Requirement
  
- Python 3.0 +
- Django 3.0 +
- MySQL Client
- Anaconda (Optional)
- Minimum Device 1Gb RAM

## How To Run

- Clone this repo
- In terminal use this command :
```
 cd storewebsiteproject
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```
## Model Explanition

in `models.py` have 3 class : `Kategori` `Status` `Produk`. `Kategori` and `Status` have a id and name of every class which will be used for `Produk` to display in table product.

## Folder Structure

    ├── store                       # Main folder all
    |    ├── __pycache__
    |    ├── migrations             # Migration Histories
    |    ├── templates              # HTML folder
    |    |    ├── add.html
    |    |    ├── edit.html
    |    |    ├── index.html
    |    |    └── landing_page.html
    |    ├── __init__.py
    |    ├── asgi.py
    |    ├── models.py              # Make classification on database
    |    ├── settings.py            # Setting project dependency
    |    ├── tests.py
    |    ├── urls.py                # Setting project path
    |    ├── views.py               # All Function in here
    |    └── wsgi.py
    ├── sb.sqlite                    
    ├── manage.py                     
    └── README.md
