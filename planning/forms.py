# planning/forms.py

from django import forms
from .models import WorkoutPlan, WorkoutSession, ScheduledWorkout

class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['exercise', 'description']

class WorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        fields = ['exercise', 'sets', 'reps', 'duration', 'rest_interval']
        widgets = {
            'duration': forms.TextInput(attrs={'placeholder': 'HH:MM:SS', 'pattern': '([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]', 'title': 'Enter a valid duration (HH:MM:SS)'}),
            'rest_interval': forms.TextInput(attrs={'placeholder': 'HH:MM:SS', 'pattern': '([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]', 'title': 'Enter a valid duration (HH:MM:SS)'}),
        }

class ScheduledWorkoutForm(forms.ModelForm):
    class Meta:
        model = ScheduledWorkout
        fields = ['workout_plan', 'date']
        
        widgets = {
            
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
