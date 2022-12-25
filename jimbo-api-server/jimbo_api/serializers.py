from rest_framework import serializers
from jimbo_server.models import Workout, Day, Section, Exercise, Muscle


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['title', 'description', 'user']
