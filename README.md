# Student Course API

A beginner-friendly REST API built with Python and Flask.

## Features

- API health check
- Retrieve all courses
- Retrieve a specific course
- Return a 404 response for a course that does not exist

## Technologies

- Python
- Flask
- Flask-CORS
- Gunicorn

## Run Locally

Install dependencies:

pip install -r requirements.txt

Start the API:

python app.py

## API Endpoints

GET /api/health

GET /api/courses

GET /api/courses/1

GET /api/courses/9999
