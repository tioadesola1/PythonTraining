class DiseasePredictor:
    def __init__(self, model, vectorizer, label_encoder):
        self.model = model
        self.vectorizer = vectorizer
        self.label_encoder = label_encoder


    def predict(self, text):
        if not text:
            raise ValueError("Symptom text is empty, please write the symptoms you're experiencing")

        X = self.vectorizer.transform([text])
        prediction = self.model.predict(X)
        disease = self.label_encoder.inverse_transform(prediction)
        return disease[0]