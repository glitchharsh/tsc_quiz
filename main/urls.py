from django.urls import path
from .views import QuizView

urlpatterns = [
    path("", QuizView.as_view()),
]
