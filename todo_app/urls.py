from django.urls import path
from .  import views



urlpatterns = [
    path("todo/",views.todo_view),
    path("addtodo/",views.addtodo),
    path("deletetodo/<int:todo_id>/",views.deletetodo)
    
]
