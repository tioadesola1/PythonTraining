from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.hello_url = reverse('hello')
        self.predict_url = reverse('predict_disease')

    def test_hello_GET(self):
        response = self.client.get(self.hello_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hello.html')

    def test_predict_disease_GET(self):
        response = self.client.get(self.predict_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'symptoms_form.html')

    def test_predict_disease_POST_success(self):
        response = self.client.post(self.predict_url, {
            'text': 'I have a headache and sore throat'
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'symptoms_form.html')

    def test_predict_disease_POST_no_text(self):
        response = self.client.post(self.predict_url)
        self.assertEquals(response.status_code, 400)