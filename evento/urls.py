from django.urls import path
from . import views

urlpatterns = [
    path('event/', views.read_events),
    path('event/<int:pk>', views.read_one_event),
    path('event/criar', views.create_event),
    path('event/proximoseventos', views.next_events),
    path('event/atualizar/<int:pk>', views.update_event),
    path('event/deletar/<int:pk>', views.delete_event),
]