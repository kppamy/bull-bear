from django.db import models
from django.contrib.auth import models as auth_models
from django.db.models import signals
from django import dispatch

STARTING_REPUTATION = 0.0
STARTING_PREDICTION_CURRENCY = 5.0

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Outcome(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    likelihood = models.FloatField()
    creation_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.event.name + ": " + self.name

class Prediction(models.Model):
    user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    outcome = models.ForeignKey(Outcome, on_delete=models.CASCADE)
    staked_reputation = models.FloatField()
    creation_time = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    """
    Saves info about users.
    """
    user = models.OneToOneField(auth_models.User, on_delete=models.CASCADE)
    prediction_currency = models.FloatField(default=STARTING_PREDICTION_CURRENCY)
    reputation = models.FloatField(default=STARTING_REPUTATION)
    def __str__(self):
        return self.user.username + ": pc" + str(self.prediction_currency) + " rep" + str(self.reputation)


@dispatch.receiver(signals.post_save, sender=auth_models.User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@dispatch.receiver(signals.post_save, sender=auth_models.User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
