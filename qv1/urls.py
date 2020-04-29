from django.contrib import admin
from django.urls import path, include
from qv1.views import QuizView
urlpatterns = [

    path('',QuizView.as_view(), name = "quizes"),

]