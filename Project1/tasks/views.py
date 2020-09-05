from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm

def index(request):
	tasks = Task.objects.all()
	form = TaskForm()
	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	context = {'tasks':tasks, 'form':form}
	return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
	task = Task.objects.get(id=pk)
	task.complete = True
	task.save()
	return redirect('/')

def deleteTask(request, pk):
	try:
		item = Task.objects.get(id=pk)
		item.delete()
	except:
		pass 
		# item already deleted
	return redirect('/')

