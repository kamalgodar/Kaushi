from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, News

def index(request):

    product1 = Product()
    product1.name = 'Apple'
    product1.price = 110
    product1.img1 = 'carrot.jpg'

    product2 = Product()
    product2.name = 'Cauliflower'
    product2.price = 40
    product2.img1 = 'cauliflower.jpg'

    product3 = Product()
    product3.name = 'Dustpan'
    product3.price = 200
    product3.img1 = 'dustpan.jpg'

    product4 = Product()
    product4.name = 'Carrot'
    product4.price = 30
    product4.img1 = 'carrot.jpg'

    product5 = Product()
    product5.name = 'Sprayer'
    product5.price = 120
    product5.img1 = 'sprayer.jpg'

    product6 = Product()
    product6.name = 'Gloves'
    product6.price = 80
    product6.img1 = 'gloves.jpg'

    product7 = Product()
    product7.name = 'Compost Manure'
    product7.price = 40
    product7.img1 = 'compostmanure.jpg'

    product8 = Product()
    product8.name = 'Spade'
    product8.price = 150
    product8.img1 = 'spade.jpg'

    product9 = Product()
    product9.name = 'Cabbahge'
    product9.price = 40
    product9.img1 = 'carrot.jpg'

    products = [product1, product2, product3, product4, product5, product6, product7, product8, product9]


    news1 = News()
    news1.headline = '>> The Government has planned to distribute free seeds to farmers'
    news1.description = 'I am a description'

    news2 = News()
    news2.headline = '>> Know the reasons behind the drastic change in the price of tomato; Is it because of border seize?'
    news2.description = 'I am a description'

    news3 = News()
    news3.headline = '>> Experts predict the future of market '
    news3.description = 'I am a description'

    news = [news1, news2, news3]

    return render(request, 'index.html', {'products': products, 'news': news, })



def news(request):

    news1 = News()
    news1.headline = '>> The Government has planned to distribute free seeds to farmers'
    news1.description = 'I am a description'

    news2 = News()
    news2.headline = '>> Know the reasons behind the drastic change in the price of tomato; Is it because of border seize?'
    news2.description = 'I am a description'

    news3 = News()
    news3.headline = '>> Experts predict the future of market '
    news3.description = 'I am a description'

    news = [news1, news2, news3]

    return render(request, 'news.html', {'news': news})




def market(request):

    product1 = Product()
    product1.name = 'Apple'
    product1.price = 110
    product1.img = 'carrot.jpg'

    product2 = Product()
    product2.name = 'Cauliflower'
    product2.price = 40
    product2.img = 'cauliflower.jpg'

    product3 = Product()
    product3.name = 'Dustpan'
    product3.price = 200
    product3.img = 'dustpan.jpg'

    product4 = Product()
    product4.name = 'Carrot'
    product4.price = 30
    product4.img = 'carrot.jpg'

    products = [product1, product2, product3, product4,]

    return render(request, 'market.html', {'products': products})


    
def shop(request):
    
    product1 = Product()
    product1.name = 'Apple'
    product1.price = 110
    product1.img = 'carrot.jpg'

    product2 = Product()
    product2.name = 'Cauliflower'
    product2.price = 40
    product2.img = 'cauliflower.jpg'

    product3 = Product()
    product3.name = 'Dustpan'
    product3.price = 200
    product3.img = 'dustpan.jpg'

    product4 = Product()
    product4.name = 'Carrot'
    product4.price = 30
    product4.img = 'carrot.jpg'

    product5 = Product()
    product5.name = 'Sprayer'
    product5.price = 120
    product5.img = 'sprayer.jpg'

    product6 = Product()
    product6.name = 'Gloves'
    product6.price = 80
    product6.img = 'gloves.jpg'

    product7 = Product()
    product7.name = 'Compost Manure'
    product7.price = 40
    product7.img = 'compostmanure.jpg'

    product8 = Product()
    product8.name = 'Spade'
    product8.price = 150
    product8.img = 'spade.jpg'

    product9 = Product()
    product9.name = 'Cabbahge'
    product9.price = 40
    product9.img = 'carrot.jpg'

    products = [product1, product2, product3, product4, product5, product6, product7, product8, product9]

    return render(request, 'shop.html', {'products': products})

def manpower(request):
    return render(request, 'manpower.html', {})

def mycart(request):
    return render(request, 'mycart.html', {})

# Create your views here.
