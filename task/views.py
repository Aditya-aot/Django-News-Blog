
from django.shortcuts import render
from .models import task_model
from .forms import TaskForm
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
    form = TaskForm()
    task_data = task_model.objects.all()

    if request.method == 'POST' :
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()


    context = { 'form':form ,
                'task_data' : task_data[::-1]

    }


    return render(request, 'home.html', context)


#creating delete view
def delete_view(request , task_id) :
    task_to_delete = task_model.objects.get(id=task_id)
    task_to_delete.delete()
    return HttpResponseRedirect('/task/') 



#to be coming 
#any idea 
