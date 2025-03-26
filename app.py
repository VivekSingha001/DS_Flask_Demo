import pickle 
from flask import Flask , request , render_template 

# Initialize Flask App
app = Flask(__name__)

# Load the trained model
with open('sal_mod.pkl' , 'rb') as file:
    model = pickle.load(file)





# Route for Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route to Get Prediction
@app.route('/predict' , methods = ['POST'])
def predict():
    experience = float(request.form['experience'])
    prediction = model.predict([[experience]])[0]
    return render_template('index.html' , prediction_text = f'Predicted Salary: ${prediction:.2f}') 




# Run Flask App
if __name__ == '__main__':
    app.run(debug = True) 

    