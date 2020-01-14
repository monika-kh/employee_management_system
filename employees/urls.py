from django.urls import path
from .views import EmployeeCreateView, AllEmployeeListView, OneEmployeeRetrieveView, EmployeeUpdateView, \
    EmployeeDestroyView, RelationshipCreateView, RelationshipRetrieveUpdateDestroyView

urlpatterns = [
    path('emp_create/', EmployeeCreateView.as_view()),
    path('emp_list/', AllEmployeeListView.as_view()),
    path('emp_retrieve/<int:pk>/', OneEmployeeRetrieveView.as_view()),
    path('emp_update/<int:pk>/', EmployeeUpdateView.as_view()),
    path('emp_delete/<int:pk>/', EmployeeDestroyView.as_view()),

    path('re_create_list/', RelationshipCreateView.as_view()),
    path('re_retrieve_update_delete/<int:pk>/', RelationshipRetrieveUpdateDestroyView.as_view()),

]
