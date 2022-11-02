from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
from ecomapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("ecomapp.urls")),
    path('search/',SearchView.as_view(),name="search"),
    path('add-to-cart-<int:pro_id>/', AddToCartView.as_view(), name="addtocart"),
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)