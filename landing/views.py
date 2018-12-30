from django.shortcuts import render,render_to_response,redirect
from .forms import SubscriberForm
from .forms import RegistrationForm,LoginForm
from products.models import ProductImage
from products.models import *
from orders.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def landing(request):

   form = SubscriberForm(request.POST or None)

   if request.method== "POST" and form.is_valid():
      print(request.POST)
      print(form.cleaned_data)
      new_form = form.save()

   return render(request, 'landing/landing.html',locals())

def home(request):
   products_images = ProductImage.objects.filter(is_active=True , is_main = True,  )
   products_images_electro = products_images.filter(product__category__id = 1,product__top = True,)
   category = Category.objects.all()

   return render(request, 'landing/home.html',locals())

def register(request):
   form = RegistrationForm(request.POST or None)
   if form.is_valid():
       # form.save(commit=False)
       user = form.save(commit=False)

       # Cleaned(normalized) data
       username = form.cleaned_data['username']
       password = form.cleaned_data['password']

       #  Use set_password here
       user.set_password(password)
       user.save()
       return HttpResponseRedirect(reverse('home'))
   context = {'form' : form}
   return render(request, 'landing/register.html', context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        login_user = authenticate(username=username,
                                  password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'landing/login.html', locals())

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

# метод просмотра  кабинета
def account(request):
   order = Order.objects.filter(customer_name = request.user )
   product = ProductInOrder.objects.filter(order__customer_name=request.user)
   wishlist = Wishlist.objects.filter(user = request.user)
   return render(request, 'landing/account.html', locals())

# метод просмотра заказа из кабинета
def order(request):
    data = request.POST
    order_id = data.get("order_id")
    product = ProductInOrder.objects.filter(order=order_id)
    # for att in dir(product):
    #         print (att, getattr(product, att))

    return render(request, 'modal_order.html', locals())
# вывод товара в модальное окно
def productview(request):
    data = request.POST
    product_id = data.get("product_id")
    product = ProductImage.objects.filter(is_active=True,product__id=product_id)
    # for att in dir(product):
    #         print (att, getattr(product, att))

    return render(request, 'modal_view_product.html', locals())

# вывод товара в модальное окно wishlist
def wishlist(request):
    data = request.POST
    product_id = data.get("product_id")
    product = ProductImage.objects.filter(is_active=True,product__id=product_id)
    product_wish = Product.objects.get( id=product_id)
    user = request.user
    get_wishlest = Wishlist.objects.filter(user=user,product=product_wish)
    if not get_wishlest:
        wishlist = Wishlist.objects.create(user=user,product=product_wish)
    # for att in dir(product_wish):
    #         print (att, getattr(product_wish, att))
    return render(request, 'wishlist_modal.html', locals())

def delete_item_in_wishlist(request,product_id):
    # print (product_id)
    product = Product.objects.filter(id = product_id)
    products_in_wishlist = Wishlist.objects.get (user = request.user,product = product )
    products_in_wishlist.delete()
    # return render(request, 'landing/checkout.html', locals())
    return HttpResponseRedirect('/account/')