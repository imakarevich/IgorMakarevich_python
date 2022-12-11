from django.shortcuts import render
from django.urls import reverse_lazy
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views import generic
# Create your views here.

###########################CRUDL-BookCard#################################
#CREATE 
class CreateBookCard(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    model = models.BookCard
    form_class = forms.BookCard
    template_name = 'app_product_books/bookcard_create_or_update.html'
    success_url = reverse_lazy('app_product_books:bookcard-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

#READ
class ReadBookCard(generic.DetailView):
    model = models.BookCard
    template_name = 'app_product_books/bookcard_read.html'

#UPDATE
class UpdateBookCard(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.BookCard
    form_class = forms.BookCard
    template_name = 'app_product_books/bookcard_create_or_update.html'
    success_url = reverse_lazy('app_product_books:bookcard-list')
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

#DELETE
class DeleteBookCard(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    model = models.BookCard
    template_name = 'app_product_books/bookcard_delete.html'
    success_url = reverse_lazy('app_product_books:bookcard-list')

#LIST
class ListBookCard(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    paginate_by = 15
    model = models.BookCard
    template_name = 'app_product_books/bookcard_list.html'
