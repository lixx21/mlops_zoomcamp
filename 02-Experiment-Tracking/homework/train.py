import os
import pickle
import click

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

import mlflow

#set tracking db
mlflow.set_tracking_uri("sqlite:///mlflow.db")
#set the experiment
mlflow.set_experiment("homework-mlops-experiment")

def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
def run_train(data_path: str):

    with mlflow.start_run():
        mlflow.set_tag("Developer", "Felix")
        mlflow.log_param("train-data-path", "./homework/green_tripdata_2022-01.parquet")
        mlflow.log_param("val-data-path", "./homework/green_tripdata_2022-02.parquet")
        
        X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
        X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))

        max_depth = 10
        random_state =0
        
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("random_state", random_state)
        
        rf = RandomForestRegressor(max_depth=max_depth, random_state=random_state)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_val)

        rmse = mean_squared_error(y_val, y_pred, squared=False)
        mlflow.log_metric("rmse", rmse)


if __name__ == '__main__':

    run_train()
