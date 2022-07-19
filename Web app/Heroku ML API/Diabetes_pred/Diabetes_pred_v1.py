import pickle
import numpy as np
import pandas as pd


class Diabetes_pred_v1( object ):
    def __init__( self ):
        self.home_path = ''
        self.sc = pickle.load(open(self.home_path + 'parameter/sc.pkl', 'rb' ))
     
    def data_preparation(self, test_raw):
        ## 5.30 Stardalization
        df1 = test_raw
        df1 = self.sc.transform(df1)
        
        return df1
    
    def get_prediction( self, model, test_raw, df1 ):
        # prediction
        test_raw['pred'] = model.predict( df1 )
        test_raw['probabilidade'] = model.predict_proba( df1 )[:,1]

        
        return test_raw.to_json(orient='records')
