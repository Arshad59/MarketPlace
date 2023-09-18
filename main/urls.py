from django.urls import path
from django.contrib.auth import views as authorization
from . import views
from .forms import Login
app_name="main"

urlpatterns = [
    path('home/',views.index_view,name="index"),
    path('contact/',views.contact_view,name="contact"),
    path('about/',views.about_view,name="about"),
    path('signup/',views.signup_view,name="signup"),
    # path('profile/<str:username>',views.profile_view,name="profile"),
    path('login/',authorization.LoginView.as_view(template_name='main/login.html', authentication_form=Login),name='login')
]
