from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Course, Exam
from django.contrib.auth import login

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def myexam(request):
    return render(request, 'myexam.html')

class CourseListView(generic.ListView):
    model = Course

class CourseDetailView(generic.DetailView):
    model = Course

class CourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['course_name', 'description']

class ExamDetailView(generic.DetailView):
    model = Exam

# class ExamCreate(LoginRequiredMixin, CreateView):
#     model = Exam
#     fields = '__all__'

def create_exam(request, id):
    context = {
        "cid": id
    }
    return render(request, 'quiz/exam_form.html', context)