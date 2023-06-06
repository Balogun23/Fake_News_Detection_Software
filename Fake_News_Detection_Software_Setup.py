# project_folder/
# ├── app.py
# ├── model/
# # │   └── model.pkl
# └── templates/
#     └── index.html
from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('/Users/macbook/Desktop/50%fake_news_classifier_model.pkl')

@app.route('/')
def index():
    return render_template('Project2.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json['text']
        # Perform preprocessing and make predictions
        prediction = model.predict([data])
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
