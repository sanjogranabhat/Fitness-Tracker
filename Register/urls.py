from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    # path('user/', views.user, name='user'),
    path('trainer/', views.trainer, name='trainer'),
    path('logout/', views.logout_view, name='logout_view'),
]