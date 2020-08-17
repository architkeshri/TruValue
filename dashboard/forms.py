from django import forms
from .models import PhoneModels
from bootstrap_datepicker_plus import DatePickerInput


class PhoneInfo(forms.ModelForm):


    warranty_period = forms.CharField(label='Is the phone in warranty period?',
                                    widget=forms.Select(choices=
                                                        [('Yes','Yes'),
                                                         ('No','No')]
                                                        ))

    charger = forms.CharField(label='Does the phone has working charger?',
                                    widget=forms.Select(choices=
                                                        [('Yes','Yes'),
                                                         ('No','No')]
                                                        ))
    refurbished = forms.CharField(label='Phone Repaired?',
                              widget=forms.Select(choices=
                                                  [('Yes', 'Yes'),
                                                   ('No', 'No')]
                                                  ))
    purchase_date = forms.DateField(label='Date of Purchase',widget=DatePickerInput())




    class Meta:
        model = PhoneModels
        fields = ['model_name','model_price','model_variant']
        widgets = {

            'model_name':forms.TextInput(attrs={'readonly': True}),
            'model_price': forms.TextInput(attrs={'readonly': True}),
            'model_variant': forms.TextInput(attrs={'readonly': True}),


        }



