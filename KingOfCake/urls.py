from sys import path_hooks
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("manageCake.urls")),
    path('customer/', include('managecustomers.urls')),
    path('cart/', include('managecart.urls')),
]
