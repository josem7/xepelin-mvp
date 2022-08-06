from django.shortcuts import render
from mvp.views.base import BaseView


class MainView(BaseView):
    def get(self, request):
        return render(request, "mvp/main.html", self.data)
