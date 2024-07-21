# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('membership-plans/', views.membership_plans, name='membership_plans'),
    path('purchase-membership/<str:plan_type>/', views.purchase_membership, name='purchase_membership'),
    path('simulate-payment/<str:plan_type>/', views.simulate_payment, name='simulate_payment'),
    path('membership-status/', views.membership_status, name='membership_status'),
    # Add other service views here
]
