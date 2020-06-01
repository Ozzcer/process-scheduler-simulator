class Process:
    def __init__(self, id, length):
        self.id = id
        self.length = length
        self.timeProcessed = 0
        self.timeWaiting = 0

    def process(self, timeSlice):
        self.timeProcessed += timeSlice
        return (self.length-self.timeProcessed)

    def wait(self, timeProcessed):
        self.timeWaiting += timeProcessed


class Scheduler:
    def __init__(self):
        self.readyProcesses = []
        self.doneProcesses = []
        self.currentProcessCounter = 0
        self.readyProcessCount = 0

    def __str__(self):
        output = "---------------------------\nReady Processes:"
        for process in self.readyProcesses:
            output += "\nProcess " + str(process.id) + ": [length: " + str(process.length) +", timeProcessed: " + str(process.timeProcessed) + ", timeWaiting: " + str(process.timeWaiting)  +"]"
        output += "\nDone Processes:"
        for process in self.doneProcesses:
            output += "\nProcess " + process.id + ": " + process.length
        output+="\n---------------------------\n"
        return output

    def addProcess(self, processLength):
        self.readyProcesses.append(
            Process(self.readyProcessCount, processLength))
        self.readyProcessCount += 1

    def transitionProcess(self, processId):
        self.doneProcesses.append(self.readyProcesses[processId])
        self.readyProcesses.pop(processId)

    def waitOtherProcesses(self, waitTime):
        for process in self.readyProcesses:
            if process.id != self.readyProcesses[self.currentProcessCounter].id:
                process.wait(waitTime)

    def RR_process(self, timeSlice):
        processTimeRemaining = 0
        waitTime = 0

        while (self.readyProcesses > 0):
            if self.currentProcessCounter == self.readyProcessCount:
                self.currentProcessCounter = 0

            processTimeRemaining = self.readyProcesses[self.currentProcessCounter].process(timeSlice)
            waitTime = timeSlice if processTimeRemaining >= 0 else timeSlice + processTimeRemaining
            self.waitOtherProcesses(waitTime)

            if processTimeRemaining < 0:
                self.transitionProcess(self.currentProcessCounter)

            self.currentProcessCounter += 1


scheduler = Scheduler()
processLength = 0

print("Welcome to the scheduler simulator, please enter the lengths of your processes, enter -1 when you have finished entering processes")

while processLength != -1:
    prompt = "Process " + str(scheduler.currentProcessCounter) + ": "
    processLength = int(input(prompt))

    if processLength > 0 :
        scheduler.addProcess(processLength)

    print(scheduler)

