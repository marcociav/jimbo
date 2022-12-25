from django.test import TestCase
from django.contrib.auth.models import User
from jimbo_server.models import Workout, Day, Section, Exercise, Muscle


class TestCreatePost(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(username='test_user', password='test_password')
        cls.test_workout = Workout.objects.create(
            title='Test Workout',
            description='Test Description',
            slug='test-workout',
            user_id=cls.test_user.id
        )

    def test_view_detail_workout(self):
        workout = Workout.objects.get(id=self.test_workout.id)

        user = str(workout.user)
        title = str(workout.title)
        description = str(workout.description)
        slug = str(workout.slug)

        self.assertEqual(user, 'test_user')
        self.assertEqual(title, 'Test Workout')
        self.assertEqual(description, 'Test Description')
        self.assertEqual(slug, 'test-workout')

        self.assertEqual(str(workout), 'Test Workout')
