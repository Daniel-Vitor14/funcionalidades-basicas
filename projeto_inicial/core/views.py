from django.shortcuts import render
from django.views.generic import View, CreateView, DeleteView, UpdateView, ListView
from django.http import HttpResponse


def index(request):
    return HttpResponse("Daleeeeeeeee.")

class BaseHtml(View):
    template_name = 'base.html'

    def get(self,request):    
        
        return render(request, self.template_name)