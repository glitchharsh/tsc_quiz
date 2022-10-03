from django.urls import path, re_path
from .views import QuizView
from django.views.static import serve 
from django.conf import settings

urlpatterns = [
    path("", QuizView.as_view()),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
