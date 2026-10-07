# AI-Assisted Box Selection System

## Project Overview

This project is a Django REST Framework based API for managing products, boxes, and orders, and recommending a suitable box for an order.

The system provides APIs to:

* Create and list products
* Create and list boxes
* Create and list orders
* Recommend a suitable box for a specific order
* Handle invalid requests and missing orders with appropriate HTTP status codes

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite
* REST API
* Git
* GitHub

## Project Structure

```text
project/
│
├── manage.py
├── requirements.txt
├── README.md
├── AI_USAGE.md
├── TEST_OUTPUT.md
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── app/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── services.py
    ├── urls.py
    ├── admin.py
    └── tests.py
```

## Data Models

### Product

The `Product` model stores product information.

Fields:

* `name`
* `length`
* `width`
* `height`
* `weight`

### Box

The `Box` model stores available box information.

Fields:

* `name`
* `length`
* `width`
* `height`
* `max_weight`
* `cost`

### Order

The `Order` model stores order information.

Fields:

* `created_at`

### OrderItem

The `OrderItem` model connects products with orders.

Fields:

* `order`
* `product`
* `quantity`

An order can contain multiple order items.

## API Endpoints

### 1. Products

#### Get all products

```http
GET /products/
```

Returns a list of all products.

#### Create a product

```http
POST /products/
```

Example request:

```json
{
    "name": "Laptop",
    "length": 30,
    "width": 20,
    "height": 5,
    "weight": 2
}
```

Response status:

```text
201 Created
```

---

### 2. Boxes

#### Get all boxes

```http
GET /boxes/
```

Returns a list of all available boxes.

#### Create a box

```http
POST /boxes/
```

Example request:

```json
{
    "name": "Small Box",
    "length": 35,
    "width": 25,
    "height": 10,
    "max_weight": 5,
    "cost": "50.00"
}
```

Response status:

```text
201 Created
```

---

### 3. Orders

#### Get all orders

```http
GET /orders/
```

Returns a list of all orders.

#### Create an order

```http
POST /orders/
```

The request body should follow the structure defined by `OrderSerializer`.

Response status:

```text
201 Created
```

---

### 4. Box Recommendation

#### Recommend a box for an order

```http
GET /orders/<order_id>/recommend-box/
```

Example:

```http
GET /orders/1/recommend-box/
```

The API checks the specified order and uses the box recommendation service to find a suitable box.

Example successful response:

```json
{
    "order_id": 1,
    "recommended_box": {
        "id": 2,
        "name": "Medium Box",
        "dimensions": {
            "length": 40,
            "width": 30,
            "height": 15
        },
        "max_weight": 10,
        "cost": 75.0
    }
}
```

If the order does not exist:

```json
{
    "error": "Order not found"
}
```

HTTP status:

```text
404 Not Found
```

If no suitable box is available:

```json
{
    "message": "No suitable box found"
}
```

HTTP status:

```text
404 Not Found
```

## HTTP Status Codes

| Status Code | Meaning                            |
| ----------- | ---------------------------------- |
| 200         | Successful request                 |
| 201         | Resource created successfully      |
| 400         | Invalid request data               |
| 404         | Resource or suitable box not found |

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python3 -m venv myenv
```

### 3. Activate the virtual environment

For macOS/Linux:

```bash
source myenv/bin/activate
```

For Windows:

```bash
myenv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## Testing

Run the Django test suite using:

```bash
python manage.py test
```

The actual test execution output is documented in:

```text
TEST_OUTPUT.md
```

## API Testing

The APIs can be tested using tools such as Postman or the Django REST Framework browsable API.

The main endpoints are:

```text
GET/POST /products/
GET/POST /boxes/
GET/POST /orders/
GET /orders/<order_id>/recommend-box/
```

## AI Usage

Details about AI tools used during development, prompts, accepted and rejected outputs, mistakes found, and verification steps are documented in:

```text
AI_USAGE.md
```

## Chat Transcript

The original chat transcript used during development is included separately in the repository as required by the assignment.

## Learning

This section should be written by the candidate in their own words based on what they personally learned while completing the assignment.
