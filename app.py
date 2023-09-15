from flask import Flask, render_template , request
import numpy as np
import joblib


model = joblib.load('Model.pkl')

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        ph=float(request.form['PH Level'])
        hardness= float(request.form['Hardness'])
        solids=float(request.form['Solids'])
        chloramines=float(request.form['Chloramines'])
        sulfate=float(request.form['Sulfate'])
        conductivity=float(request.form['Conductivity'])
        organic_carbon=float(request.form['Organic_carbon'])
        trihalomethanes=float(request.form['Trihalomethanes'])
        turbidity=float(request.form['Turbidity'])

        new_arr=np.array([[ph,hardness,solids,chloramines,sulfate,conductivity,organic_carbon,trihalomethanes,turbidity]])
        new_output = model.predict(new_arr)

        if(new_output[0]==1):
            predicted_result="Water is SAFE to drink !!!"
        else:
            predicted_result="Water is UNSAFE to drink !!!" 
        return render_template('home.html',predicted_result= predicted_result)

    except KeyError as e:
        # Handle missing form fields gracefully
        return "Missing form field: " + str(e), 400
          

if __name__ == "__main__":
    app.run(port=5000, debug=True)