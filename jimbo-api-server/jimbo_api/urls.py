from django.urls import path
from .views import WorkoutList, WorkoutDetail

app_name = 'jimbo_api'

urlpatterns = [
    # workouts
    path('<int:pk>/', WorkoutDetail.as_view(), name='workoutdetail'),
    path('', WorkoutList.as_view(), name='workoutlistcreate')

    # days

    # exercises
]