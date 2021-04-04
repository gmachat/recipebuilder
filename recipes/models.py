from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField
from django.core.validators import MinValueValidator, MaxValueValidator

import json

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Recipe(models.Model):
    name = models.CharField(max_length=256)
    cook_time = models.IntegerField()
    prep_time = models.IntegerField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='created_recipes', null=True)
    saved_by = models.ManyToManyField(UserProfile, related_name='saved_recipes', null=True)
    liked_by = models.ManyToManyField(UserProfile,  related_name='liked_recipes', null=True)
    # ingredients is a list of IDs from external api
    ingredients = JSONField(null=True)


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ratings')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])