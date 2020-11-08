# Django
from django.urls import path

# Owns
from . import views

app_name = 'todo_list'

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('cross_off/<list_id>', views.cross_off, name='cross_off'),
    path('uncross/<list_id>', views.uncross, name='uncross'),
    path('edit-item/<list_id>', views.edit, name='edit'),
]
