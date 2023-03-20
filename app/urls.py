from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('cancel/<uuid:task_id>', views.CancelTask, name='cancel-task'),
]
