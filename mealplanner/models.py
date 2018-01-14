from django.db import models

# Create your models here.
from django.utils import timezone


class MealWeek(models.Model):
    meal_member = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)
    #TODO: auto-set this from a function that starts with a wednesday and contains the beginning week's calendar week and the dates included (e.g. "Week 29 - July 3rd - July 9th"
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    modified_date = models.DateTimeField(
            blank=True, null=True)
    #TODO: add fields can_modify(boolean), meals(boolean, 3 each day), ...

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
