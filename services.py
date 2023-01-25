class Service():
    def __init__(self, desc, cat, job_id, step, abbriev=None, allowed_connections=None):
        self.description = desc
        self.category = cat
        self.job_id = job_id
        self.step = step
        self.tag = abbriev
        self.connections = allowed_connections
        # self.time_estimate = None

    def __str__(self):
        return f"{self.description}"

class Job:
    def __init__(self, job_tag, steps: int, sop: list[Service], priority):
        self.tag = job_tag
        self.num_steps = steps
        self.sop = sop # sequence of protocols
        self.priority = priority

    def __str__(self) -> str:
        return f"JOB {self.tag} with {self.num_steps} steps"

'''
A job consists of:
* unique job ID
* ordered sequence of Services
* a priority level assigned to it

A Service consists of:
* ID associated to the job
* step # in the Service
* description
* category of the action
'''

import pandas as pd

options = pd.read_csv("data/services.csv")
services = options.iloc[:,1]
services = [a for a in services if a is not None and type(a) == str and a != 'nan']
categories = options.iloc[:,2]
services_plus_categories = list(zip(services, categories))

print('\n--- List of Services ---')
count = 1
for d in services_plus_categories:
    print(str(count) + "|" + str(d[0]) + "| category " + str(d[1]))
    count+=1
print(' ')

num_services = len(services_plus_categories)
print(str(num_services) + " services currently offered by the DAMP lab.\n")

'''
randomly generated Services below for testing purposes
- a job can have any number of Services
- random sequence of Services make up a job
- randomly assigned priority value
'''

import random

num_jobs = random.randint(1, 10)
jobs_sizes = [random.randint(1, 20) for i in range(num_jobs)]
jobs = list(zip(map(lambda n: 'J-' + str(n), range(1, num_jobs + 1)), jobs_sizes))
print("Auto-generated jobs: ")
print(jobs)
print(' ')

received_jobs = []
for j in jobs:
    (job_name, num_steps) = j
    print(j)
    sop = []
    for i in range(num_steps):
        rand_pick = random.randint(0, len(services_plus_categories)-1) #can make this more random
        (s, c) = services_plus_categories[rand_pick]
        print((s, c))
        rand_service = Service(s, c, job_name, i)
        sop = sop + [rand_service]
    new_job = Job(job_name, num_steps, sop, 0)
    received_jobs.append(new_job)
    print('OK\n')

# print(received_jobs)
for j in received_jobs:
    print(str(j))

#Equipment Capacity/Availability
#Duration of each Job