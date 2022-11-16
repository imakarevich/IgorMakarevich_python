from django.shortcuts import render
from django.views import generic
from app_product_books.models import BookCard
import datetime

# Create your views here.

class HomePage(generic.TemplateView):
    template_name = "app_home_page/home_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
    
        #Days ago, when new book appeared
        td = datetime.timedelta(days=20)        
        objs = BookCard.objects.filter(date_entered_catalog__gt=datetime.date.today() - td)
        context['object_list'] = objs
        print(context)
        return context


