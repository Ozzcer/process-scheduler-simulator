import scheduler

scheduler = scheduler.Scheduler()
processLength = 0

scheduler.addProcess(20)
scheduler.addProcess(10)
scheduler.addProcess(15)
scheduler.addProcess(5)

print(scheduler)

'''
scheduler._RR_process(5, False)


print("Final:\n" +str(scheduler))
print("Wait times:\n---------------------------\nTotal wait time: "+ str(scheduler.totalWaitTime()) + "\nAverage wait time: " + str(scheduler.averageWaitTime()) + "\n---------------------------")
print("Processing times:\n---------------------------\nTotal Processing time: "+ str(scheduler.totalProcessingTime()) + "\nAverage Processing time: " + str(scheduler.averageProcessingTime()) + "\n---------------------------")
'''

scheduler._FCFS_process(True)