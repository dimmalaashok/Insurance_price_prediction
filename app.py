from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from source.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

@app.route('/')
def index():
    return render_template('interface.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('inputs.html')
    else:
        data = CustomData(
                    Age=float(request.form.get('Age')),
                    Gender=request.form.get('Gender'),
                    Annual_Income=float(request.form.get('Annual_Income')),
                    Marital_Status=request.form.get('Marital_Status'),
                    Number_of_Dependents=float(request.form.get('Number_of_Dependents')),
                    Education_Level=request.form.get('Education_Level'),
                    Occupation=request.form.get('Occupation'),
                    Health_Score=float(request.form.get('Health_Score')),
                    Location=request.form.get('Location'),
                    Policy_Type=request.form.get('Policy_Type'),
                    Previous_Claims=float(request.form.get('Previous_Claims')),
                    Credit_Score=float(request.form.get('Credit_Score')),
                    Insurance_Duration=float(request.form.get('Insurance_Duration')),
                    Customer_Feedback=request.form.get('Customer_Feedback'),
                    Smoking_Status=request.form.get('Smoking_Status'),
                    Exercise_Frequency=request.form.get('Exercise_Frequency'),
                    Property_Type=request.form.get('Property_Type'),
                    Year=int(request.form.get('Year')) if request.form.get("Year") else 2023,
                    Day=int(request.form.get('Day')) if request.form.get("Day") else 6,
                    Month_name=request.form.get('Month_name') if request.form.get("Month_name") else "May"
                )

    pred_df = data.get_data_as_data_frame()
    print("pred_df:\n", pred_df)

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    print("Prediction result:", results[0])

    return render_template('inputs.html', results=results[0])

        
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)