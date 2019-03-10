from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader

from .models import Activity, IndexPageData
from .forms import ActivityForm, TextForm

from datetime import date


indexpagedata = IndexPageData.objects.first()
if indexpagedata is None:
    indexpagedata=IndexPageData.objects.create(txt="Cliquez en bas pour éditer ce texte ...")

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
    if request.method == "POST":
        form = TextForm(request.POST, instance=indexpagedata)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TextForm(instance=indexpagedata)
    return render(request, 'permanences/text.html', {'form': form})


def index(request):
    activity_list = Activity.objects.filter(date__gte=date.today()).order_by('date')
    return render(request, 'permanences/index.html', {'activity_list': activity_list, 'txt': indexpagedata.txt})
