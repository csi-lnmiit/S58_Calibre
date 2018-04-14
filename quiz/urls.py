from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('myexam/', views.myexam, name='myexam'),
    path('course/$', views.CourseListView.as_view(), name='course_list'),
    path('course/create/$', views.CourseCreate.as_view(), name='course_form'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
#    path('course/<int:pk>/exam/', views.CourseDetailView.as_view(), name='course_detail'),
    path('exam/new/<int:id>', views.create_exam, name='exam_form'),
    path('exam/<int:pk>', views.ExamDetailView.as_view(), name='exam_detail'),

]
