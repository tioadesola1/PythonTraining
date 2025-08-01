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
    print(f"Method received: {request.method}")
    if request.method == 'POST':
        text = request.POST.get('text')
        if not text:
            return JsonResponse({'error': 'No symptom text provided'}, status=400)

        X = vectorizer.transform([text])
        prediction = model.predict(X)
        disease = label_encoder.inverse_transform(prediction)

        return render(request, 'symptoms_form.html', {'prediction': disease[0], 'text': text})
    else:
        print("Loaded model:", type(model))
        print(f"Loading model from: {model}")
        return render(request, 'symptoms_form.html')
