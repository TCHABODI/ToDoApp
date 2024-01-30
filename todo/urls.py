from django.urls import path
from todo import views

urlpatterns = [
    path('addtask/',views.addTask,name = 'addtask'),
    path('mark_as_done/<int:pk>',views.mark_as_done, name= 'task_as_done'),
    path('mark_as_incomplete/<int:pk>',views.mark_as_incomplete, name= 'mark_as_incomplete'),
    path('edit_task/<int:pk>',views.edit_task, name= 'edit_task')
]