from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

courses = [
    {
        "id": 1,
        "code": "IT 101",
        "name": "Introduction to Computing",
        "description": "Fundamentals of computers and information technology."
    },
    {
        "id": 2,
        "code": "IT 205",
        "name": "Systems Integration and Architecture",
        "description": "Fundamentals of integrating software systems."
    },
    {
        "id": 3,
        "code": "CS 210",
        "name": "Data Structures and Algorithms",
        "description": "Study of data organization and problem-solving algorithms."
    },
    {
        "id": 4,
        "code": "IT 230",
        "name": "Database Management Systems",
        "description": "Introduction to database design and management."
    },
    {
        "id": 5,
        "code": "NET 240",
        "name": "Networking and Cloud Fundamentals",
        "description": "Fundamentals of computer networks and cloud computing."
    }
]

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "message": "The API is running.",
        "service": "Student Course API",
        "version": "1.0.0"
    })

@app.route("/api/courses", methods=["GET"])
def get_courses():
    return jsonify(courses)

@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            return jsonify(course)

    return jsonify({
        "error": "Not Found",
        "message": f"No course exists with id {course_id}.",
        "available_ids": [course["id"] for course in courses]
    }), 404

if __name__ == "__main__":
    app.run(debug=True)
