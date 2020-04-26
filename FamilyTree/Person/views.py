from django.shortcuts import render, redirect
from django.forms import ModelForm

from Person.models import Person
from Relationship.models import Relationship


# Create your views here.
def index(request):
	all_members = Person.objects.all()
	response_json = {}
	response_json["members"] = all_members
	template = 'person/index.html'
	if request.method == 'POST':
		if request.POST.get("relation"):
			selected_relation = request.POST.get("relation")
			request.session['person_id'] = request.POST.get("selected")
			if selected_relation == "sibling":
				return redirect("/siblings")
			elif selected_relation == "parents":
				return redirect("/parents")
			elif selected_relation == "children":
				return redirect("/children")
			elif selected_relation == "children":
				return redirect("/children")
			elif selected_relation == "children":
				return redirect("/children")
	return render(request, template, response_json)

def display_parents(request):
	"""
	Method to get parents of passed person_id of family member.
	1) We will look up into database and find all direct relation with the person
	2) We can also extend the logic by searching siblings' parents relation(if exist)
	and then assign that result of parents to the existing person's parents
	(passed person_id). So get_parents and get_siblings method can be REUSED.
	"""
	response_json = {}
	person_id = request.session["person_id"]
	parents_list = get_parents(person_id)
	response_json = {"data": parents_list}
	template = "person/relation_table.html"
	return render(request, template, response_json)

def get_parents(person_id):
	"""
	Method to get all possible relation of parents of passed person's_id
	Recall we had assigned int value 7=Son, 8=Daughter, 1=Son, 2=Daughter 
	(see relationship models.py)
	"""
	parents_list = []
	avl_relation = search_saved_relations(person_id)
	if avl_relation:
		for relation in avl_relation:
			x = []
			if int(relation[2]) == 1:
				x.append(relation[0])
				x.append(relation[1])
				x.append("Father")
				x.append(relation[3])
				x.append(relation[4])
			elif int(relation[2]) == 2:
				x.append(relation[0])
				x.append(relation[1])
				x.append("Mother")
				x.append(relation[3])
				x.append(relation[4])
			else:
				pass
			if len(x) > 0:
				parents_list.append(x)
	more_relation = search_saved_relations_reverse(person_id)
	if more_relation:
		for relation in more_relation:
			x = []
			if int(relation[2]) == 7:
				x.append(relation[0])
				x.append(relation[1])
				x.append("Son")
				x.append(relation[3])
				x.append(relation[4])
			elif int(relation[2]) == 8:
				x.append(relation[0])
				x.append(relation[1])
				x.append("Daughter")
				x.append(relation[3])
				x.append(relation[4])
			else:
				pass
			if len(x) > 0 and x not in parents_list:
				parents_list.append(x)
	return parents_list

def search_saved_relations(person_id):
	"""
	This generic method can be used to get all stored relations in database of 
	given person_id
	"""
	relation_objects = Relationship.objects.filter(person__num__exact=person_id)
	relationships = []
	for obj in relation_objects:
		relation = (obj.person.num, obj.person.first_name, obj.relation,
					obj.related_person.first_name, obj.related_person.num)
		relationships.append(relation)
	return relationships

def search_saved_relations_reverse(person_id):
	"""
	This generic method can be used to get all stored relations in database of 
	given related_person's person_id
	"""
	relation_objects = Relationship.objects.filter(related_person__num__exact=person_id)
	relationships = []
	for obj in relation_objects:
		relation = (obj.person.num, obj.person.first_name, obj.relation,
					obj.related_person.first_name, obj.related_person.num)
		relationships.append(relation)
	return relationships

def display_siblings(request):
	"""
	Method to display siblings of passed person_id of family member.
	1) We will look up into database and find all direct relation with the person
	2) We can also extend the logic by searching siblings' parents relation(if exist)
	and then find children of above result parents. Atlast their children will be
	siblings of person_id. Some methods can be REUSED here.
	"""
	response_json = {}
	person_id = request.session["person_id"]
	# get the direct relation with person_id
	if person_id:
		siblings_list = get_silbings(person_id)
	else:
		msg = "Kindly select the person name from the List!!!"
	response_json = {"data": siblings_list}
	template = "person/relation_table.html"
	return render(request, template, response_json)

