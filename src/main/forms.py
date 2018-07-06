from django import forms

class SearchForm(forms.Form):
    search    = forms.CharField(required = True)

class CreateEvaluationForm(forms.Form):
    name        = forms.CharField(max_length = 120, required = True)
    price       = forms.FloatField(required = True)
    category    = forms.CharField(max_length = 120, required = True)
    mark        = forms.FloatField(required = True)
    evaluation  = forms.TextInput()
