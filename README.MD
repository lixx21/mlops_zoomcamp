# MLOps Zoomcamp from datatalks

All Homework Data: [NYC TRIP DATA](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

## [01-Intro](/01-Intro/)

&nbsp;&nbsp;&nbsp;&nbsp;In this module I learned about what is MLOps and the maturity of MLOps. Not just that in this module I also learned about how to setup the environment for our machine (linux).

## [02-Experiment-Tracking](/02-Experiment-Tracking/)

&nbsp;&nbsp;&nbsp;&nbsp;In this module I learned about how to track our experiment as a data scientist and machine learning engineer. Sometimes as a data scientist we do many of experiments before we get the best model, and we need to tracking those environments, therefore we use ```mlflow``` or ```weight and biases``` to help us tracking our environment an analyzed our experiment (accuracy, RMSE, parameters and so on)

## [03-Orchestation](/03-Orchestration/)

```data``` ```.prefectignore``` ```deployment.yaml``` ```mlflow.db``` ```prefect.yaml``` are the dapendencies for prefect deployment using Github, because when we want to deploy Prefect using data, prefect will see the directory from root directory of github. That is why I put all dependencies in main root directory of my github