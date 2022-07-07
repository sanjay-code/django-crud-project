from django.db import models

# Create your models here.

class People_data(models.Model):
	name = models.CharField(max_length=150)
	email = models.EmailField(max_length=200)
	phone = models.IntegerField()
	date_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-date_time']
    