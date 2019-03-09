from django import forms

from .models import Activity, IndexPageData

class ActivityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['readonly'] = True
        self.fields['date'].widget.attrs['readonly'] = True
    class Meta:
        model = Activity
        fields = '__all__'
        # widgets = {
        #     'date': DateInput(),
        # }

class TextForm(forms.ModelForm):
    class Meta:
        model = IndexPageData
        fields = '__all__'
