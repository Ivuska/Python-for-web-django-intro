from django.urls import path
from . import views

'''
Django umoznuje psat pohledy jako funkce, tak i jako tridy. 
Rozhodne je lepsi je psat vzdy jako tridy jako v nasem projektu.
'''

urlpatterns =  [
    path('', views.IndexView.as_view(), name='index'),
    path('contacts', views.ContactsView.as_view(), name='contacts'),
    path('aboutus', views.AboutUsView.as_view(), name='aboutus'),
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('branches/', views.BranchListView.as_view(), name='branch_list') ,
    path('persons/', views.PersonListView.as_view(), name='person_list'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
    path('branch/<int:pk>', views.BranchDetailView.as_view(), name='branch_detail'),
    path('application/<int:pk>', views.ApplicationCreateView.as_view(), name='application_create'),
    path('confirmation/', views.ApplicationConfirmation.as_view(), name='application_confirmation'),
    path('registration/', views.PersonRegister.as_view(), name='person_register'),
    path('registration/confirmation', views.PersonRegisterConfirmation.as_view(), 
    name='register_confirmation'),
]