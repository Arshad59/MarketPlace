from django.urls import path

from . import views
app_name="products"

urlpatterns = [
    path('new/',views.new_product,name="new"),
    path('items/',views.items,name="items"),
    path('<int:pk>/',views.product_details,name="detail"),
    path('<int:pk>/edit',views.edit_product,name="edit")
]
