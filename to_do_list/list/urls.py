from django.urls import path
from . import views
urlpatterns = [
    path('', views.home ,name='home'),
    path('todolist/', views.todolist ,name='todolist'),
    path('contact/', views.contact,name='contact'),
    path('about/', views.about ,name='about'),
    path('todolist/delete/<task_id>',views.delete,name='delete'),
    path('todolist/edit/<task_id>',views.edit,name='edit'),
    path('todolist/complete/<task_id>',views.complete,name='complete'),
    path('todolist/pending/<task_id>',views.pending,name='pending'),
]
