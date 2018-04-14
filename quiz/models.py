from django.db import models
from django.urls import reverse
from datetime import date
import uuid

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])

class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    # Unique id for a particular exam
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for a particular Exam")
    start_datetime = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
        verbose_name="Start Date & Time",
        help_text="Enter time in HH:MM format."
    )
    end_datetime = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
        verbose_name="End Date & Time",
        help_text="Enter time in HH:MM format."
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('exam_detail', args=[str(self.id)])


class Question(models.Model):
    TEXT = 'text'
    RADIO = 'radio'
    SELECT_MULTIPLE = 'select-multiple'

    QUESTION_TYPES = (
        (RADIO, 'Single Correct'),
        (SELECT_MULTIPLE, 'Multiple Correct'),
        (TEXT, 'Text'),
    )

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.CharField(max_length=1200, blank=False)
    figure = models.ImageField(blank=True, null=True)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default=RADIO)
    is_answered = models.BooleanField(default=False)
    is_marked = models.BooleanField(default=False)
    explanation = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.text

# class AnswerText(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer = models.TextField(max_length=1200)

# class AnswerMCQ(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     option = models.CharField(max_length=500)
#     is_correct = models.BooleanField(default=False)

# class options(models.Model):
#     question = models.ForeignKey(Question)
#     option_no = models.IntegerField()
#     option = models.TextField()
