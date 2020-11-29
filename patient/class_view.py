from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .forms import PatientForm
from .models import Patient
from django.urls import reverse_lazy

class PatientList(ListView):
    model = Patient
    template_name = 'index.html'

 #   def get_queryset(self):
 #       return self.model.objects.all()[:2]


class PatientCreate(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'Create_patient.html'
    success_url = reverse_lazy('index')

class PatientUpdate(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'Create_patient.html'
    success_url = reverse_lazy('index')

class PatientRemove(DeleteView):
    model = Patient
    template_name = 'verification.html'
    success_url = reverse_lazy('index')