#from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import Category, City, Restaurant, Payment
from django.contrib.auth import logout as auth_logout


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'categories': Category.objects.all(),
            'payments': Payment.objects.all(),
            'cities': City.objects.all(),
            'restaurants': Restaurant.objects.all()[:5],
            'path': self.request.path,
        }


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')