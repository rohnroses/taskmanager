from django.shortcuts import render, redirect
from .serializers import TaskSerializer
from rest_framework import viewsets
from django.http import HttpResponse
from .models import Task
from rest_framework.permissions import IsAuthenticated
from .forms import RegisterForm, TaskForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.template.context_processors import request

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, ]

class TaskHome(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'tasks/login.html', {'form':form})

class AddTask(LoginRequiredMixin, CreateView):
    form_class = TaskForm
    template_name = 'tasks/add_task.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user  # связываем задачу с текущим пользователем
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'status' , 'deadline']
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('home')   

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('home')
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm() 
        
    return render(request, "tasks/register.html", {"form": form})  