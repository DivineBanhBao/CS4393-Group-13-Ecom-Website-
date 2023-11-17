from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('product/<int:pk>', views.product, name='product'), #go to product page based on product (primary key) number
    path('category/<str:cate>',views.category,name='category'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('view-cart/', views.view_cart, name='view_cart'),
    path('cart_count/', views.cart_count, name='cart_count'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment_confirmation/', views.payment_confirmation, name='payment_confirmation'), 
]