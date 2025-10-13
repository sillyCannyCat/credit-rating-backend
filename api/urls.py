from django.urls import path
from .views import ModelPoolsView

urlpatterns = [
    path('analyse/', ModelPoolsView.as_view(), name='analyse')
]
