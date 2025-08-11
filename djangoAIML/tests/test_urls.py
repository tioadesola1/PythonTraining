from django.test import SimpleTestCase
from django.urls import reverse, resolve
from djangoAIML.views import hello, predict_disease

class TestUrls(SimpleTestCase):
    def test_hello(self):
        url = reverse('hello')
        print(resolve(url))
        self.assertEquals(resolve(url).func, hello)

    def test_form(self):
        url = reverse('predict_disease')
        print(resolve(url))
        self.assertEquals(resolve(url).func, predict_disease)