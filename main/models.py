from django.db import models

# Create your models here.
class Product:
    id : int
    name: str
    img1: str
    price : int


class News:
    id: int
    headline: str
    description: str