import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.utils import save_object
from src.exception import CustomException
from src.logger import logging
import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl') # Saving the preprocessor object as a pickle file

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            numerical_features=['writing_score','reading_score']
            categorical_features=['gender','race_ethnicity','parental_level_of_education',
                                  'lunch','test_preparation_course']
            
            numerical_pipeline=Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())])
            logging.info("Numerical columns encodings are done")
            categorical_pipeline=Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoder',OneHotEncoder(handle_unknown='ignore'))
            ]) 
            logging.info("Categorical columns converted using one_hot")

            preprocessor=ColumnTransformer(transformers=[
                ('numerical_pipeline',numerical_pipeline,numerical_features),
                ('categorical_pipeline',categorical_pipeline,categorical_features)
            ])
            return preprocessor
            
        except Exception as e:
            raise CustomException(e, sys)   

    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("Read train and test data")

            preprocessing_obj=self.get_data_transformation_object()
            target_column_name="math_score"
            numerical_columns=['writing_score','reading_score']
            
            input_feature_train_df=train_df.drop(columns=[target_column_name], axis=1).copy()
            target_feature_train_df=train_df[target_column_name].copy()

            input_feature_test_df=test_df.drop(columns=[target_column_name], axis=1).copy()
            target_feature_test_df=test_df[target_column_name].copy()

            logging.info("Applying preprocessing object to train and test datasets.")

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)  

            train_arr=np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Returning train_array and test_array")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e, sys)