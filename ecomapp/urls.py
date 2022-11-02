from django.urls import path
from .views import *

app_name = "ecomapp"
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('product/<slug:slug>/',ProductDetailView.as_view(),name="productdetail"),
    path('all-products/', AllProductsView.as_view(), name="allproducts"),
    path('add-to-cart-<int:pro_id>/', AddToCartView.as_view(), name="addtocart"),
    path('my-cart/',MyCartView.as_view(),name="mycart"),
    path('search/',SearchView.as_view(),name="search"),
    path('manage-cart/<int:cp_id>/',ManageCartView.as_view(), name="managecart"),
    path('checkout/',CheckoutView.as_view(), name="checkout"),
    path('register/',CustomerRegistrationview.as_view(), name="customerregistration"),
    path('logout/', CustomerLogoutView.as_view(), name="customerlogout"),
    path('login/', CustomerLoginView.as_view(),name="customerlogin"),
    path('profile/',CustomerProfileView.as_view(), name="customerprofile"),
    path('profile/order-<int:pk>', CustomerOrderDetailView.as_view(), name="customerorderdetail"),
    path('admin-login/', AdminLoginView.as_view(), name="adminlogin"),
    path('admin-home/', AdminHomeView.as_view(), name="adminhome" ),
    path('admin-order/<int:pk>/', AdminOrderDetailView.as_view(), name="adminorderdetail"),
    path('admin-all-orders/', AdminOrderListView.as_view(), name="adminorderlist"),
    path('admin-order-<int:pk>-change/', AdminOrderStatuschangeView.as_view(), name="adminorderstatuschange"),


]

