import pickle 
from flask import Flask , request , render_template 

# Initialize Flask App
app = Flask(__name__)

# Load the trained model
with open('sal_mod.pkl' , 'rb') as file:
    model = pickle.load(file)

# Load the another model to train
# with open('another_pickle_file.pkl' , 'rb') as myfile:
#     model = pickle.load(myfile)



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

# Route to get demo Prediction
@app.route('/predict2' , methods = ['GET'])
def predict2():
    numbericalValue1 = int(request.form['numbericVal11'])
    predictValue1 = model.predict


# Run Flask App
if __name__ == '__main__':
    app.run(debug = True) 

    