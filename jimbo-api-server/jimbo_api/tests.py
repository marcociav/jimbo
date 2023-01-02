from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from jimbo_server.models import Workout, Day, Section, Exercise, Muscle


class WorkoutTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(username='test_user', password='test_password')

    def test_crud_workout(self):
        self.client.login(username='test_user', password='test_password')

        # create
        data = {
            "title": "test workout", "description": "test description", "public": False, "user": self.test_user.id
        }
        url = reverse('jimbo_api:workoutlistcreate')
        post_response = self.client.post(url, data, format='json')
        print(f'POST response body: {post_response.data}')
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)

        # read
        url = reverse('jimbo_api:workoutdetail', kwargs={'pk': post_response.data['id']})
        get_response = self.client.get(url, format='json')
        print(f'GET response body: {get_response.data}')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        # update
        put_response = self.client.put(url, {
            "title": "edited title", "user": self.test_user.id
        })
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        print(f'PUT response body: {put_response.data}')

        # delete
        delete_response = self.client.delete(url, format='json')
        print(f'DELETE response body: {delete_response.data}')
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_view_all_workouts(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('jimbo_api:workoutlistcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
