from django.test import TestCase,Client
from django.urls import reverse,resolve


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home-index')
        self.profile_url = reverse('profile')
    
    def test_home_view(self):
        print("test_home_view")
        response = self.client.get(self.home_url)
        print(response)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home/index.html')

    def test_profile_view(self):
        print("test_profile_view")
        response = self.client.get(self.profile_url)
        print(response)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"home/profile.html")




