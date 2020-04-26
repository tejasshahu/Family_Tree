## Task:Implemenent a family tree API.

The API should be capable of keeping track of people and the connecections between them. While you have full control to model the entities as you see fit you should keep the following guidelines in mind.

Details about a person and their relationships should be editable. At a minimum you should use the following traits to describe a Person:
	
	First name
	Last name
	Phone number
	Email address
	Address
	Birth date 

When thinking about relations between people the API should be able to provide the following information:

	1. For a given person list all of their siblings
	2. For a given person list all of their parents
	3. For a given person list all their children
	4. For a given person list all of their grandparents
	5. For a given person list all of their cousins

## Solution

Steps:

	1) We will create Person model to store all user information.
	2) We will create Relationship model which will have 3 columns: 
		* one person
		* Relation with other person
		* above other person
	3) There are 5 APIs in this familytree project. 3 APIs are working perfectly 
	and there is also verbally written logic in docstring of each method to 
	extend it for more better implementation.

Note: 
1. There is no UI implementation for user to enter new family members. 
For quick up and running, you can add family members from `Django admin panel`.
* Django Admin panel username:admin, password: admin (First insert data from 
admin panel then go to below link).
* http://localhost:8000/familytree/

2. `Not 100%  code coverage`: I tested on limited dataset and tried to cover 
as much scenario as I could, based on my current thought. But there are still
many possibilities which I have missed here. Comments or any Pull request will
be appreciated.

3. Code can be optimized at many places.
