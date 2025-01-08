import sys
import os
import pandas as pd
from source.exception import CustomException
from source.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("data_files", "model.pkl")
            preprocessor_path = os.path.join('data_files', 'preprocessor.pkl')
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, 
                 Age, 
                 Gender, 
                 Annual_Income, 
                 Marital_Status, 
                 Number_of_Dependents, 
                 Education_Level, 
                 Occupation, 
                 Health_Score, 
                 Location, 
                 Policy_Type, 
                 Previous_Claims, 
                 Credit_Score, 
                 Insurance_Duration, 
                 Customer_Feedback, 
                 Smoking_Status, 
                 Exercise_Frequency, 
                 Property_Type, 
                 Year, 
                 Day, 
                 Month_name):

        self.Age = float(Age) 
        self.Gender = Gender
        self.Annual_Income = float(Annual_Income)
        self.Marital_Status = Marital_Status
        self.Number_of_Dependents = float(Number_of_Dependents)
        self.Education_Level = Education_Level
        self.Occupation = Occupation
        self.Health_Score = float(Health_Score)
        self.Location = Location
        self.Policy_Type = Policy_Type
        self.Previous_Claims = float(Previous_Claims)
        self.Credit_Score = float(Credit_Score)
        self.Insurance_Duration = float(Insurance_Duration)
        self.Customer_Feedback = Customer_Feedback
        self.Smoking_Status = Smoking_Status
        self.Exercise_Frequency = Exercise_Frequency
        self.Property_Type = Property_Type
        self.Year = int(Year)
        self.Day = int(Day)
        self.Month_name = Month_name

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Age": [self.Age],
                "Gender": [self.Gender],
                "Annual_Income": [self.Annual_Income],
                "Marital_Status": [self.Marital_Status],
                "Number_of_Dependents": [self.Number_of_Dependents],
                "Education_Level": [self.Education_Level],
                "Occupation": [self.Occupation],
                "Health_Score": [self.Health_Score],
                "Location": [self.Location],
                "Policy_Type": [self.Policy_Type],
                "Previous_Claims": [self.Previous_Claims],
                "Credit_Score": [self.Credit_Score],
                "Insurance_Duration": [self.Insurance_Duration],
                "Customer_Feedback": [self.Customer_Feedback],
                "Smoking_Status": [self.Smoking_Status],
                "Exercise_Frequency": [self.Exercise_Frequency],
                "Property_Type": [self.Property_Type],
                "Year": [self.Year],
                "Day": [self.Day],
                "Month_name": [self.Month_name]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)