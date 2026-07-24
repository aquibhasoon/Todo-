from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    task=tasks.objects.all().order_by("-id")

    form=taskform()
    context={'task': task , 'form':form}

    if request.method=='POST':
        form=taskform(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')

    return render(request,'task/list.html',context)

def Updatetask(request,pk):
    task=tasks.objects.get(id=pk)

    form=taskform(instance=task)
    if request.method=='POST':
        form=taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')


    context={'form':form}

    return render(request,'task/update_task.html',context)

def deleteTask(request,pk):
    item=tasks.objects.get(id=pk)


    if request.method=='POST':
        item.delete()
        return redirect('/')

    context={'item':item}


    return render(request,'task/delete.html',context)