from django.contrib import admin
from .models import Course, Exam, Question
# Register your models here.
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Question)

