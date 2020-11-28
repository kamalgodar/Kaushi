from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name='index'),
    path("news/", views.news, name="news"),
    path("market/", views.market, name="market"),
    path("shop/", views.shop, name="shop"),
    path("manpower/", views.manpower, name="manpower"),

]