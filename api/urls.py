from django.urls import path
from .views import ModelPools
urlpatterns = [
    path('analise/', ModelPools.as_view(), name='analise')
]