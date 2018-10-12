from .models import Category
from django.conf import settings
from urllib.parse import urljoin
        
def category_menu(context):
    site_url = settings.BASE_URL
    category_url = urljoin(site_url, 'blog/category/')
    media_url = urljoin(settings.BASE_URL, 'media/')
    #sub_menu = Category.objects.filter(status=1)
    sub_menu = Category.objects.filter()
    return {'sub_menu': sub_menu, 'category_url':category_url, 'site_url':site_url, 'media_url':media_url}