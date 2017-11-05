from django import forms

class BMIForm(forms.Form):
  """
  Height is in meters. Weight is in kg.
  """
  name = forms.CharField(required=False)
  height = forms.FloatField(label="Height in meters", required=True, min_value=0)
  weight = forms.FloatField(label="Weight in kg", required=True, min_value=0)