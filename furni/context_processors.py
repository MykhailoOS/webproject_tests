from .models import Home, Shop, BlogPost


def home(request):
    items = Home.objects.filter(is_visible=True)
    return {'items': items}


def blog(request):
    items = BlogPost.objects.filter(is_visible=True)
    return {'blogs': items}


def shop(request):
    items = Shop.objects.filter(is_visible=True)
    return {'shop': items}
