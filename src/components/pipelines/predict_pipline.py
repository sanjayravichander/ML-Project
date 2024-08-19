import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        gender: str,
        race/ethnicity: str,
        parental level of education,
        lunch: str,
        test preparation course: str,
        reading score: int,
        writing score: int):

        self.gender = gender

        self.race/ethnicity = race ethnicity

        self.parental level of education = parental level of education

        self.lunch = lunch

        self.test preparation course = test preparation course

        self.reading score = reading score

        self.writing score = writing score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race/ethnicity],
                "parental_level_of_education": [self.parental level of education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test preparation course],
                "reading_score": [self.reading score],
                "writing_score": [self.writing score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
