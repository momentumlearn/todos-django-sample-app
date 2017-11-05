from django.shortcuts import render
from django.http import HttpResponse
from core.forms import BMIForm

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