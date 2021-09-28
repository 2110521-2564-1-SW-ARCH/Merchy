from django import forms
# from django.forms.extras.widgets import SelectDateWidget

from .models import User


class RegistationForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(RegistationForm, self).__init__(*args, **kwargs)
        #Change date field's widget here
        # self.fields['date'].widget = SelectDateWidget()
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = User
        fields = ['fname', 'lname', 'email', 'gender', 'role']
        