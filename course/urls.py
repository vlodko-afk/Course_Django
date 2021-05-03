from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_courses, name = 'courses'),
    path('<int:pk>', views.CourseDetailView.as_view(), name = 'detail_course'),
    path('create/', views.CourseCreateView.as_view(), name = 'create_course'),
    path('<int:pk>/update', views.CourseUpdateView.as_view(), name = 'update_course'),
    path('<int:pk>/delete', views.CourseDeleteView.as_view(), name = 'delete_course'),
]