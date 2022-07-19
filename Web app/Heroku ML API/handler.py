import os
import pandas as pd
import pickle
from flask import Flask, request, Response
from Diabetes_pred.Diabetes_pred_v1 import Diabetes_pred_v1


#Loading model
model = pickle.load(open('model/Diabetes_predictor.pkl', 'rb'))


app = Flask(__name__)
@app.route('/diabetes/diabetes_predict', methods=['POST'])
def diabetes_predict():
    test_json = request.get_json()
    
    if test_json:#there is data
        if isinstance(test_json, dict):
            test_raw = pd.DataFrame(test_json, index=[0]) #funciona apenas se unica linha
        else:
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys()) #funciona para várias linhas
        
    else:
        return Response('{}', status=200, mimetype='application/json')
    
    #Instantiate Diabetes_pred_v1 class
    pipeline = Diabetes_pred_v1()
    

    #Data preparation
    df1 = pipeline.data_preparation(test_raw)
    
    #Predict
    df_response = pipeline.get_prediction(model, test_raw, df1)


    return df_response#.to_json()

    
if __name__ == '__main__':
    port = os.environ.get('PORT',5000)
    app.run(host='0.0.0.0', port= port)
