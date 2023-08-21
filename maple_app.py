from flask import Flask, render_template,request
from sklearn import *
from flask import *  
import numpy as np
app = Flask(__name__)
import pickle
import joblib
model = pickle.load(open("model1.pkl",'rb'))
@app.route('/')
def home():
   return render_template('first_page.html')
@app.route('/form')
def form():
  return render_template('form_page.html')
@app.route('/eda')
def eda():
  return render_template('eda_page.html')
@app.route('/guest', methods = ["POST"])
def Guest():
   a = request.form['a']
   b = request.form['b']
   c = request.form['c']
   d = request.form['d']
   e = request.form['e']
   f = request.form['f']
   g = request.form['g']
   data = [[int(a),int(b),int(c),int(d),int(e),int(f),int(g)]]
   #data = scaler.fit_transform(data)
   prediction = model.predict(data) 
   #pred = scaler.inverse_transform(prediction)
   
   session['output'] = 'The predicted average price is {} US dollars'.format(round(prediction[0][0]),4)
   
   return predict()

@app.route('/predict')
def predict():
    return render_template('predict_page.html', prediction_text='{}'.format(session['output']))
if __name__ == '__main__':
   app.config['SECRET_KEY'] = 'some random string'
   app.secret_key = 'super secret key'
   app.run(debug = True)