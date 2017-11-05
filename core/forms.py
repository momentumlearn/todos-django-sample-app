from django import forms
from core.models import BmiMeasurement

class BMIForm(forms.Form):
  """
  Height is in meters. Weight is in kg.
  """
  name = forms.CharField(required=False)
  height = forms.FloatField(label="Height in meters", required=True, min_value=0)
  weight = forms.FloatField(label="Weight in kg", required=True, min_value=0)

class BMIMeasurementForm(forms.ModelForm):
  class Meta:
    model = BmiMeasurement
    fields = ['height_in_meters', 'weight_in_kilograms', 'measured_at']