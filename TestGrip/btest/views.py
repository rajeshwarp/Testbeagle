from cgi import test
from pyexpat import model
from unicodedata import name
from django.shortcuts import render
from django.views.generic import CreateView, FormView, ListView
from .models import Step, Test
from django.urls import reverse_lazy
# Create your views here.

class CreateStep(CreateView):
    model= Step
    fields= "__all__"

    success_url = reverse_lazy('btest:home')


class CreateTest(CreateView):
    model= Test
    fields= "__all__"
    success_url = reverse_lazy('btest:home')

def homepage(request):
        return render(request, 'btest/home.html')

class ListTest(ListView):
    model = Test
    context_object_name = 'listTest'
    #template_name = 'btest/home.html'
   # paginate_by = 5 # 5 book instances per page

   # def get_queryset(self):
   #     return Test.objects.all() 