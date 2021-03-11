import matplotlib.pyplot as plt
import numpy as np

def queue(lam,time):
    total_waiting_time = 0                                    # The future total waiting time
    average_waiting_time = 0                                  # The future average waiting time
    queue=[]                                                  # The queue that will be filled with jobs of the form [arrival_time,service_requirement]
    arrivals = np.random.poisson(lam,time)                    # The arrivals time of every job with an arrival rate following a poisson process of rate lam
    for t,n in enumerate(arrivals):                           # For every time, we count the jobs that arrive and put them in the queue
        queue += [[t,0]]*n                                  
    for job in queue:                                         # For every job in the queue we will chose the requirement time
        if np.random.random() < 0.98:                         # We chose the requirement time randomly
            job[1] = 1
        else:
            job[1] = 201
            
    time = 0                                                  # This represents the time during processing
    for job in queue:                                         # We begin to process the jobs
        arrival_time,process_time = job                       # We process the first job in the list(FCFS) 
        if time < arrival_time:                               # If the next job has not yet arrived, we wait for it
            time = arrival_time + 1 
        elif time == arrival_time:                            # If the next job has just arrived, we process it for its process time
            time += process_time
        else:                                                 # If the next job has arrived some time ago, this is added to the total waiting time, and we process for the required process time
            total_waiting_time += time - arrival_time
            time += process_time                                    
    if len(queue):                                            # Just in case we have a very bad luck
        average_waiting_time = total_waiting_time/len(queue)  # We process the mean waiting time
    return(average_waiting_time,queue,arrivals)

print(queue(0.6,3))