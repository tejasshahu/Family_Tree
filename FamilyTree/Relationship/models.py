from django.db import models
from Person.models import Person

# Relationship models here.
class Relationship(models.Model):

	SELECT_RELATION = (
		(1, "Father"),
		(2, "Mother"),
		(3, "Grand Father"),
		(4, "Grand Mother"),
		(5, "Brother"),
		(6, "Sister"),
		(7, "Son"),
		(8, "Daughter"),
		(9, "Husband"),
		(10, "Wife"),
		(11, "Uncle"),
		(12, "Aunty")
	)

	person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person')
	relation = models.IntegerField(choices=SELECT_RELATION)
	related_person = models.ForeignKey(Person, on_delete=models.CASCADE, 
		related_name='related_person', verbose_name='Related Person')

	class Meta:
		verbose_name_plural = 'Relationships'
