from django.urls import path
from .views import EmployeeListView

app_name = 'employees'

urlpatterns = [
    path('list/', EmployeeListView.as_view(), name='list')
]