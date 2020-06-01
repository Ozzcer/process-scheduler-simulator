import scheduler

scheduler = scheduler.Scheduler()
processLength = 0

scheduler.addProcess(20)
scheduler.addProcess(10)
scheduler.addProcess(15)
scheduler.addProcess(5)
scheduler.addProcess(18)
scheduler.addProcess(13)
scheduler.addProcess(24)
scheduler.addProcess(1)
scheduler.addProcess(17)
scheduler.addProcess(33)

print(scheduler)

scheduler.RR_process(5, False)


print("Final:\n" +str(scheduler))
print("Wait times:\n---------------------------\nTotal wait time: "+ str(scheduler.totalWaitTime()) + "\nAverage wait time: " + str(scheduler.averageWaitTime()) + "\n---------------------------")
print("Processing times:\n---------------------------\nTotal Processing time: "+ str(scheduler.totalProcessingTime()) + "\nAverage Processing time: " + str(scheduler.averageProcessingTime()) + "\n---------------------------")

print("Sort:")
scheduler.sortDoneByProcessId()
print(scheduler)

print("Reset:")
scheduler.reset()
print(scheduler)


scheduler.RR_process(5, False)
print("Wait times:\n---------------------------\nTotal wait time: "+ str(scheduler.totalWaitTime()) + "\nAverage wait time: " + str(scheduler.averageWaitTime()) + "\n---------------------------")
print("Processing times:\n---------------------------\nTotal Processing time: "+ str(scheduler.totalProcessingTime()) + "\nAverage Processing time: " + str(scheduler.averageProcessingTime()) + "\n---------------------------")

scheduler.reset()

scheduler.RR_process(10, False)
print("Wait times:\n---------------------------\nTotal wait time: "+ str(scheduler.totalWaitTime()) + "\nAverage wait time: " + str(scheduler.averageWaitTime()) + "\n---------------------------")
print("Processing times:\n---------------------------\nTotal Processing time: "+ str(scheduler.totalProcessingTime()) + "\nAverage Processing time: " + str(scheduler.averageProcessingTime()) + "\n---------------------------")

scheduler.reset()

scheduler.RR_process(15, False)
print("Wait times:\n---------------------------\nTotal wait time: "+ str(scheduler.totalWaitTime()) + "\nAverage wait time: " + str(scheduler.averageWaitTime()) + "\n---------------------------")
print("Processing times:\n---------------------------\nTotal Processing time: "+ str(scheduler.totalProcessingTime()) + "\nAverage Processing time: " + str(scheduler.averageProcessingTime()) + "\n---------------------------")


scheduler.reset()

scheduler.RR_process(20, False)
print("Wait times:\n---------------------------\nTotal wait time: "+ str(scheduler.totalWaitTime()) + "\nAverage wait time: " + str(scheduler.averageWaitTime()) + "\n---------------------------")
print("Processing times:\n---------------------------\nTotal Processing time: "+ str(scheduler.totalProcessingTime()) + "\nAverage Processing time: " + str(scheduler.averageProcessingTime()) + "\n---------------------------")
