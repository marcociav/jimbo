from django.urls import path
from .views import WorkoutList, WorkoutDetail

app_name = 'jimbo_api'

urlpatterns = [
    # workouts
    path('<int:pk>/', WorkoutDetail.as_view(), name='detailcreate'),
    path('', WorkoutList.as_view(), name='listcreate')

    # days

    # exercises
]