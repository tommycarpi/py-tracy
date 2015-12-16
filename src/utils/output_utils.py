# Write on file
def create_sub_row(elem):
    return str(elem[0]) + "," + str(elem[1]) + "," + str(elem[2]) + "," + str(elem[3]) + "," + str(elem[4])

def write_jobs_csv(interval_list, event_type, init_time, finish_time, granularity):
    init_time = init_time * 10**(-6)
    finish_time = finish_time * 10**(-6)
    granularity = granularity * 10**(-6)
    f = open("../csv/jobs_intervals_"+str(event_type)+"_"+str(int(init_time))+"_"+str(int(finish_time))+"_@"+str(int(granularity))+".csv",'w')
    f.write("init_time,finish_time,timestamp_1,timestamp_2,inter_time\n") # write csv header
    
    for element in interval_list:
        f.write(create_sub_row(element) + "\n")
    f.close()   
    
def write_tasks_csv(interval_list, event_type, machine_ID, job_ID, init_time, finish_time, granularity):
    init_time = init_time * 10**(-6)
    finish_time = finish_time * 10**(-6)
    granularity = granularity * 10**(-6)
    f = open("../csv/tasks_intervals_"+str(event_type)+"_"+str(machine_ID)+"_"+str(job_ID)+"_"+str(int(init_time))+"_"+str(int(finish_time))+"_@"+str(int(granularity))+".csv",'w')
    f.write("init_time,finish_time,timestamp_1,timestamp_2,inter_time\n") # write csv header
    
    for element in interval_list:
        f.write(create_sub_row(element) + "\n")
    f.close()   