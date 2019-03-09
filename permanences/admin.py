from django.conf.urls import url
from django.shortcuts import render, redirect
from django.contrib import admin
from django.http import HttpResponse
from django import forms

from datetime import date, timedelta

from .models import Activity, IndexPageData


class RecurringForm(forms.Form):
    description = forms.CharField(label='Description', initial='Permanence', max_length=100)
    begin_date = forms.DateField(label='Date de début (incluse)')
    end_date = forms.DateField(label='Date de fin (incluse)')
    DAYS = (
        (0, "Lundi"),
        (1, "Mardi"),
        (2, "Mercredi"),
        (3, "Jeudi"),
        (4, "Vendredi"),
        (5, "Samedi"),
        (6, "Dimanche"),
    )
    days = forms.MultipleChoiceField(label='Jours', widget=forms.CheckboxSelectMultiple, choices=DAYS)

    
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):  
    list_display = ('description', 'date', 'volunteer1', 'volunteer2', 'comment')

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url(r'^recurring/$', self.add_recurring_view, name='recurring'),
        ]
        return my_urls + urls

    def add_recurring_view(self, request):
        if request.method == 'POST':
            form = RecurringForm(request.POST)
            # todo save
            if form.is_valid():
                description = form.cleaned_data['description']
                begin_date = form.cleaned_data['begin_date']
                end_date = form.cleaned_data['end_date']
                delta = end_date - begin_date
                days = [int(d) for d in form.cleaned_data['days']]
                for i in range(delta.days + 1):
                    d = begin_date + timedelta(days=i)
                    if d.weekday() in days:
                        a = Activity(description=description, date=d)
                        a.save()
                return redirect('admin:permanences_activity_changelist') #cleanup
        else:
            form = RecurringForm()
        return render(request, 'admin/recurring.html',
                      { 'opts': self.model._meta, 'form': form})


admin.site.register(IndexPageData)


from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)
