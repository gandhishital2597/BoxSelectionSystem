 AI Usage

1.AI Tools Used :OpenAI ChatGPT

 AI-assisted development tool while working on this assignment.

The AI was used mainly for:

* Understanding the assignment requirements.
* Planning the Django project structure.
* Understanding Django models and relationships.
* Creating initial Django REST Framework API examples.
* Developing the box selection algorithm.
* Understanding product dimensions, weight, box capacity, and cost-based selection.
* Identifying possible edge cases.
* Getting help with debugging and improving the implementation.
* Preparing test cases and interview/project documentation.



2.Prompts Used  : Some of the main prompts I used were:
AI-Assisted Box Selection System. We operate an ecommerce platform. When a customer places an order, the warehouse team needs to know which shipping box should be used. Each product has dimensions and weight. Each box has internal dimensions, maximum weight capacity, and cost. Design and build a small Django-based system that recommends the most suitable box for an order."
Complete Django Implementation
"explain this task how to implement so start with Django project to Django REST Framework."

Box Selection Logic
"How should the system select the most suitable box based on product dimensions, weight and cost?"

API Development
"Create Django REST Framework APIs for products, boxes, orders and box recommendation."

Testing
"Give me test cases for the box selection algorithm."


3.Output Accepted

I accepted and adapted AI-generated suggestions for:

Django project and app structure.
Product, Box, Order and OrderItem models.
Django REST Framework serializers.
APIView-based REST APIs.
URL configuration.
Basic serializer validation.
Box recommendation service structure.
Product rotation/orientation checking.
Unit test examples.
Project documentation structure.

For example, the AI suggested separating the business logic into a `services.py` file instead of placing all the recommendation logic directly inside `views.py`.

I accepted this approach because it keeps the API layer and business logic separate and makes the code easier to test and maintain.



4.Output Rejected or Modified

I did not blindly use all AI-generated code.

I reviewed and modified the suggestions based on the actual requirements of the assignment.

Examples of modifications include:

Adjusting model fields and relationships to match the assignment.
Modifying API URLs and response formats.
Adding validation for dimensions, weight and box cost.
Adding test cases for products that can and cannot fit into boxes.
Reviewing the box recommendation algorithm instead of treating the AI-generated implementation as a complete 3D packing solution.
Adjusting code where necessary to match the Django and Django REST Framework version used in the project.

The AI suggested a simplified packing approach based on volume, weight and individual product dimensions. I recognized that this does not completely solve the mathematical 3D bin-packing problem when multiple products must physically fit together in one box.

Therefore, I treated this as a simplified recommendation algorithm rather than claiming that it was a perfect 3D packing algorithm.

6. Mistakes or Limitations Identified

One important limitation identified during the AI-assisted development was the box-packing algorithm.

The simplified algorithm checks:
1.Total product weight.
2.Total product volume.
3.Whether individual products can fit inside the box.
4.Different orientations of individual products.
5.Cost of suitable boxes.

However, these checks alone do not guarantee that multiple products can physically be arranged together inside the same box.

For example, two products might each individually fit inside a box but may not fit together because of their combined spatial arrangement.

Therefore, the implementation should be considered a **simplified box recommendation algorithm**, not a complete 3D bin-packing solver.

Another important consideration was that AI-generated code can contain assumptions that do not exactly match the project's requirements. I therefore reviewed the generated code rather than copying it without verification.




I verified the final implementation by:
python manage.py check
to check for Django configuration and project errors
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


and verifying that the Django application starts successfully.

Django Admin  : I created sample products, boxes, orders and order items through the Django Admin interface.

API Testing  : I tested the REST APIs using Postman, including:


GET /api/products/
POST /api/products/

GET /api/boxes/
POST /api/boxes/

GET /api/orders/
POST /api/orders/

GET /api/orders/<id>/recommend-box/


Algorithm Testing

I tested scenarios such as:

A product fitting inside a box. 
A product not fitting because of its dimensions.
Product weight exceeding box capacity.
Different product orientations.
Multiple products in an order.
Multiple suitable boxes where the lower-cost box should be selected.
No suitable box being available.



I also used Django's test framework to test the box-fitting logic:


python manage.py test


The final code was reviewed and tested before being considered for submission.
