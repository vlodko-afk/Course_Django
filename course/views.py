from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from .forms import CourseForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView
from django.db.models import Q
from itertools import chain
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend

def all_courses(request):
    search_query = request.GET.get('search', '')
    filter_query = request.GET.get('filter', '')
    day, month, year = datetime.now().day, datetime.now().month, datetime.now().year
    if search_query:
        all_course = [list(Course.objects.filter(Q(name = i.name))) for i in Course.objects.all() if search_query.lower() in i.name.lower()]
        all_course = list(set([j for i in all_course for j in i]))
        if filter_query == '2':
            all_course = [i[0] for i in sorted([[i, i.start_course]for i in all_course], key = lambda x: x[1])]
        elif filter_query == '3':
            all_course = [i for i in all_course if i.start_course.day == day]
        elif filter_query == '4':
                all_course = [i for i in all_course if i.start_course.month == month]
        elif filter_query == '5':
                all_course = [i for i in all_course if i.start_course.year == year]
    else:
        if filter_query:
            if filter_query == '1':
                all_course = Course.objects.all()
            elif filter_query == '2':
                all_course = Course.objects.all().order_by("start_course")
            elif filter_query == '3':
                all_course = [i for i in Course.objects.all() if i.start_course.day == day]
            elif filter_query == '4':
                all_course = [i for i in Course.objects.all() if i.start_course.month == month]
            elif filter_query == '5':
                all_course = [i for i in Course.objects.all() if i.start_course.year == year]
        else:
            all_course = Course.objects.all()
    """ Якщо кількість символів більша за вказану"""
    for i in all_course:
        if len(str(i.description)) > 90:
            i.description = i.description[:80] + " ..."
    return render(request, 'All_courses.html', {'all_course' : all_course})

class CourseDetailView(DetailView):
    model = Course
    template_name = r'Detail_course.html'
    context_object_name = 'dictionary'

class CourseCreateView(CreateView):
    template_name = r'Create_course.html'
    form_class = CourseForm
    queryset = Course.objects.all()


class CourseUpdateView(UpdateView):
    model = Course
    template_name =  r'Update_course.html'
    form_class = CourseForm


class CourseDeleteView(DeleteView):
    model = Course
    success_url = '/'
