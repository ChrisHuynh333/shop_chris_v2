from shop.models import Category

def extras(request):
    categories = Category.objects.all().order_by('category')
    return {'categories': categories}