from django.test import SimpleTestCase

from djangoAIML.forms import SymptomForm


class TestForms(SimpleTestCase):
    def test_symptoms_form_valid_data(self):
        form = SymptomForm(data = {
        'text': 'I have a headache and a sore throat'
        })
        self.assertTrue(form.is_valid())

    def test_symptoms_form_empty_text(self):
        form = SymptomForm(data={'text': ''})
        self.assertFalse(form.is_valid())
