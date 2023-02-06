from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from engine.forms import Movieform
from engine.models import information, Movies


# def data(request):
# info = information.objects.all()
# content = {'infolist': info}
# return render(request, 'personal.html', content)


# def detail(request,infoli_st):
# return HttpResponse(infoli_st)


def movie(request):
    info = Movies.objects.all()
    content = {'infolist': info}
    return render(request, 'personal.html', content)


def detail(request, det):
    deta = Movies.objects.get(id=det)
    return render(request, 'detial.html', {'dett': deta})


def update(request, id):
    movie1 = Movies.objects.get(id=id)
    form = Movieform(request.POST or None, request.FILES, instance=movie1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie1})


def addmovie(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        star = request.POST.get('star')
        img = request.FILES['img']
        movie = Movies(name=name, desc=desc, star=star, img=img)
        movie.save()
    return render(request, 'add.html')


def delete(request,id):
    movied = Movies.objects.get(id=id)
    movied.delete()
    return redirect('/')
