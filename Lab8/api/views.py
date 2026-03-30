from django.http import JsonResponse
from .models import Product, Category

def product_to_json(product):
    return {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'count': product.count,
        'is_active': product.is_active,
        'category_id': product.category.id,
        'category_name': product.category.name,
    }

def category_to_json(category):
    return {
        'id': category.id,
        'name': category.name,
    }

def products_list(request):
    products = Product.objects.all()
    data = [product_to_json(product) for product in products]
    return JsonResponse(data, safe=False)

def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
        data = product_to_json(product)
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'})
    
def categories_list(request):
    categories = Category.objects.all()
    data = [category_to_json(category) for category in categories]
    return JsonResponse(data, safe=False)

def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
        data = category_to_json(category)
        return JsonResponse(data)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'})
    
def category_products(request, id):
    try:
        category = Category.objects.get(id=id)
        products = Product.objects.filter(category=category)
        data = [product_to_json(product) for product in products]
        return JsonResponse(data, safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'})