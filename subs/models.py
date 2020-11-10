from django.db import models

# Create your models here.
class Sub(models.Model):
	name = models.CharField(max_length=200)
	subscribed_date = models.DateField()
	days = models.IntegerField(default=1)
	is_staff = models.BooleanField(default=False)
	active = models.BooleanField(default=True)