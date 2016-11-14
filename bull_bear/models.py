from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Outcome(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    likelihood = models.FloatField()
    def __str__(self):
        return self.event.name + ": " + self.name

