from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DeleteView,CreateView,TemplateView, ListView, UpdateView
from . import models
from app_product_books.models import BookCard
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import forms
from app_home_page.templatetags.util import has_group
from django.db.models import Q


# Create your views here.

#delete position from cart function
def delete_position(request, pk):
    #checking: Is the cart owned by this user?
    if request.session.get('cart_pk') == models.BookInCart.objects.get(pk=pk).cart.pk:
        models.BookInCart.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse_lazy('app_orders:cart'))


def show_cart(request):
    context={}
    context['cart'] = None
    #getting data from book forms, method post
    if request.method == "POST":
        book_pk = int(request.POST.get('book_pk'))
        quantity = int(request.POST.get('quantity'))
    #checking: Is there data? 
        if book_pk and quantity:
    #checking: Does user have a cart?
            cart_pk = request.session.get('cart_pk')
    #checking: is user anonimuous?
            if cart_pk:
                cart_pk = int(cart_pk)
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None
    #cart_pk to int
            cart, created = models.Cart.objects.get_or_create(
                pk=cart_pk,
                defaults={'user': user}
            )
            context['cart'] = cart
    #add cart object to session
            if created:
                request.session['cart_pk'] = cart.pk

            book = BookCard.objects.get(pk=book_pk)
            book_in_cart, created = models.BookInCart.objects.get_or_create(
                book=book,
                cart=cart,
                defaults={
                'quantity':quantity,
                'price':book.price,
                }
            )
            if not created:
                book_in_cart.quantity += quantity
                book_in_cart.save()

    #If Get method and others
    else:
        cart_pk = request.session.get('cart_pk')
        if cart_pk:
            cart = models.Cart.objects.get(pk=cart_pk)
            context['cart'] = cart

    context['form'] = forms.OrderForm()


    return render(
        request=request,
        template_name='app_orders/cart.html',
        context=context
    )

class Order(CreateView):
    model = models.OrderAll
    form_class = forms.OrderForm
    success_url = reverse_lazy('app_orders:order-success')

    def form_valid(self, form):
        cart = models.Cart.objects.get(
            pk=self.request.session.get('cart_pk'))
        form.instance.cart = cart
        return super().form_valid(form)

class OrderSuccess(TemplateView):
    template_name = 'app_orders/order_success.html'


class OrderAllList(LoginRequiredMixin, ListView):
    paginate_by = 10
    login_url = reverse_lazy('app_admin_portal:login')
    model = models.OrderAll
    template_name = 'app_orders/orders_list.html'
    ordering = ['-created_date']
    def get_success_url(self):
        self.request.session['cart_pk']
        return super().get_success_url()
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and has_group(user, 'Customers'):
            if user.carts.all():
                qs = models.OrderAll.objects.filter(cart__user=user).order_by('-created_date')
                print(qs)
                return qs
        
        return super().get_queryset()


class AddBookInCartFromOrderUpdate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    model = models.BookInCart
    form_class = forms.BookInCartForm
    template_name = 'app_orders/add_book_in_cart_from_order_update.html'
    success_url = reverse_lazy('app_orders:orders-list')

    def form_valid(self, form):
        pk = self.kwargs.get('pk', None)
        order = models.OrderAll.objects.get(pk=pk)
        cart = models.Cart.objects.get(pk=order.cart.pk)
        book_pk = form.cleaned_data.get('book').pk
        form.instance.price = BookCard.objects.get(pk=book_pk).price
        form.instance.cart = cart
        self.object = form.save()
        return super().form_valid(form)


class OrderAllUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'app_accounts.access_for_managers_admin'
    login_url = reverse_lazy('app_admin_portal:login')
    model = models.OrderAll
    form_class = forms.OrderAllForm
    template_name = 'app_orders/orders_update.html'
    success_url = reverse_lazy('app_orders:orders-list')

@login_required
@permission_required('app_accounts.access_for_managers_admin')
def delete_book_from_order(request, pk):
    models.BookInCart.objects.get(pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

