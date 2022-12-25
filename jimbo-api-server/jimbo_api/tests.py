from django.urls import reverse
from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from jimbo_server.models import Workout, Day, Section, Exercise, Muscle


class WorkoutTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(username='test_user', password='test_password')

    def test_view_workouts(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('jimbo_api:workoutlistcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_workout(self):
        self.client.login(username='test_user', password='test_password')
        data = {
            "title": "test workout", "description": "test description", "user": self.test_user.id
        }
        url = reverse('jimbo_api:workoutlistcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
