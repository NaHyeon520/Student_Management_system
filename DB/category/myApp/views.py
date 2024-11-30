from django.shortcuts import render, redirect
from .forms import StudentsForm

# Create your views here.
from .models import Students


def display(request):
    students = Students.objects.all()
    return render(request, 'myApp/index.html', {"students": students})


def add(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, "myApp/add.html")


def update(request, stud_id):
    stud = Students.objects.get(id=stud_id)
    if request.method == "POST":
        form = StudentsForm(request.POST, instance=stud)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, 'myApp/update.html', {'student': stud})


def delete(request, stud_id):
    stud = Students.objects.get(id=stud_id)
    stud.delete()
    return redirect('index')
