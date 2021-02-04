from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def products(request):
    """ A view to show the product, including sorting and searching """
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                message.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)


    context = {
        'products': products,
        'search_term': query,
    }

    return render(request,'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show an individual product with its details """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request,'products/product_detail.html', context)
