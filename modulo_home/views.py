from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	context = {}
	background = BackgroundFile.objects.all().first()
	todos = TodoItem.objects.all()

	if request.method == 'POST':
		if 'changeSettings' in request.POST:
			form = ConfigForm(request.POST, request.FILES)
			if form.is_valid():
				print('form valido')
				img = form.cleaned_data.get("img")
				print(type(img))
				category = form.cleaned_data.get("newcategory")
				deletes = form.cleaned_data.get("deletes").split(",")
				print(deletes)
				if category != '':
					cat = Category()
					cat.name = category
					cat.save()
				if img != None:					
					background.img_path = img
					background.save()
				if len(deletes) > 1:
					print('deletes para deletar')
					for cat_id in deletes:
						print(cat_id)
						try:
							cat = Category.objects.get(pk=cat_id)
							cat.delete()
						except:
							pass


		if 'newTask' in request.POST:
			form = NewTaskForm(request.POST)
			if form.is_valid():
				print('newTask')
				content = form.cleaned_data["title"]
				category = form.cleaned_data["category"]	
				due_date = form.cleaned_data["due_date"]
				todo = TodoItem()
				todo.content = content
				todo.category = category
				todo.due_date = due_date
				todo.save()

		if 'deleteTasks' in request.POST:
			checkedlist = request.POST.getlist("checkedbox")
			for todo_id in checkedlist:
				task = TodoItem.objects.get(pk=int(todo_id))
				task.delete()

		return redirect(index)
	else:
		request.method = 'GET'
		context['back'] = background.img_path.url
		context['form_config'] = ConfigForm()
		context['form_newtask'] = NewTaskForm()
		context['todos'] = todos
		context['categories'] = Category.objects.all()
		return render(request, "index.html", context)

def new_task(request):
	context = {}
	background = BackgroundFile.objects.get(pk=1)

	if request.method == 'POST':
		form = NewTaskForm(request.POST, request.FILES) 
		if form.is_valid():
			print('form valido')
			img = form.cleaned_data.get("img")
			background.img_path = img
			background.save()

	context['back'] = background.img_path.url
	context['form_background'] = BackgroundForm()
	
	return render(request, "index.html", context)
