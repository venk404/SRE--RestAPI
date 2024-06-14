Project Name (Replace with your project's name)

Description

This FastAPI application provides a RESTful API for managing student data. It allows you to:

Create new student entries
Retrieve all student records
Get a specific student by ID
Update existing student information
Delete student records
Features

Built with FastAPI for efficient and performant API development
Utilizes Pydantic for robust data validation and modeling
Employs exception handling (HTTPExceptions) for error management
Separates API endpoints into versions for potential future changes
Local Setup

Prerequisites:

Python 3.11
pip (package manager)
Installation:

Clone this repository: git clone https://your-github-repo-url.git
Navigate to the project directory: cd your-project-name
Create a virtual environment (recommended for isolation): python -m venv venv
Activate the virtual environment:
For Linux/macOS: source venv/bin/activate
For Windows: venv\Scripts\activate.bat
Install dependencies: pip install -r requirements.txt
Configuration (Optional):

If your Models.py file or database connection details require modification, update the values accordingly.
Run the API:

uvicorn main:app --host 0.0.0.0 --port 8000 (Modify host and port if needed)
Access the API endpoints at http://localhost:8000/ or http://your-server-ip:8000/ (replace with your actual host/port)
API Endpoints

Version 1 (Default):

/AddStudent (POST): Creates a new student entry. Provide a JSON payload with the student's details (name, email, age, phone).
/GetAllStudents (GET): Retrieves all student records.
/GetStudent (GET): Fetches a specific student by ID. Provide the student ID as a path parameter.
Version 2 (Prefix: /v2):

/UpdateStudent (PATCH): Updates existing student information. Provide the student ID as a path parameter and a JSON payload with the updated fields.
/DeleteStudent (DELETE): Deletes a student record. Provide the student ID as a path parameter.
Example Usage (Using Postman or curl):

Create a Student (v1):

Bash
POST http://localhost:8000/AddStudent

Content-Type: application/json

{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "age": 25
}
Use code with caution.
content_copy
Response:

JSON
{
  "message": "Student data added",
  "student_id": 123  // (Example student ID)
}
Use code with caution.
content_copy
Get All Students (v1):

Bash
GET http://localhost:8000/GetAllStudents
Use code with caution.
content_copy
Response:

JSON
{
  "students": [
    {
      "id": 123,  // (Example ID)
      "name": "John Doe",
      "email": "john.doe@example.com",
      "age": 25
    },
    // ... (Other student records)
  ]
}
Use code with caution.
content_copy
Update a Student (v2):

Bash
PATCH http://localhost:8000/v2/UpdateStudent/123  // Replace 123 with actual student ID

Content-Type: application/json

{
  "name": "Jane Doe"  // Update only the name
}
Use code with caution.
content_copy
Response:

JSON
{
  "students": {
    "id": 123,
    "name": "Jane Doe",
    "email": "john.doe@example.com",  // Email remains unchanged
    "age": 25
  }
}
Use code with caution.
content_copy
Additional Notes

Error handling is implemented using HTTPExceptions to provide informative error messages to the client.
You may need to adjust the provided examples and API usage instructions depending on your specific database configuration and data models.
