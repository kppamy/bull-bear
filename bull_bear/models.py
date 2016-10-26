from django.db import models

class Gamble(models.Model):
	description = models.CharField(max_length=200)

class Option(models.Model):
	gamble = models.ForeignKey(Gamble, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)

