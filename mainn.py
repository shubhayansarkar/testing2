from flask import Flask, render_template, request

import requests
import pickle

import sklearn

app = Flask(__name__)
model = pickle.load(open('testingss.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        x1 = float(request.form['x1'])
        x2 = float(request.form['x2'])
        prediction=model.predict([[x1,x2]])
        output=round(prediction[0],2)
        return render_template('index.html',prediction_text="result is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)