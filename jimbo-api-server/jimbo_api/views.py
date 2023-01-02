from rest_framework import generics
from jimbo_server.models import Workout, Day, Section, Exercise, Muscle
from .serializers import WorkoutSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticatedOrReadOnly

# TODO: create permission (or new endpoint entirely) to handle viewing your private workouts


class WorkoutDetailUserWritePermission(BasePermission):
    message = 'You cannot access this workout.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and obj.public == 1:
            return True
        return obj.user == request.user


class WorkoutList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView, WorkoutDetailUserWritePermission):
    permission_classes = [WorkoutDetailUserWritePermission]
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
