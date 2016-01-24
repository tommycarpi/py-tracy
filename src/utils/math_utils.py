import numpy
import math
# We define some useful functions that will be used later for our computation

# Given a list of timestamps we create tuples containing each element and it's
# follower (if any) in the list
# E.G. given the list [1,2,3,4,5]
# the output will be:
# [(1,2), (2,3), (3,4), (4,5)]
def calculate_tuples(cluster_list):
    tuples = []
    for i,e in enumerate(cluster_list):
        if i < len(cluster_list)-1:
            tuples.append((e,cluster_list[i+1]))
    return tuples

# Given a list of ordered timestamps we evaluate the mean time passed between subsequent logs
def mean_time_evaluation(sc, cluster_list):
    tuples = calculate_tuples(cluster_list)
    # Transform the array into an RDD for faster computation
    tuples_RDD = sc.parallelize(tuples)
    # Create an RDD such that the resulting element is the subtraction between the
    # 2 element of the tuples in reverse order.
    # This operation will return the time passed between the 2 different logs
    tuples_RDD = tuples_RDD.map(lambda elem: (elem[1]-elem[0]))
    # Then we apply the mean() over all the values
    mean_value = numpy.mean(tuples_RDD.collect())
    return mean_value

def global_metrics(sc, cluster_list):
    tuples = calculate_tuples(cluster_list)
    # Transform the array into an RDD for faster computation
    tuples_RDD = sc.parallelize(tuples)
    # Create an RDD such that the resulting element is the subtraction between the
    # 2 element of the tuples in reverse order.
    # This operation will return the time passed between the 2 different logs
    tuples_RDD = tuples_RDD.map(lambda elem: ((elem[1]-elem[0])/10**6))
    tuples_list = tuples_RDD.collect()
    return [numpy.mean(tuples_list), numpy.var(tuples_list), numpy.median(tuples_list), numpy.std(tuples_list)]

def get_interval_values(sc, cluster_list, init_time, finish_time):
    tuples = calculate_tuples(cluster_list)
    interval = map(lambda elem: (init_time, finish_time, elem[0], elem[1], (elem[1]-elem[0])/10**6),tuples)
    return interval

def metrics(inter_list):
    # 1. mean
    # 2. variance
    # 3. median
    # 4. standard deviation
    if inter_list.count > 0:
        return [numpy.mean(inter_list), numpy.var(inter_list), numpy.median(inter_list), numpy.std(inter_list)]
    else:
        return [0,0,0,0]

# In this function we unite all the calculated inter-arrivals that belong to the same cluster
# i.e. to the same temporal slot defined by the granularity
def evaluate_statistics(sc, interval_list):
    interval_list_RDD = sc.parallelize(interval_list)
    interval_list_RDD = interval_list_RDD.map(lambda elem:((elem[0], elem[1]), elem[4]))\
        .groupByKey()\
        .sortByKey(1,1)\
        .map(lambda elem: (elem[0][0], elem[0][1], metrics(list(elem[1]))))
        
    return interval_list_RDD.collect()

def removeNans(evaluated_means_list):
    for elem in evaluated_means_list:
        if math.isnan(elem[2]):
            elem[2] = 0
    return evaluated_means_list

# Transform time into microseconds
def adjust_values(init_time, finish_time, granularity):
    init_time = init_time*10**6
    finish_time = finish_time*10**6
    granularity = granularity*10**6
    return init_time, finish_time, granularity

# ** Parameters evaluation **
# The following functions evaluate the input (day number) given by the user and covert it
# in seconds in order to evaluate the traces

def get_day_function_parameters(day):
    if day > 30:
        print "Error, exceeded month length (30 days)"
        return None,None
    else:
        # Define parameters for the function
        init_time = 0
        finish_time = 0
        if day != 1:
            init_time = 18000 + (day-2) * 86400
            finish_time = 18000 + (day-1) * 86400 - 1     
        else:
            init_time = 0
            finish_time = 18000
        # Return the computed values
        return init_time, finish_time
    
def get_days_function_parameters(init_day, finish_day):
    if init_day > finish_day:
        print "Error, init day must be previous finish day"
        return None,None
    elif init_day > 30 or finish_day > 30:
        print "Error, exceeded month length (30 days)"
        return None,None
    else:
        # Define parameters for the function
        init_time = 0
        finish_time = 0
        if init_day != 1:
            init_time = 18000 + (init_day-2) * 86400
            finish_time = 18000 + (finish_day-1) * 86400 - 1   
        else:
            init_time = 0
            finish_time = 18000 + (finish_day-1) * 86400 - 1
        return init_time, finish_time