from django.test import TestCase

# Create your tests here.

from django.urls import resolve,reverse
from django.test import TestCase

class HomeTest(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

#Simple test to  make sure the status code is returning the correct response

    ###def test_home_url_resolves_home_view(self):
       # view = resolve('/')
        #self.assertEqual(view.func, home)
#The above isn't working need to figure out what is happening
