from argparse import Namespace
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('auth/', include('users.urls')),
    path('retorno/pagseguro/', include('pagseguro.urls')),
]
