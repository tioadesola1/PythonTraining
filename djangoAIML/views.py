from django.shortcuts import render
from django.http import JsonResponse
from djangoAIML.machinelearning.utils.paths import ML_DIR
import joblib
import os

def hello(request):
    return render(request,"hello.html", {'name' : 'Tio'})

def input_form(request):
    return render(request, 'symptoms_form.html')


model = joblib.load(os.path.join(ML_DIR, 'model.pkl'))
vectorizer = joblib.load(os.path.join(ML_DIR, 'vectorizer.pkl'))
label_encoder = joblib.load(os.path.join(ML_DIR, 'label_encoder.pkl'))

def predict_disease(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if not text:
            return JsonResponse({'error': 'No symptom text provided'}, status=400)

        X = vectorizer.transform([text])
        prediction = model.predict(X)
        disease = label_encoder.inverse_transform(prediction)

        return render(request, 'templates/symptoms_form.html', {'prediction': disease[0]})
    else:
        return render(request, 'templates/hello.html')
