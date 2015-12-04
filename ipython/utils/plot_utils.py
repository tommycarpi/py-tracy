from bokeh.plotting import figure, show, output_file
from bokeh.io import output_notebook

# Function to plot some values calculated over the single clusters
def plot_metrics(metrics_list):
    # Prepare dataset for plotting
    metrics_list_RDD = sc.parallelize(metrics_list)
    x_axis = metrics_list_RDD.map(lambda elem: (elem[0]+elem[1])/2).collect()
    y_axis = metrics_list_RDD.map(lambda elem: elem[2]).collect()
    
    # Plot the graphs
    p = figure(title="Metrics on job events", x_axis_label='Time Window (seconds)', y_axis_label='Mean Time (seconds)')
    # Mean
    #p.line(x_axis, metrics_list_RDD.map(lambda elem: elem[2][0]).collect(), line_width=1.5, line_color="orange")
    # Variance
    p.line(x_axis, metrics_list_RDD.map(lambda elem: elem[2][1]).collect(), line_width=1.5, line_color="red")
    # Median 
    #p.line(x_axis, metrics_list_RDD.map(lambda elem: elem[2][2]).collect(), line_width=1.5, line_color="blue")
    # Starndard Deviation 
    #p.line(x_axis, metrics_list_RDD.map(lambda elem: elem[2][3]).collect(), line_width=1.5, line_color="green")
    
    # Show the results
    show(p)
    
# Function to plot some values calculated over the single clusters
def plot_custom_metrics(sc, metrics_list, metric_id, trace_id, x_label, y_label, color):
    # Prepare dataset for plotting
    metrics_list_RDD = sc.parallelize(metrics_list)
    x_axis = metrics_list_RDD.map(lambda elem: (elem[0]+elem[1])/2e+6).collect()
    y_axis = metrics_list_RDD.map(lambda elem: elem[2]).collect()
    
    # Plot the graphs
    p = figure(title="Metrics on "+str(trace_id)+" events", x_axis_label=x_label, y_axis_label=y_label)
    p.line(x_axis, metrics_list_RDD.map(lambda elem: elem[2][metric_id]).collect(), line_width=1.5, line_color=color)
    
    # Show the results
    show(p)
    
    
def plot_inter_arrivals(sc, evaluated_means_list, mean_time_whole_period):
    # Prepare dataset for plotting
    evaluated_means_RDD = sc.parallelize(evaluated_means_list)
    x_axis = evaluated_means_RDD.map(lambda elem: (elem[0]+elem[1])/2e+6).collect()
    y_axis = evaluated_means_RDD.map(lambda elem: elem[2]/1e+6).collect()
    
    # Plot the graphs
    p = figure(title="Mean inter-arrival time", x_axis_label='Time Window (seconds)', y_axis_label='Mean Time (seconds)')
    p.line(x_axis, y_axis, line_width=1.5, line_color="orange")
    p.ray(x=x_axis[0],y=mean_time_whole_period/1e+6,length=x_axis[len(x_axis)-1]-x_axis[0], angle=0, line_color="red")
    p.circle(x_axis, y_axis, size=3, legend="Time", line_color="red", fill_color="red", fill_alpha=1.0)

    # Show the results
    show(p)