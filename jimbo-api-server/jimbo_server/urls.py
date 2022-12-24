from django.urls import path
from django.views.generic import TemplateView

app_name = 'jimbo_server'

urlpatterns = [
    path('', TemplateView.as_view(template_name='jimbo_server/index.html'))
]