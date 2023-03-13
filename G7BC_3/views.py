from django.shortcuts import render
from store.models import Item

def home(request):
    products = Item.objects.all().filter(is_avalible = True).order_by('created_date')

   # for product in products:
        # adicionar as avaliaçoes do produto a product_details.html
        #reviews = ReviewRating.objects.filter(product_id = product.id, status=True)
    context = {
        'products': products,
        #'reviews':reviews,
    }
    return render(request, 'home.html', context)