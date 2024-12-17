from django.shortcuts import render, redirect
from .models import Tasks, History

# Create your views here.
def index(request):
    # data = Tasks.objects.all().order_by('id')
    # context = {
    #     'data':data
    # }
    # return render(request,'index.html',context)
    query = request.GET.get('search', '')
    if query:
        data = Tasks.objects.filter(task__icontains=query)
    else:
        data = Tasks.objects.all()
    return render(request,'index.html',{'data':data, 'is_index':True})

def create(request):
    edit = False
    if request.method == "POST":
        task = request.POST.get('task')
        description = request.POST.get('description')
        # print(name,author,price,genre,quantity,rating)
        a = Tasks.objects.create(task = task, description = description)
        return redirect("create")
    return render(request,'add.html',{'edit':edit})

def display(request,pk):
    data1 = Tasks.objects.get(id=pk)
    if request.method == "POST":
        b = History.objects.create(htask = data1.task, hdescription = data1.description)
        data1.delete()
        return redirect("index")
    context = {
        'data1':data1
    }
    return render(request,'display.html',context)

def edit(request,ab):
    edit = True
    data2 = Tasks.objects.get(id = ab)
    
    if request.method == "POST":
        task = request.POST.get('task')
        description = request.POST.get('description')
        print(task,description)
        data2.task = task
        data2.description = description
        data2.save()
        return redirect("index")
        # print(name,author,price,genre,quantity,rating)
    context = {
        'data2':data2,
        'edit':edit
    }
    return render(request,'edit.html',context)

def history(request):
    htable = History.objects.all()
    context = {
        'htable' : htable
    }
    return render(request,'history.html',context)

def delete(request,hi):
    data4 = History.objects.get(id=hi)
    data4.delete()
    return redirect('history')