from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('list/', views.EmployeeListView.as_view(), name='list'),
    path('create/', views.EmployeeCreateView.as_view(), name='create'),
    path('update/<pk>/', views.EmployeeUpdateView.as_view(), name='update'),
    path('delete/<pk>/', views.EmployeeUpdateView.as_view(), name='delete'),
]
