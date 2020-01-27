from django.db import models
from django.contrib.auth.models import User


class QuarterBlock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    action_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.level


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.IntegerField()

    def __str__(self):
        return self.goal

