from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(login_required, name="dispatch")
class BaseView(View):
    def __init__(self):
        self.data = {}
