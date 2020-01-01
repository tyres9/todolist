from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo_models



# Create your views here.


def todo_view(request):
    todo_items = Todo_models.objects.all()
    return render(request,'todo.html',{'todo_items' : todo_items})

def addtodo(request):
    new_todo =  request.POST['content']
    date_new_todo  =  request.POST['date_todo']
    new_item = Todo_models(content = new_todo, date_todo=date_new_todo)
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deletetodo(request,todo_id):
    delete_todo = Todo_models.objects.get(id = todo_id)
    delete_todo.delete()
    return HttpResponseRedirect('/todo/')