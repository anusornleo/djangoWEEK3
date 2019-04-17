from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError('%(value)s not even',params={'value':value})

class PollForm(forms.Form):
    title = forms.CharField(label="Name poll",max_length=100,required=True)
    email = forms.CharField(validators=[validators.validate_email])
    no_questions = forms.IntegerField(label="count q",min_value=0,max_value=10,required=True, validators=[validate_even])
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)

    def clean_title(self):
        data = self.cleaned_data['title']
        if "IT" not in data:
            raise forms.ValidationError("please input IT")
        return data

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')

        if start and not end:
            # raise forms.ValidationError("forget enddate")
            self.add_error('end_date','forgot end date')
        if end and not start:
            # raise forms.ValidationError("forget startdate")
            self.add_error('end_date', 'forgot start date')