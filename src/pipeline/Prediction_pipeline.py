import os , sys
import numpy as np
import pandas as pd
from dataclasses import dataclass
from src.utilities import *
from src.exception import CustomException
from src.logger import logging
from src.constants import *

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self , feature_values):

        preprocessor_path = os.path.join(
            
            CURRENT_DIR_KEY,
            ARTIFACT_DIR ,
            ARTIFACT_DIR_KEY2 ,
            "preprocessor.pkl"
    )
        model_path = os.path.join(
            
            CURRENT_DIR_KEY,
            ARTIFACT_DIR ,
            ARTIFACT_DIR_KEY3 ,
            "model_trainer.pkl"
    
    )
        
        preprocessor = load_object(preprocessor_path)
        model = load_object(model_path)

        scaled_feature_values = preprocessor.transform(feature_values)
        predicted_value = model.predict(scaled_feature_values)

        return predicted_value
    
class CustomClass:
    def __init__(self, 
                  age:int,
                  workclass:int, 
                  education_num:int, 
                  marital_status:int, 
                  occupation:int,
                  relationship:int,  
                  race:int,
                  sex:int,  
                  capital_gain:int, 
                  capital_loss:int,
                  hours_per_week:int, 
                  native_country:int):
        self.age = age
        self.workclass = workclass
        self.education_num = education_num
        self.marital_status = marital_status
        self.occupation = occupation
        self.relationship = relationship
        self.race = race
        self.sex = sex
        self.capital_gain = capital_gain
        self.capital_loss = capital_loss
        self.hours_per_week = hours_per_week
        self.native_country = native_country


    def get_data_DataFrame(self):
        try:
            custom_input = {
                "age": [self.age],
                "workclass": [self.workclass],
                "education_num":[self.education_num],
                "marital_status":[self.marital_status],
                "occupation":[self.occupation],
                "relationship":[self.relationship],
                "race":[self.race],
                "sex":[self.sex],
                "capital_gain":[self.capital_gain],
                "capital_loss":[self.capital_loss],
                "hours_per_week":[self.hours_per_week],
                "native_country":[self.native_country]

            }

            data= pd.DataFrame(custom_input)
            return data
        
        except Exception as e:
           raise CustomException(e , sys)

            
        
