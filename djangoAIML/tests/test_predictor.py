from djangoAIML.machinelearning.predictor import DiseasePredictor
from unittest.mock import MagicMock
import unittest

class TestPredictor(unittest.TestCase):
    def setUp(self):
        self.mock_model = MagicMock()
        self.mock_vectorizer = MagicMock()
        self.mock_label_encoder = MagicMock()

        self.mock_model.predict.return_value = [0]
        self.mock_vectorizer.transform.return_value = 'mocked_vector'
        self.mock_label_encoder.inverse_transform.return_value = ['Flu']

        self.predictor = DiseasePredictor(
            self.mock_model,
            self.mock_vectorizer,
            self.mock_label_encoder
        )

    def test_predict_success(self):
        result = self.predictor.predict("I have a headache")
        self.assertEquals(result, 'Flu')
        self.mock_vectorizer.transform.assert_called_once_with(["I have a headache"])
        self.mock_model.predict.assert_called_once_with('mocked_vector')

    def test_predict_empty_input(self):
        with self.assertRaises(ValueError):
            self.predictor.predict("")