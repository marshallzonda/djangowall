from django.urls import path
from .views import index, by_rubric

urlpatterns = [
    path('<rubric_id>/',by_rubric),
    path('', index),
]