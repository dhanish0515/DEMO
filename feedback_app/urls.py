from django.urls import path
from . import views

urlpatterns = [
    path('feedback', views.submit_feedback, name='feedback'),
    path('', views.show_feedback, name='submission'),
    path('edit/<pk>', views.edit_feedback, name='edit'),
    path('delete/<pk>', views.delete_feedback, name='delete'),
    path('signup', views.signup_view, name='signup'),
    path('signin', views.signin_view, name='signin'),
]
