from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader

from .models import Activity, IndexPageData
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
    txt = IndexPageData.objects.get()
    if request.method == "POST":
        form = TextForm(request.POST, instance=txt)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TextForm(instance=txt)
    return render(request, 'permanences/text.html', {'form': form})


def index(request):
    activity_list = Activity.objects.filter(date__gte=date.today()).order_by('date')
    txt = IndexPageData.objects.get()
    return render(request, 'permanences/index.html', {'activity_list': activity_list, 'txt': txt.txt})
