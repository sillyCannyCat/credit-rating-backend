from django.urls import path
from .views import ModelPools
urlpatterns = [
    path('analyse/', ModelPools.as_view(), name='analise')
]