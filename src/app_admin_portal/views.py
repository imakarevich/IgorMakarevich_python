from django.shortcuts import render
from django.views import generic

# Create your views here.

class AdminPortalForExployees(generic.TemplateView):
    template_name = "app_admin_portal/admin_portal_main.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    
    #     #Days ago, when new book appeared
    #     td = datetime.timedelta(days=20)        
    #     objs = BookCard.objects.filter(date_entered_catalog__gt=datetime.date.today() - td)
    #     context['object_list'] = objs
    #     print(context)
    #     return context
