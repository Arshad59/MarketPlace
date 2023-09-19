from django.urls import path

from . import views

app_name='conversation'

urlpatterns = [
    path('',views.inbox_view,name="inbox"),
    path('<int:pk>/',views.detail,name="detail"),
    path('new/<int:pk>/',views.new_conversation,name="conversation")
]
