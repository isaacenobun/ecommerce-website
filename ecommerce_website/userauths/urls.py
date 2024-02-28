from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('logout/',views.log_out, name='logout')
]