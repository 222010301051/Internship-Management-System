from django.test import TestCase
from django.urls import reverse

class DummyTestCase(TestCase):
    def test_main_dashboard(self):
        response = self.client.get(reverse('main_dashboard'))
        self.assertEqual(response.status_code, 200)  # Simulating a pass

    def test_student_login(self):
        response = self.client.post(reverse('Student_Login'), {'email': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)  # Simulating a pass
        self.assertContains(response, "Invalid email or password")  # Simulating a failure

    def test_faculty_login(self):
        response = self.client.post(reverse('faculty_login'), {'email': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)  # Simulating a pass
        self.assertContains(response, "Invalid email or password")  # Simulating a failure

    # Add more test cases for other views if needed
