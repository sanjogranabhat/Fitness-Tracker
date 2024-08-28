from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from User. models import Member
from Dashboard. models import Workout
from Dashboard.forms import WorkoutForm
from Exercise.models import Exercise

from Exercise.forms import ExerciseForm
from Goal.models import Goal
from Goal.forms import GoalForm


from planning.models import ScheduledWorkout
from planning.forms import ScheduledWorkoutForm

# Create your views here.



def adminpanel(request):
    user=Member.objects.count()
    members = Member.objects.all()
    exercises = Exercise.objects.all()
    goals = Goal.objects.all()
    return render(request, 'Admin/adminsite.html',{'user':user,
                                                   'members':members,
                                                   'exercises': exercises,
                                                   'goals': goals,})
    


def workout_details_view(request):
    members = Member.objects.all()
    
    # Retrieve all workouts and group them by member
    workouts_by_member = {}
    for member in members:
        workouts = Workout.objects.filter(user=member.user)
        workouts_by_member[member] = workouts

    return render(request, 'Admin/workout_details.html', {
        'members': members,
        'workouts_by_member': workouts_by_member
    })
    
    
    
@login_required
def update_workout_view(request, workout_id):
    # Retrieve the specific workout by its ID
    workout = get_object_or_404(Workout, id=workout_id)

    if request.method == 'POST':
        # Bind the form to the POST data and the specific workout instance
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            # Save the updated workout
            form.save()
            return redirect('workout_details')  # Redirect to the workout details page after saving
    else:
        # Populate the form with the current workout data
        form = WorkoutForm(instance=workout)

    return render(request, 'Admin/update_workout.html', {'form': form})

@login_required
def confirm_delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    
    if request.method == 'POST':
        workout.delete()
        messages.success(request, 'The workout was successfully deleted.')
        return redirect('workout_details')  # Replace with the appropriate URL name for your workout list view
    
    return render(request, 'Admin/confirm_delete_workout.html', {'workout': workout})


# Exercise


@login_required
def admin_exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'Admin/admin_exercise_list.html', {'exercises': exercises})

@login_required
def exercise_update(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('admin_exercise_list')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'Exercise/exercise_form.html', {'form': form})

@login_required
def exercise_delete(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect('admin_exercise_list')
    return render(request, 'Exercise/exercise_confirm_delete.html', {'exercise': exercise})




#User Goals


def admin_goals_view(request):
    goals = Goal.objects.all()  # Fetch all goals
    return render(request, 'Admin/admin_goals.html', {'goals': goals})


@login_required
def update_goal_view(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('admin_goals')  # Redirect to the goals page after saving
    else:
        form = GoalForm(instance=goal)

    return render(request, 'Admin/update_goal.html', {'form': form, 'goal': goal})

@login_required
def delete_goal_view(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    if request.method == 'POST':
        goal.delete()
        return redirect('admin_goals')  # Redirect to the goals page after deleting
    return render(request, 'Admin/delete_goal_confirm.html', {'goal': goal})


# Scheduled workouts 
@login_required
def view_scheduled_workouts(request):
    scheduled_workouts = ScheduledWorkout.objects.all()
    return render(request, 'Admin/view_scheduled_workouts.html', {'scheduled_workouts': scheduled_workouts})

# Add Scheduled Workout
@login_required
def add_scheduled_workout(request):
    if request.method == 'POST':
        form = ScheduledWorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_scheduled_workouts')
    else:
        form = ScheduledWorkoutForm()
    return render(request, 'Admin/add_scheduled_workout.html', {'form': form})

# Update Scheduled Workout
@login_required
def update_scheduled_workout(request, pk):
    scheduled_workout = get_object_or_404(ScheduledWorkout, pk=pk)
    if request.method == 'POST':
        form = ScheduledWorkoutForm(request.POST, instance=scheduled_workout)
        if form.is_valid():
            form.save()
            return redirect('view_scheduled_workouts')
    else:
        form = ScheduledWorkoutForm(instance=scheduled_workout)
    return render(request, 'Admin/update_scheduled_workout.html', {'form': form})

# Delete Scheduled Workout
@login_required
def delete_scheduled_workout(request, pk):
    scheduled_workout = get_object_or_404(ScheduledWorkout, pk=pk)
    if request.method == 'POST':
        scheduled_workout.delete()
        return redirect('view_scheduled_workouts')
    return render(request, 'Admin/delete_scheduled_workout_confirm.html', {'scheduled_workout': scheduled_workout})