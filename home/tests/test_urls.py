from django.test import SimpleTestCase
from django.urls import reverse,resolve
from home.views import (
    home,profile
)


class TestUrls(SimpleTestCase):
    def test_home_index_url_is_resolved(self):
        print('test_home_index_url')
        url = reverse('home-index') # localhost/
        # print("url = ",url) #url for home-index 
        # print(home) #home function from views 
        print(resolve(url))
        # print('-'*20)
        self.assertEqual(resolve(url).func,home)
    
    def test_profile_url_is_resolved(self):
        print('test_profile_url')
        url = reverse('profile')
        # print("url = ",url)
        print(resolve(url))
        # print('-'*20)
        self.assertEqual(resolve(url).func,profile)
    

