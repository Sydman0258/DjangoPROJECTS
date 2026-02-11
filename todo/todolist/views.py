from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoForms

def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method=="POST":
        form=TodoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form=TodoForms()

    page={
        "forms":form,
        "list":item_list,
        "title":"TODO LIST",
    }
    return render(request,'todolist/index.html',page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')


