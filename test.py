import unittest
import requests

class TestStudentDetailsAPI(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/"
        self.student_data = {
            "name": "Foo",
            "email": "foo@example.com",
            "age": 20,
            "phone": 1234567890
        }

    def test_post_studentdetails(self):
        response = requests.post(self.url + '/AddStudent', json=self.student_data)

        # Check if the request was successful
        self.assertEqual(response.status_code, 200)

        # Check the response content if necessary
        response_data = response.json()
        print(response_data)

    def test_get_studentdetails(self):
        response = requests.get(self.url + 'GetAllStudents')

        # Check if the request was successful
        self.assertEqual(response.status_code, 200)

        # Check the response content if necessary
        response_data = response.json()
        print(response_data)



if __name__ == "__main__":
    unittest.main()
