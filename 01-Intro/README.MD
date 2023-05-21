# Introduction 

&nbsp;&nbsp;&nbsp;&nbsp;There are a process for machine learning project:

1. Design: Think if the machine learning is the right tool for solving our problems 
2. Train: Train the model and try to fing the best possible model we do a lot of different experiments here. And the result of this stage is we have model to used
3. Operate: After we got the model we will need to deploy the model so end users can use our model and in this stage we also make sure that the model is performing well

&nbsp;&nbsp;&nbsp;&nbsp;So mlops here will do all the stages to make it easier for us to retrain, deploy and monitoring the model

# Dataset

Course Data: [Green NYC GOV January - February 2021](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

Homework Data: [Yellow NYC GOV January - February 2022](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

# MLOps Maturity 

reference: [MLOps Maturity Model - Microsoft](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mlops/mlops-maturity-model#:~:text=The%20MLOps%20maturity%20model%20helps%20clarify%20the%20Development,existing%20organization%27s%20attempt%20to%20implement%20such%20an%20environment.)

&nbsp;&nbsp;&nbsp;&nbsp;Number of level in mlops

## NO MLOps: Level 0

1. No Automation
2. All code in jupyter notebook

## Devops, no MLOps: Level 1

1. Releases or deployment are automated
2. CI/CD
3. Unit & Integration Tests
4. Ops Metrics
5. But not machine learning
6. No experiment tracking
7. No reproducibility
8. DS seperated from engineers

## Automated Training: Level 2

1. Training Pipelines
2. Experiment Tracking
3. Model Registry
4. Low Friction Deployment
5. DS work with engineers

## Automated Deployment: Level 3

1. Easy to deploy model ( can just make an API call )
2. A/B Test 
3. Model Monitoring

## Full MLOps Automation: Level 4

1. Automatic Training
2. Automatic re-train
3. Automatic Deployment