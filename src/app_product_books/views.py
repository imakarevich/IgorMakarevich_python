from django.shortcuts import render
from django.urls import reverse_lazy
from . import models, forms
from django.views import generic
# Create your views here.

###########################CRUDL-BookCard#################################
#CREATE 
class CreateBookCard(generic.CreateView):
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
class UpdateBookCard(generic.UpdateView):
    model = models.BookCard
    form_class = forms.BookCard
    template_name = 'app_product_books/bookcard_create_or_update.html'
    success_url = reverse_lazy('app_product_books:bookcard-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

#DELETE
class DeleteBookCard(generic.DeleteView):
    model = models.BookCard
    template_name = 'app_product_books/bookcard_delete.html'
    success_url = reverse_lazy('app_product_books:bookcard-list')

#LIST
class ListBookCard(generic.ListView):
    model = models.BookCard
    template_name = 'app_product_books/bookcard_list.html'
