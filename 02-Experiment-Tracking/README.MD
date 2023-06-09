# Experiment Tracking

&nbsp;&nbsp;&nbsp;&nbsp;Experiment tracking is the process of keeping track of all the **relevant information** from an **ML experiment**, which includes:

1. Source code
2. Environment
3. Data
4. Model
5. Hyperparameter
6. Metrics, and so on

## Why is experiment tracking is important?

1. Reproducibility: because we are a data scientist or ML engineer, we do a lot of experiment that are reproducible 
2. Organizations: If we have an organization then it will make it easier to people in your organization to track your experiments and understand more about what you do and what you've done.
3. Optimization: because of the experiment tracking we know the result and the hyperparameter of our model, we can also visualize it then we can considered to optimize the model for better performance

# MLFLOW

&nbsp;&nbsp;&nbsp;&nbsp;First thing that you can do before implement all of these processed is to run requirements.txt with ```pip install -r requirements.txt``` And to run MLFlow UI you need to write this to your command:
``` mlflow ui --backend-store-uri sqlite:///<name_of_db>.db``` 
you can change the ```<name_of_db>`` with your db name that you want