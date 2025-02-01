# Django Language API

This project is a Django application that provides an API for handling FAQs in multiple languages (Hindi and Bengali). The API supports CRUD operations for FAQs and allows filtering based on the language (Hindi or Bengali).

## Features

- CRUD functionality for managing FAQs.
- Automatic translation of questions into Hindi and Bengali using Google Translate.
- Filter FAQs based on the language (Hindi or Bengali).
- Use of Django REST Framework to expose the API.

## Requirements

- Python 3.x
- Django 3.x or higher
- Django REST Framework
- `googletrans` library (for translations)
- `ckeditor` (for rich text fields in answers)

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/PiyushVedwal7/lang_api.git
cd lang_api


Step 2: Run the development server

python manage.py runserver
The API will be accessible at http://localhost:8000/api/faqs/.

API Endpoints
GET /api/faqs/
Fetch all FAQs.

Query Parameters
language: Optional. Filters FAQs by language. Accepts values hi (Hindi) or bn (Bengali).
Example:


http://localhost:8000/api/faqs/?language=hi
Returns only FAQs with Hindi translations.

POST /api/faqs/
{
  "question": "What is your favorite color?",
  "answer": "My favorite color is blue."
}
The system will automatically translate the question into Hindi and Bengali.

GET /api/faqs/{id}/
Fetch a specific FAQ by its ID.

PUT /api/faqs/{id}/
Update a specific FAQ by its ID.

DELETE /api/faqs/{id}/
Delete a specific FAQ by its ID.
