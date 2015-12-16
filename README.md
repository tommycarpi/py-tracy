# Py-Tracy
Py-tracy evaluates the inter-arrivals times between logs applying different filters based on the user input. <br>
The logs comes from the Google's traces *clusterdata-2011-2* (available on Google Storage) for ```job_events``` and ```task_events```. <br>
Py-tracy was created furing the course of *Computer Systems Performance Evaluation* @ Politecnico of Milan. <br>
This repository contains the code used to analyse the data provided by Google.

Dependencies
===
For this project we used  <br>
[IPython](http://ipython.org) <br>
[Spark](http://spark.apache.org)  <br>
[Bokeh](http://bokeh.pydata.org/en/latest/) <br>
I wrote a tutorial on how to [link IPython with Spark](https://gist.github.com/tommycarpi/f5a67c66a8f2170e263c) on OS X and Linux. 

Usage
===
Up to now the code is available only as ```ipynb```, so you need to open the source file with IPython. <br>
The traces contain data starting from the 1st of May 2011 19 EDT until the 30th of May 2011. <br>
**Important:** many parameters may be set to filter the traces, in any case (except time parameters) you can type ```None``` and no filter will be applied. 
```python
j_eval_day(None, 2, 3600)
``` 
will evaluate traces with any ```event_type```.

Job Events 
---
Open the ```inter_arrival_jobs``` file and run all the cells till the **Usage** section. <br>
After that you can call the function to start the computation. <br>

```python
# j_eval_day(event_type, day, granularity)
j_eval_day(0, 2, 3600)
```

* ```event_type``` : the type of event, e.g. 0 correspond to SUBMIT
* ```day``` : day you wish to evaluate, e.g. 2 correspond to the 2nd of May from 0:00 until 23:59
* ```granularity``` : interval at which you want to perfom the evaluation (expressed in seconds!), e.g. 3600 will evaluate the model at intervals of 1 hour 

```python
# j_eval_days(event_type, init_day, finish_day, granularity)
j_eval_days(0, 2, 5, 3600)
```

* ```event_type``` : the type of event, e.g. 0 correspond to SUBMIT
* ```init_day``` : day you wish to start the evaluation, e.g. 2 correspond to the 2nd of May 0:00
* ```finish_day``` : day you wish to end the evaluation, e.g. 5 correspond to the 5th of May 23:59
* ```granularity``` : interval at which you want to perfom the evaluation (expressed in seconds!), e.g. 3600 will evaluate the model at intervals of 1 hour 

If you wish you could also select periods of time which are not day or days

```python
# j_eval_time_window(event_type, init_time, finish_time, granularity)
j_eval_time_window(0, 600, 86400, 3600)
```

* ```event_type``` : the type of event, e.g. 0 correspond to SUBMIT
* ```init_time``` : time you wish to start the evaluation (in seconds!), e.g. 600 correspond to the 600 seconds after the start of the collection of the traces (May 2nd 19:00 ETD)
* ```finish_time``` : time you wish to end the evaluation (in seconds!)
* ```granularity``` : interval at which you want to perfom the evaluation (expressed in seconds!), e.g. 3600 will evaluate the model at intervals of 1 hour 


Task Events 
---

Open the ```inter_arrival_tasks``` file and run all the cells till the **Usage** section. <br>
After that you can call the function to start the computation. <br>

```python
# t_eval_day(event_type, machine_ID, job_ID, day, granularity)
t_eval_day(0, 2, 3600)
```

* ```event_type``` : the type of event, e.g. 0 correspond to SUBMIT
* ```machine_ID```: ID of the machine running the task
* ```job_ID```: ID of the jobs the task belongs to
* ```day``` : day you wish to evaluate, e.g. 2 correspond to the 2nd of May from 0:00 until 23:59
* ```granularity``` : interval at which you want to perfom the evaluation (expressed in seconds!), e.g. 3600 will evaluate the model at intervals of 1 hour 

```python
# t_eval_days(event_type, machine_ID, job_ID, init_day, finish_day, granularity)
t_eval_days(0, 1, 1, 2, 5, 3600)
```

* ```event_type``` : the type of event, e.g. 0 correspond to SUBMIT
* ```machine_ID```: ID of the machine running the task
* ```job_ID```: ID of the jobs the task belongs to
* ```init_day``` : day you wish to start the evaluation, e.g. 2 correspond to the 2nd of May 0:00
* ```finish_day``` : day you wish to end the evaluation, e.g. 5 correspond to the 5th of May 23:59
* ```granularity``` : interval at which you want to perfom the evaluation (expressed in seconds!), e.g. 3600 will evaluate the model at intervals of 1 hour 

If you wish you could also select periods of time which are not day or days

```python
# t_eval_time_window(event_type, machine_ID, job_ID, init_time, finish_time, granularity)
t_eval_time_window(0, 1, 1, 600, 86400, 3600)
```

* ```event_type``` : the type of event, e.g. 0 correspond to SUBMIT
* ```machine_ID```: ID of the machine running the task
* ```job_ID```: ID of the jobs the task belongs to
* ```init_time``` : time you wish to start the evaluation (in seconds!), e.g. 600 correspond to the 600 seconds after the start of the collection of the traces (May 2nd 19:00 ETD)
* ```finish_time``` : time you wish to end the evaluation (in seconds!)
* ```granularity``` : interval at which you want to perfom the evaluation (expressed in seconds!), e.g. 3600 will evaluate the model at intervals of 1 hour 

Output
===
Py-tracy outputs a csv file containing the processed traces in the format described below, and it also outputs some graphs showing the computed inter-arrival values. <br>
Those graphs represents:
* Mean  
* Variance
* Median
* Standart Variation

Job events csv format
---
```
init_time,finish_time,timestamp_1,timestamp_2,inter_time
```
* ```init_time``` and ```finish_time```: those are time values considered with respect to the granularity, for example if we consider a granularity of 1 hour (3600 seconds) over the 2nd of May, the values will be ```0:00 am - 1:00 am```, ```1:00 am - 2:00 am``` and so on (in seconds).
* ```timestamp_1``` and ```timestamp_2```: those represent 2 subsequent logs in the traces, used to evaluate the inter-arrival rate.
* ```inter time```: the computed inter-arrival time

The name of the csv in written in this format
```
jobs_intervals_event-type_init-time_finish-time_@granularity.csv
```

Task events csv format
---
```
init_time,finish_time,timestamp_1,timestamp_2,inter_time
```
* ```init_time``` and ```finish_time```: those are time values considered with respect to the granularity, for example if we consider a granularity of 1 hour (3600 seconds) over the 2nd of May, the values will be ```0:00 am - 1:00 am```, ```1:00 am - 2:00 am``` and so on (in seconds).
* ```timestamp_1``` and ```timestamp_2```: those represent 2 subsequent logs in the traces, used to evaluate the inter-arrival rate.
* ```inter time```: the computed inter-arrival time

The name of the csv in written in this format
```
tasks_intervals_event-type_machine-ID_job-ID_init-time_finish-time_@granularity.csv
```
