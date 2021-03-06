from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader

from .models import Activity, HomePageData
from .forms import ActivityForm, TextForm

from datetime import date


def details(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'permanences/details.html', {'form': form})


def text(request):
    homedata = HomePageData.objects.first()
    if homedata is None:
        homedata = HomePageData.objects.create(txt="Cliquez en bas pour éditer ce texte ...")
    if request.method == "POST":
        form = TextForm(request.POST, instance=homedata)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TextForm(instance=homedata)
    return render(request, 'permanences/text.html', {'form': form})


def index(request):
    homedata = HomePageData.objects.first()
    if homedata is None:
        homedata = HomePageData.objects.create(txt="Cliquez en bas pour éditer ce texte ...")
    activity_list = Activity.objects.filter(date__gte=date.today()).order_by('date')
    return render(request, 'permanences/index.html', {'activity_list': activity_list, 'txt': homedata.txt})
