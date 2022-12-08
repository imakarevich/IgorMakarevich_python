from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DeleteView,CreateView,TemplateView, ListView, UpdateView
from . import models
from app_product_books.models import BookCard
from . import forms
from app_home_page.templatetags.util import has_group


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
    # def get_success_url(self):
    #     self.request.session['order_pk'] = 
    #     return super().get_success_url()

class OrderSuccess(TemplateView):
    template_name = 'app_orders/order_success.html'

class OrderAllList(ListView):
    paginate_by = 10
    # login_url = reverse_lazy('app_admin_portal:login')
    model = models.OrderAll
    template_name = 'app_orders/orders_list.html'
    ordering = ['-updated_date']
    def get_success_url(self):
        self.request.session['cart_pk']
        return super().get_success_url()
    def get_queryset(self):!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # if self.request.user.is_authenticated():
        # user = self.request.user
        # qs = user.carts.order.all()
        # print(qs)!!!!!!!!!!!!!!!!!!!!!!!!
        return super().get_queryset()

class AddBookInCartFromOrderUpdate(CreateView):
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
            # print(type(BookCard.objects.get(pk=book_pk).price))
            # c = 2/0
        form.instance.cart = cart
        self.object = form.save()
        return super().form_valid(form)


class OrderAllUpdate(UpdateView):
    model = models.OrderAll
    form_class = forms.OrderAllForm
    template_name = 'app_orders/orders_update.html'
    success_url = reverse_lazy('app_orders:orders-list')
    

# def order_update(request, pk):
#     context = {}
#     order = models.OrderAll.objects.get(pk=pk)
#     if request.method == 'POST':
#         book_in_cart_form_list_post = []
#         order_all_form = forms.OrderAllForm(request.POST, instance=order)
#         if order_all_form.is_valid():
#             order_all_form.save()
#             return redirect(reverse_lazy('app_orders:orders-list'))
#         else:
#             messages.error(request, ('Пожалуйста, исправьте ошибки.'))    

#     else:
#         order_all_form = forms.OrderAllForm(instance=order)
#         book_in_cart_form_list = []
#         for book_in_cart in order.cart.book_in_cart.all():
#             book_in_cart_form_list.append(forms.BookInCartForm(instance=book_in_cart)) 
        
#         context['order_all_form'] = order_all_form
#         context['order'] = order
#         context['book_in_cart_form_list'] = book_in_cart_form_list

#     return render(request, 'app_orders/orders_update.html', context=context)

def delete_book_from_order(request, pk):
    models.BookInCart.objects.get(pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

