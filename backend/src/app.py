from flask import Flask, request
import pickle
import pandas as pd
import os
import sklearn
from sklearn.linear_model import LogisticRegression


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"


@app.route("/predict", methods=["POST"])
def predict():
    model_data_filename = "./data/prod/final_data.csv"
    model_filename = "./data/prod/finalized_model.sav"
    print(os.getcwd())
    df = pd.read_csv(model_data_filename)
    columns = []
    for column in df.columns:
        if column != "loan_status":
            columns.append(column)
    
    param_df = df.iloc[[1000]]

    params = param_df[columns].values
    lr = pickle.load(open(model_filename, 'rb'))
    print(type(lr))
    # print(lr.predict(params))
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)