from django.shortcuts import render,get_object_or_404,redirect
from items.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def dashboard_view(request):
    products = Product.objects.filter(created_by = request.user)
    return render(request,'dashboard/dashboard.html',{
        'products':products
    })
    
    
@login_required
def product_delete_view(request,pk):
    item = get_object_or_404(Product,pk=pk,created_by=request.user)
    
    item.delete()
    
    return redirect('dashboard:dashboard')
