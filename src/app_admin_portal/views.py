from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import  render, redirect
from .forms import RegistrationUserForm
from django.contrib.auth.models import Group
from app_orders import models as orders_models
from app_reference_book.models import Status
from app_accounts.forms import UserExtensionForm


# Create your views here.

# class AdminPortalForEmployees(LoginRequiredMixin, generic.TemplateView):
#     login_url = reverse_lazy('app_admin_portal:login')
#     template_name = "app_admin_portal/admin_portal_main.html"


def register_request(request):
    context = {}
    if request.method == "POST":
        registration_user_form = RegistrationUserForm(request.POST)
        user_extension_form = UserExtensionForm(request.POST)
        if registration_user_form.is_valid() and user_extension_form.is_valid():
            user = registration_user_form.save()
            extension = user_extension_form.save()
            extension.user = user
            extension.save(update_fields=["user"])
            group, created = Group.objects.get_or_create(name='Customers')
            if group:
                user.groups.add(group)
            else:
                user.groups.add(created)
            login(request, user)
            # messages.success(request, "Registration successful." )
            return redirect(reverse_lazy('app_admin_portal:admin-portal'))
        messages.error(request, "Неудачная регистрация. Вы ввели неверные данные. Либо такой пользователь уже есть.")
    context['registration_user_form'] = RegistrationUserForm()
    context['user_extension_form'] = UserExtensionForm()
    return render (request=request, template_name="app_admin_portal/register.html", context=context)

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    
    #     #Days ago, when new book appeared
    #     td = datetime.timedelta(days=20)        
    #     objs = BookCard.objects.filter(date_entered_catalog__gt=datetime.date.today() - td)
    #     context['object_list'] = objs
    #     print(context)
    #     return context

def statistic_information_for_admin(request):
    context={}
    orders_all = orders_models.OrderAll.objects.count()
    
    orders_statuses_queryset = Status.objects.all()
    orders_count_statuses_dict = {}
    for status in orders_statuses_queryset:
        orders_count_statuses_dict[status] = status.order.all().count()
    print(orders_count_statuses_dict)

    context['orders_all'] = orders_all
    context['orders_count_statuses_dict'] = orders_count_statuses_dict
    return render (request=request, template_name="app_admin_portal/admin_portal_main.html", context=context)