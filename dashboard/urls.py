from django.urls import path

from .views import *

app_name='dashboard'

urlpatterns = [
    path('',dashboard_view,name='dashboard'),
    path('<int:pk>',product_delete_view,name="delete")
]
