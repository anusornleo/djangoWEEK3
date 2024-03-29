from django.urls import path

from . import views

urlpatterns = [
  path('index/', views.index, name='index'),
  path('detail/<int:poll_id>/', views.detail, name='detail'),
  path('create/', views.create, name='create_poll')
]
