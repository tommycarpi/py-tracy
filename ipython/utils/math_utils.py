import numpy
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