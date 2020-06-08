from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def indexView(request):
	return render(request,'index.html')


@login_required
def dashboardView(request):
	tasks = Task.objects.all()
	form = TaskForm()
	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('dashboard')
	context = {'tasks':tasks, 'form':form}
	return render(request,'tasks/dashboard.html',context)


def registerView(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login_url')
	else:
		form=UserCreationForm()


	return render(request,'registration/register.html',{'form':form})

# Create your views here.


	

def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('dashboard')

	context = {'form':form}

	return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('dashboard')

	context = {'item':item}
	return render(request, 'tasks/delete.html', context)



