from django.shortcuts import render
from .models import Category, Dish, Event, Banners
import datetime


def main(request):
    special_categories = Category.objects.filter(is_visible=True).filter(is_special=True).order_by('category_order')
    for item in special_categories:
        item.dishes = Dish.objects.filter(category=item.pk)

    categories = Category.objects.filter(is_visible=True).filter(is_special=False).order_by('category_order')
    for item in categories:
        item.dishes = Dish.objects.filter(category=item.pk)

    events = Event.objects.filter(event_date__gte=datetime.date.today())

    banners = Banners.objects.filter(is_visible=True)

    return render(request, 'index.html', context={'categories': categories,
                                                  'special_categories': special_categories,
                                                  'events': events,
                                                  'banners': banners,
                                                  }
                  )
