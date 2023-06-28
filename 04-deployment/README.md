# Deployment

&nbsp;&nbsp;&nbsp;&nbsp;Model Deployment has a multiple options (if we want to have a prediction immediately or want to wait a little bit (hour, day, week)):

## Batch [Offline]

This option, the model won't running all the time and just apply our model to new data regularly. The way it look like is: 
```
1. Suppose we have a database
2. Then we have name as "Scoring Job" that contains of our model. Then if the scheduler running daily this scoring job will get the model of prediction with yesterday data
3. Then we write the result to some other database that contains of the prediction's results
4. Then something can read from this database and react on this prediction (i.e. report)
```

## Online 
&nbsp;&nbsp;&nbsp;&nbsp;this option will up and running model all the time, if we need predictions as soon as possible this can be an option. Then if using this online deployment, there are two variants:
     
### Web Service: 

&nbsp;&nbsp;&nbsp;&nbsp;This variant, the model is available through a web service, we can send http requests, we get back the predictions from this service. This variant is 1-on-1 client-server (because will predict for one user/server) and this user flow simply like this:
```
1. User want to know the prediction of something on app
2. Then it will request to the backend
3. Backend will predict user request from model
4. The result of the prediction will be returned to the backend
5. Then the backend will send back to the user
```

### Streaming
&nbsp;&nbsp;&nbsp;&nbsp;This option is when there is a stream of events model services listening for events on the stream and react to this. This streaming is like 1-N (one to many) because 1 producer will send to multiple customers or N-N (many to many). The flow is like this:
```
1. There are a PRODUCER and pushes some event to an event stream
2. Then customers would read from this stream
3. Then customers will react to these events and
4. Do something with this
```