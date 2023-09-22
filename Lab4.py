from random import *
import heapq

cpuproc = []

for i in range(-20,20):
    cpuproc.append((i,randint(1,100)))

process = ""
heapq.heapify(cpuproc)
print(cpuproc)
for i in range(0,len(cpuproc)):
    if 100>=cpuproc[i][1]>95: 
        process = "No process running for this time slice"
        print(process)
        continue 
    elif 95>=cpuproc[i][1]>90: process = "Completing Arithmetic: "
    elif 90>=cpuproc[i][1]>80: process = "Decoding: "
    elif 80>=cpuproc[i][1]>70: process = "Execution: "
    elif 70>=cpuproc[i][1]>60: process="Managing: "
    elif 60>=cpuproc[i][1]>50: process = "Logic Processing: "
    elif 50>=cpuproc[i][1]>40: process = "Fetching instructions: "
    elif 40>=cpuproc[i][1]>30: process = "Pipelining: "
    elif 30>=cpuproc[i][1]>20: process = "Moving Data: "
    elif 20>=cpuproc[i][1]>10: process = "Handling Execptions: "
    else: process = "Excuting Control Flow"
    print("Task ", str(i), " ",process, " Started")
    count = 0
    for l in range(1,cpuproc[i][1]+1):
        count+=1
        #print("Time slice ",count) #This piece of code makes the output cluttered so its commentted out
        if count==cpuproc[i][1]: print(process+ " Completed")

