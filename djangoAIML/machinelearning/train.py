from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from djangoAIML.machinelearning.utils.paths import BASE_DIR

import pandas as pd
import joblib
import os

# Load dataset
dataset = pd.read_csv('Symptom2Disease.csv')

# Clean missing values
dataset.dropna(subset=['text', 'label'], inplace=True)

# Encode labels (diseases)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(dataset['label'])

# Vectorize symptom descriptions using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(dataset['text'])

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train classifier
prediction_model = RandomForestClassifier()
prediction_model.fit(X_train, y_train)

# Evaluate
y_pred = prediction_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Save model and encoders
joblib.dump(BASE_DIR, os.path.join(BASE_DIR, 'model.pkl'))
joblib.dump(vectorizer, os.path.join(BASE_DIR, 'vectorizer.pkl'))
joblib.dump(label_encoder, os.path.join(BASE_DIR, 'label_encoder.pkl'))
