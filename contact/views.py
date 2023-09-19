from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from items.models import Product
from .models import Conversation
from .forms import MessageForm
# Create your views here.


@login_required
def new_conversation(request,pk):
    product = get_object_or_404(Product,pk=pk)
    
    if product.created_by==request.user:
        return redirect('dashboard:dashboard')
    
    conversations = Conversation.objects.filter(item=product).filter(members__in=[request.user.id])
    
    if conversations:
        return redirect('conversation:detail',pk=conversations.first().id)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=product) 
            conversation.members.add(request.user)
            conversation.members.add(product.created_by)
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by=request.user
            conversation_message.save()
            
            return redirect('products:detail',pk=pk)
    else:
        form = MessageForm()
        
    return render(request,'conversation/new.html',{
        'form':form
    })
            
            
            
@login_required
def inbox_view(request):
     conversations = Conversation.objects.filter(members__in=[request.user.id])
     return render(request,'conversation/inbox.html',{
         'conversations':conversations
     })
     
     
@login_required

def detail(request,pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by=request.user
            conversation_message.save()
            
            return redirect('conversation:detail',pk=pk)
    else:
        form = MessageForm()
        
    return render(request,'conversation/detail.html',{
        'form':form
    })