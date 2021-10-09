import datetime
from django import forms
from django.forms.widgets import SelectDateWidget

from .models import User


class RegistationForm(forms.ModelForm):
    dob = forms.DateField(input_formats=['%Y-%m-%d'], initial=datetime.date.today())
    
    def __init__(self, *args, **kwargs):
        super(RegistationForm, self).__init__(*args, **kwargs)
        #Change date field's widget here
        # self.fields['dob'].widget = SelectDateWidget()
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = User
        fields = ['fname', 'lname', 'email', 'dob', 'gender', 'role']
        