#from . import views
#from django.urls import path

#urlpatterns = [
#    path('', views.home_page, name='home'),
#]

# Testing TemplateView method.
from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name='home')
]