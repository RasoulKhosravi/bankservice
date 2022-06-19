from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('bank_system_app/', include('bank_system_app.urls')),
]