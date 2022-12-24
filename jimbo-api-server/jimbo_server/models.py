from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Workout(models.Model):
    # general info
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=4000, null=True)

    # meta info
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


class Section(models.Model):
    # general info
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, null=True)

    # meta info
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return self.title


class Exercise(models.Model):
    # general info
    name = models.CharField(max_length=250)
    # TODO: create category for both sets and reps to allow "AMRAP" or similar
    sets = models.IntegerField()
    reps = models.IntegerField()

    # detailed info
    description = models.TextField(max_length=1000, null=True)

    # meta info
    order = models.IntegerField()  # needs to be gotten from the order in which the user entered the exercises
    published = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='exercises')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.name


class Muscle(models.Model):
    name = models.CharField(max_length=250)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='muscles')

    def __str__(self):
        return self.name
