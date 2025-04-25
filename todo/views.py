from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import TodoForm
from .models import Todos
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView

# Create your views here.
def home(request):
    return HttpResponse("Hello World")

# class HomeView(View):
#     def get(self, request):
#         todos = Todos.objects.all()
#         return render(request, 'todo/index.html', {'todos':todos})

class HomeView(ListView):
    model = Todos
    template_name = 'todo/index.html'
    context_object_name = 'todos'
    ordering = '-id'

    def get_queryset(self):
        return Todos.objects.filter(todo__icontains = 'Django')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = 'The ToDo is for Vishal'
        return context
    
class AddView(View):
    def get(self, request):
        form = TodoForm()
        return render(request, 'todo/add.html', {'form':form})
    
    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'todo/add.html', {'form':form})
        
class AboutView(TemplateView):
    template_name = 'todo/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_name'] = 'Vishal Saxena'
        # context['name_from_url'] = kwargs['name_from_url']
        return context

class RedirectAbout(RedirectView):
    url = '/about/'

class RedirectAbout_1(RedirectView):
    pattern_name = 'home'
    query_string = True
