from django.shortcuts import render,redirect
from items.models import * 

from .forms import SignUp

# Create your views here.
def index_view(request):
    products = Product.objects.filter(is_sold=False)
    categories = ProductCategory.objects.all()
    
    return render(request,'main/index.html',{
        'categories':categories,
        'products':products,
       
    })

def profile_view(request,username:str):
    return render(request,'main/index.html')
    

def contact_view(request):
    return render(request,'main/contact.html')


def about_view(request):
    return render(request,'main/about.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
        
    else:
        form = SignUp()
    
    
    return render(request,'main/signup.html',{
        'form':form
    })