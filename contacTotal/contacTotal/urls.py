from django.contrib import admin
from django.urls import path, include
from radioStation.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name="index"),
]