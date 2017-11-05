from django.shortcuts import render
from django.http import HttpResponse
from core.forms import BMIForm, BMIMeasurementForm
from core.models import BmiMeasurement

# Create your views here.

def greeting_view(request):
  return render(request, "greeting.html")

def goodbye_view(request):
  return HttpResponse("Goodbye!")

def bmi(request):
  if request.method == "POST":
    form = BMIForm(request.POST)
    if form.is_valid():
      height = form.cleaned_data['height']
      weight = form.cleaned_data['weight']
      bmi = weight / (height * height)
      return render(request, "bmi.html", {"form": form, "bmi": bmi})
  else:
    form = BMIForm()

  return render(request, "bmi.html", {"form": form})

def bmi_measurement(request):
  if request.method == "POST":
    form = BMIMeasurementForm(request.POST)
    if form.is_valid():
      measurement = form.save()

      measurements = BmiMeasurement.objects.order_by("measured_at").all()

      return render(request, "measurement_recorded.html", 
        {"measurements": measurements})
  else:
    measurements = BmiMeasurement.objects.order_by("measured_at").all()
    form = BMIMeasurementForm()

  return render(request, "measurement.html", {"form": form, "measurements": measurements})