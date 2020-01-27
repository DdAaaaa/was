from django.db import models
from django.contrib.auth.models import User

class QuaterBlock(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  level = models.IntegerField(default=0)
  created_date = models.DateTimeField()
  modified_date = models.DateTimeField()
  def __str__(self):
      return self.level

class Goal(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  goal = models.IntegerField()
  def __str__(self):
      return self.goal

class Sentences(models.Model):
  percentage = models.IntegerField()
  sentences = models.TextField()
  def __str__(self):
      return self.sentences