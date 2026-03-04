from django.shortcuts import render ,redirect
from . models import task
from . forms import taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request ,'home.html')

@login_required 
def todolist(request):
    if request.method == "POST":
        form_data=taskform(request.POST or None)
        if form_data.is_valid():
            page=request.GET.get('page',1)
            instance = form_data.save(commit=False)
            instance.owner = request.user
            instance.save()
             
            messages.success(request,"task added successfully")
            return redirect(f"/todolist/?page={page}")
        
        messages.success(request,"something went wrong . ")
    
    all_task = task.objects.filter(owner = request.user)
    paginator = Paginator(all_task, 10)
    page = request.GET.get('page',1)
    
    all_task= paginator.get_page(page)
    
    context={
        'page':'todolist',
        'all_task':all_task,
    }
    return render (request,'todo.html',context)

@login_required
def delete(request,task_id):
    page= request.GET.get('page',1)
    task_obj=task.objects.get(id=task_id)
    task_obj.delete()
    messages.success(request," task deleted successfully")
    return redirect(f'/todolist/?page={page}') 
   
@login_required
def edit(request,task_id):
    task_obj=task.objects.get(id=task_id)
    if request.method == 'POST':
        page=request.GET.get('page')
        form_data=taskform(request.POST or None,instance=task_obj)
        if form_data.is_valid():
            form_data.save()
            messages.success(request," task update successfully")
            return redirect(f"/todolist/?page={page}")
    else:
        context = {
          'task_obj':task_obj
        }
    
        return render(request,'edit.html',context)
@login_required    
def complete(request,task_id):
    page=request.GET.get('page')
    task_obj = task.objects.get(id=task_id)
    task_obj.is_completed = True
    task_obj.save()
    messages.success(request,'status changed completed')
    return redirect(f'/todolist/?page={page}')

@login_required
def pending(request,task_id):
    page=request.GET.get('page')
    task_obj = task.objects.get(id=task_id)
    task_obj.is_completed = False
    task_obj.save()
    messages.success(request,'status changed pending')
    return redirect(f'/todolist/?page={page}')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request, 'about.html')
