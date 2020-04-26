from django.contrib import admin
from Person.models import Person
from Relationship.models import Relationship


class RelationshipInline(admin.StackedInline):
	"""docstring for RelationshipInlines"""
	model = Relationship
	verbose_name = 'Relationships'
	verbose_name_plural = 'Relationships'
	extra = 0
	fk_name = 'person'

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
	inlines = [RelationshipInline, ]
	list_display = ('num', 'first_name', 'last_name', 'dob', 'sex', )
	search_fields = ["num", "first_name", "sex"]


admin.site.register(Person, PersonAdmin)