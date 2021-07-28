from django import forms
from .models import *

class AddPlan(forms.ModelForm):

    class Meta:
        model = Plans
        fields = ['name', 'comment', 'spent']