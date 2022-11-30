from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView,CreateView,TemplateView
from . import models
from app_product_books.models import BookCard
from . import forms

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
    def get_success_url(self):
        del self.request.session['cart_pk']
        return super().get_success_url()

class OrderSuccess(TemplateView):
    template_name = 'app_orders/order_success.html'