def get_silbings(person_id):
	"""
	Method to get all possible relation of siblings of passed person's_id
	Recall we had assigned int value 5=Brother, 6=Sister
	(see relationship models.py)
	"""
	siblings_list = []
	avl_relation = search_saved_relations(person_id)
	if avl_relation:
		for relation in avl_relation:
			x = []
			if int(relation[2]) == 5:
				x.append(relation[0])
				x.append(relation[1])
				x.append("Brother")
				x.append(relation[3])
				x.append(relation[4])
			elif int(relation[2]) == 6:
				x.append(relation[0])
				x.append(relation[1])
				x.append("Sister")
				x.append(relation[3])
				x.append(relation[4])
			else:
				pass
			if len(x) > 0:
				siblings_list.append(x)
	more_relation = search_saved_relations_reverse(person_id)
	if more_relation:
		for relation in more_relation:
			x = []
			if int(relation[2]) == 5:
				x.append(relation[0])
				x.append(relation[1])
				x.append("Brother")
				x.append(relation[3])
				x.append(relation[4])
			elif int(relation[2]) == 6:
				x.append(relation[0])
				x.append(relation[1])
				x.append("Sister")
				x.append(relation[3])
				x.append(relation[4])
			else:
				pass
			if len(x) > 0 and x not in siblings_list:
				siblings_list.append(x)
	return siblings_list

def display_children(request):
	"""
	Method to display children of passed person_id of family member.
	1) We will look up into database and find all direct relation with the 
	person.
	2) We can also extend the logic by searching siblings' of a children. So
	resulted siblings will be children of searched parents. Some methods can 
	be REUSED here.
	"""
	response_json = {}
	person_id = request.session["person_id"]
	if person_id:
		children_list = get_children(person_id)
	else:
		msg = "Kindly select the person name from the List!!!"
	response_json = {"data": children_list}
	template = "person/relation_table.html"
	return render(request, template, response_json)

def get_children(person_id):
	"""
	Method to get all possible relation of children of passed person's_id
	Recall we had assigned int value 1=Father, 2=Mother, 7=Son, 8=Daughter
	(see relationship models.py)
	"""
	children_list = []
	avl_relation = search_saved_relations(person_id)	
	if avl_relation:
		for relation in avl_relation:
			x = []
			if int(relation[2]) == 7:
				x.append(relation[0])
				x.append(relation[1])
				x.append("Son")
				x.append(relation[3])
				x.append(relation[4])
			elif int(relation[2]) == 8:
				x.append(relation[0])
				x.append(relation[1])
				x.append("Daughter")
				x.append(relation[3])
				x.append(relation[4])
			else:
				pass
			if len(x) > 0:
				children_list.append(x)
	more_relation = search_saved_relations_reverse(person_id)
	if more_relation:
		for relation in more_relation:
			x = []
			if int(relation[2]) == 1:
				x.append(relation[0])
				x.append(relation[1])
				x.append("Father")
				x.append(relation[3])
				x.append(relation[4])
			elif int(relation[2]) == 2:
				x.append(relation[0])
				x.append(relation[1])
				x.append("Mother")
				x.append(relation[3])
				x.append(relation[4])
			else:
				pass
			if len(x) > 0 and x not in children_list:
				children_list.append(x)
	return children_list


def display_grandparents(request):
	"""
	Method to display children of passed person_id of family member.
	1) We will look up into database and find all direct relation with the 
	person.
	2) We can also extend the logic by searching for parents of given 
	person'id and then again look for the parents of resulted parents.
	They will be the grand parents of given person_id.
	"""

def get_grandparents(person_id):
	"""
	Method to get all possible relation of grandparents of passed person's_id
	Recall we had assigned int value 3=Grand Father, 4=Grand Mother
	(see relationship models.py)
	"""

def display_cousins(request):
	"""
	Method to display cousins of passed person_id of family member.
	1) We will look up into database and find all direct relation with the 
	person from get_cousins method.
	2) We can also extend the logic by searching for parents of given 
	person'id and then look for their siblings. Atlast children of that resulted
	parents will be cousin of given person_id.
	"""

def get_cousins(person_id):
	"""
	Method to get all possible relation of cousins of passed person's_id
	We can add relation of cousins in relationship model.
	"""
