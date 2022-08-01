from django.shortcuts import render

# Create your views here.

from django.views.generic import View, CreateView, DeleteView, UpdateView, ListView
from django.http import HttpResponse
from .models import Question, Choice
from .forms import TestForm

class teste(CreateView):
    model = Question
    form_class = TestForm
    template_name = 'test_question.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TestForm
        return context
     