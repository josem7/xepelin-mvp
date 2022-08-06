from django.urls import path

from mvp.views.main import MainView

urlpatterns = [
    path("", MainView.as_view()),
]
