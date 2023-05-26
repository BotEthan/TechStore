from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index),
    path('home/', views.index, name='home'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('basket/', views.basket, name='basket'),
    path('basket/remove-item/<int:basket_id>', views.basketRemove, name='basket_remove_item'),
    path('account/login', views.loginregister, name='login'),
    path('account/create-account', views.create_user, name='create_account'),
    path('account/attempt-login', views.attemptLogin, name='attempt_login'),
    path('logout/', views.logout_view, name='logout')
]