from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import *
from dashboard.views import *
# Create your views here.

def items(request):
    query = request.GET.get('query','')
    product = Product.objects.filter(is_sold=False).order_by('-created_at',)
    categories = ProductCategory.objects.all()
    category_id = request.GET.get('category',0)
    if query:
        product = product.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category_id:
        product = product.filter(category_id=category_id)
    return render(request,'details/browser.html',{
        'products':product,
        'query':query,
        'categories':categories,
        'category_id':int(category_id)
    })

def product_details(request,pk):
    product = get_object_or_404(Product, pk=pk)
    
    related = Product.objects.filter(category=product.category,is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'details/detail.html',{
        'product':product,
        'related':related,
    })


@login_required    
def new_product(request):
    
    if request.method == 'POST':
        form = AddProductForm(request.POST,request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('products:detail',pk = item.id)
        
    else:
        form =AddProductForm()
        
    return render(request,'details/form.html',{
        'form':form,
        'title':'New Item'
    })
    

@login_required    
def edit_product(request,pk):
    product = get_object_or_404(Product, pk=pk,created_by=request.user)
    if request.method == 'POST':
        form = EditProductForm(request.POST,request.FILES,instance=product)
        
        if form.is_valid():
            form.save()
            return redirect('products:detail',pk = product.id)
        
    else:
        form =EditProductForm(instance=product)
        
    return render(request,'details/form.html',{
        'form':form,
        'title':'Edit Item'
    })