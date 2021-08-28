#Importing the libraries
import pickle
import numpy
from flask import Flask, request , render_template


#Global Variables
app = Flask(__name__)
loadedModel = pickle.load(open('NFLX.pkl', 'rb'))



#User defined Functions
@app.route('/', methods=['GET'])
def Home():
    return render_template('NFLX.html')

@app.route('/predictions', methods= ['POST'])
def predict():
    h = float(request.form['HIGH PRICE'])
    l = float(request.form['LOW PRICE'])
    o = float(request.form['OPEN PRICE'])

    predictions= loadedModel.predict([[h,l,o]])
    print(predictions)
    
    return render_template('NFLX.html', prediction_output= predictions)





#Main function
if __name__ == "__main__":
    app.run(debug = True)