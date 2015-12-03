# Write on file
def create_sub_row(elem):
    return str(elem[0]) + "\t" + str(elem[1]) + "\t" + str(elem[2]) + "\t" + str(elem[3]) + "\t" + str(elem[4])

def write_csv(interval_list, event_type, init_time, finish_time, granularity):
    f = open("../csv/jobs_intervals_"+str(event_type)+"_"+str(init_time)+"_"+str(finish_time)+"_@"+str(granularity),'w')
    f.write("init_time,finish_time,timestamp_1,timestamp_2,inter_time\n") # write csv header
    
    for element in interval_list:
        f.write(create_sub_row(element) + "\n")
    f.close()   