from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.


def todoView(request):
    print(TodoItem.objects.all()[0].status)
    all_todo_items=TodoItem.objects.filter(author=request.user)#.filter(status == True)
    filtered_items = all_todo_items.filter(status = True)
    return render(request,'todo.html',
        {'all_items':filtered_items, 'todo': 'active'})

def addTodo(request):
    #find the attribute with the name content
    #c = request.POST['content']
    #new_item = TodoItem(content = c)
    new_item = TodoItem()
    new_item.content = request.POST['content']
    print(request.user.get_username())
    new_item.author = request.user.get_username()
    new_item.save()
    return HttpResponseRedirect('/todo/')
    
    #create a new todo all_items
    #save
    #redirect the browser to '/todo/'

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.status = False
    item_to_delete.save()
    return HttpResponseRedirect('/todo/')
    
def historyTodo(request):
    #print(request.user.get_username())
    all_todo_items=TodoItem.objects.all()
    return render(request,'todohistory.html',
        {'all_items':all_todo_items, 'todo_history': 'active'})

def teamContributions(request):
    context = {"team_contribution": "active"}
    return render(request, 'teamContributions.html', context)
