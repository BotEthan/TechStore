from django.shortcuts import redirect, render
from django.urls import reverse
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import AuthenticationForm

from .models import ProductModel, BasketModel

@login_required(login_url='main:login')
def add_to_cart(request, product_id):
    product = get_object_or_404(ProductModel, pk=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        basket_item,created = BasketModel.objects.get_or_create(user=request.user, product_id=product_id, quantity=1)
        if not created:
            basket_item.quantity += quantity
            basket_item.save()
        else:
            basket_item.quantity = quantity
            basket_item.save()
        return redirect('main:home')
    return redirect('main:home')

def loginregister(request):
    return render(request, 'login.html')

# Create your views here.
def index(request):
    products = ProductModel.objects.all()
    categories = ProductModel.CATEGORY_CHOICES
    context = {
        'products' : products,
        'categories' : categories,
    }
    return render(request=request, template_name='index.html', context=context)

@login_required(login_url='main:login')
def basket(request):
    user = request.user
    basket_items = BasketModel.objects.filter(user=user)
    context = {'basket_items': basket_items}
    return render(request, 'basket.html', context)

def basketRemove(request, basket_id):
    basket_item = get_object_or_404(BasketModel, id=basket_id, user=request.user)
    basket_item.delete()
    return redirect('main:basket')

def logout_view(request):
    logout(request)
    return redirect('main:home')

def create_user(request):
    firstName = request.POST['firstname']
    username = request.POST['username']
    password = request.POST['password']
    if User.objects.filter(username=username).exists():
        return redirect('main:login')
    user = User.objects.create_user(username=username, password=password, email=None, **{'first_name': firstName})
    user.save()
    return redirect('main:login')


def attemptLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
        reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
        #reverse('user_auth:show_user')
        reverse('main:home')
        )