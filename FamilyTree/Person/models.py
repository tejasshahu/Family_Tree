from django.db import models


# Person models here.
class Person(models.Model):

	GENDER_CHOICE = ((1, "Male"), (2, "Female"))

	num = models.BigIntegerField("Number", primary_key=True)
	first_name = models.CharField("First Name", max_length=15)
	last_name = models.CharField("Last Name", max_length=15)
	phone_number = models.BigIntegerField("Contact Number")
	email = models.EmailField("Email ID")
	address = models.CharField("Address", max_length=500)
	dob = models.DateField("Date of Birth")
	sex = models.IntegerField("Gender", choices=GENDER_CHOICE)

	class Meta:
		verbose_name_plural = 'Person'

	def __str__(self):
		return self.first_name
