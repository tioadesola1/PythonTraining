from django.shortcuts import render
from django.http import JsonResponse
from djangoAIML.machinelearning.utils.paths import ML_DIR
from djangoAIML.machinelearning.predictor import DiseasePredictor
from djangoAIML.forms import SymptomForm
import joblib
import os

def hello(request):
    return render(request,"hello.html", {'name' : 'Tio'})

def input_form(request):
    return render(request, 'symptoms_form.html')

model = joblib.load(os.path.join(ML_DIR, 'model.pkl'))
vectorizer = joblib.load(os.path.join(ML_DIR, 'vectorizer.pkl'))
label_encoder = joblib.load(os.path.join(ML_DIR, 'label_encoder.pkl'))

predictor = DiseasePredictor(model, vectorizer, label_encoder)

def predict_disease(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if not text:
            return JsonResponse({'error': 'No symptom text provided'}, status=400)
        disease = predictor.predict(text)
        return render(request, 'symptoms_form.html', {'prediction': disease, 'text': text})
    else:
        return render(request, 'symptoms_form.html')
