# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Membership, UserMembership
from datetime import timedelta

@login_required
def simulate_payment(request, plan_type):
    membership = Membership.objects.get(plan_type=plan_type)
    end_date = timezone.now() + timedelta(days=membership.duration_days)
    UserMembership.objects.update_or_create(
        user=request.user,
        defaults={'membership': membership, 'start_date': timezone.now(), 'end_date': end_date}
    )
    return redirect('membership_status')

@login_required
def membership_plans(request):
    memberships = Membership.objects.all()
    return render(request, 'Membership/membership_plans.html', {'memberships': memberships})

@login_required
def membership_status(request):
    user_membership = UserMembership.objects.filter(user=request.user).first()
    return render(request, 'Membership/membership_status.html', {'user_membership': user_membership})

@login_required
def purchase_membership(request, plan_type):
    membership = Membership.objects.get(plan_type=plan_type)
    end_date = timezone.now() + timedelta(days=membership.duration_days)
    UserMembership.objects.update_or_create(
        user=request.user,
        defaults={'membership': membership, 'start_date': timezone.now(), 'end_date': end_date}
    )
    return redirect('home')
