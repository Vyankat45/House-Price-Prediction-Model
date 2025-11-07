from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the trained model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)  # ✅ assign to a variable

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # your HTML form page

@app.route('/predict', methods=["POST"])  # ✅ corrected spelling "methods"
def predict():
    # ✅ Extract form data safely
    try:
        features = [float(x) for x in request.form.values()]
        final_features = np.array([features])  # reshape for model
        prediction = model.predict(final_features)
        predicted_price = round(prediction[0], 2)
        
        return render_template(
            'index.html',
            prediction_text=f"🏠 Estimated House Price: ₹{predicted_price:,}"
        )
    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f"⚠️ Error: {str(e)}"
        )

if __name__ == '__main__':
    app.run(debug=True)
