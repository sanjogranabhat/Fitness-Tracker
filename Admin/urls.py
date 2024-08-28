from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminpanel, name='adminsite'),
    
    
    # Workouts
    path('workout-details/', views.workout_details_view, name='workout_details'),
    path('update-workout/<int:workout_id>/', views.update_workout_view, name='update_workout'),
    path('delete-workout/<int:workout_id>/confirm/', views.confirm_delete_workout, name='confirm_delete_workout'),
    
    
    
    # Exercise
    path('exercises/', views.admin_exercise_list, name='admin_exercise_list'),
    path('exercises/update/<int:pk>/', views.exercise_update, name='exercise_update'),
    path('exercises/delete/<int:pk>/', views.exercise_delete, name='exercise_delete'),
    
    
    
    # Goals
    path('goals/', views.admin_goals_view, name='admin_goals'),
    path('goals/update/<int:goal_id>/', views.update_goal_view, name='update_goal'),
    path('goals/delete/<int:goal_id>/', views.delete_goal_view, name='delete_goal'),
    
    
    # Scheduled Workouts 
    path('admin/scheduled-workouts/', views.view_scheduled_workouts, name='view_scheduled_workouts'),
    path('admin/scheduled-workouts/add/',views. add_scheduled_workout, name='add_scheduled_workout'),
    path('admin/scheduled-workouts/update/<int:pk>/', views.update_scheduled_workout, name='update_scheduled_workout'),
    path('admin/scheduled-workouts/delete/<int:pk>/', views.delete_scheduled_workout, name='delete_scheduled_workout'),
    
    
    
]
