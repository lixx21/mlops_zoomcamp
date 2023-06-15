# Orchestration and ML Pipelines

&nbsp;&nbsp;&nbsp;&nbsp;Prefect is an orchestration tools for python or Machine Learning tasks especially for ML Pipelines. The reason why we used prefect is: 
1. Flexible: Prefect can be laveraged to turn python code into robust wokrflows that are more resilient to downtime and unforseen failures
2. Open-source: Prefect can be install using pip because Prefect is an open-source library. Or you can see Prefect Installation on [Prefect - Installation Docs](https://docs.prefect.io/2.10.13/getting-started/installation/)
3. Python framework to turn standard pipelines into fault-tolerant dataflows

## Self Hosting a Prefect Server

&nbsp;&nbsp;&nbsp;&nbsp;Essentially you weill be hosting the **orchestration API** which is a rest API that used by a server to work with workflow metadata. This workflow metadata is stored in **database**. A local SQL lite database is used by default and is configured upon installation. There is also a **Server UI** which is used for visualizing workflows in a centralized location. Here is the [Self Hosting a Prefect Server - Docs](https://docs.prefect.io/2.10.13/host/) that you can read.

## Prefect Terminology

&nbsp;&nbsp;&nbsp;&nbsp;There are basic building blocks of prefect: 
1. Task: You can think task as just regular python functions, they take input and perform work and then produce output 
2. Flow: Flows can also be viewed as python functions and they are responsible for serving as the container for workflow logic. Flows can be laveraged as parent functions used to call tasks and define state dependencies and data dependencies between tasks.
3. Subflow: Flow can also called other flow, not only task. when this occurs we get a subflow.

&nbsp;&nbsp;&nbsp;&nbsp; Task contain a decorator and flow also contain a decorator. These decorators are necessary when converting existing scripts into a Prefect workflow. All of the decorators can have a name argument set, this name arugument passes a descriptive name to each of the functions. this informations gets passed to Prefect and is visible in the UI when the workflows are visualized.

## Getting Started with Prefect

1. Create environment with ```conda create -n <name env> python==3.9.12``` or ```python -m virtualenv <name env>``` With python version = 3.9.12
2. Install all dependencies using ```pip install -r requirements.txt```
3. Then start Prefect using ```prefect server start```
4. When you see ```Prefect API URL```, you have to copy the url and apply to our Prefect configuration use this command: in new terminal ```prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api```. **Doing this will ensure that we send our workflow metadata to the server's UI**.
5. Run python's script that already contain with all Prefect terminologies (in this case you can test scripst in folder 3.2)
6. Click the dashboard URL to see Prefect's UI

## Deploying Workflow

&nbsp;&nbsp;&nbsp;&nbsp;We can also make a deployment that will live on a server and it will allow us to do things like **scheduling** and **colaboration** with other folks for example if you are using a Prefect cloud. The first thing that we need to do is to make sure that our project is already on github, then we can simply do:

### 1. Initialize prefect project
&nbsp;&nbsp;&nbsp;&nbsp;Type ```Prefect project init``` on command and this will going to create 4 files

1. ```.prefectignore```
2. ```deployment.yaml``` this is useful for template if you are making a multiple deployments from one project
3. ```prefect.yaml``` 
4. ```.prefect/``` 

### 2. Add @flow and other decorators in your code
&nbsp;&nbsp;&nbsp;&nbsp;Add an @flow decorator to your code entrypoint function, give it a name.

### 3. Orchestration environment
&nbsp;&nbsp;&nbsp;&nbsp;Login to Prefect cloud or Start an open source server

```prefect cloud login``` to login in cloud

```prefect server start ``` to start an open source prefect server

### 4. Execution environment
&nbsp;&nbsp;&nbsp;&nbsp;Start a worker that polls your work pool using this command:

```prefect worker start -p my-pool -t process```

### 5. Deploy your flow

```prefect deploy <your python script>:<function name where flow is decorator> -n 'my-deployment' -p my-pool```

In this case the example like this:

```prefect deploy orchestrate.py:main_flow -n taxi1 -p zoompool```

### 6. Start and run a deployment flow on CLI

```prefect deployment run Hello/my-deployment```

&nbsp;&nbsp;&nbsp;&nbsp;When this actually happens, we will have the trigger set for this deployment to actually run and it will create our flow run. We will submit that to the work pool and our worker that is on our execution environment will be polling for that work and we will pick it up and start kick it off by setting up the infrastructure that has been specified in our project steps and the the worker will start our flow run with our configuration

```
NOTE:

    if you want to deploy and you have data, please make sure that you are already push your data into github. Because if you want to deploy and prefect cannot find the data in your github, then the process will fail
```