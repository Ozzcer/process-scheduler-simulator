import scheduler
import sys


def userInput(prompt):
    userInput = input(prompt)
    if userInput == "exit":
        print("Exiting...")
        sys.exit()
    return userInput


def getProcessLengths(scheduler):
    print("Welcome to the scheduler simulator, please enter the lengths of your processes, enter a negative number when you have finished entering processes, type exit at any time to leave the program.")
    processLength = 0
    while processLength > -1:
        prompt = "Process " + str(scheduler.readyProcessCount) + ": "
        try:
            processLength = int(userInput(prompt))
            if processLength > 0:
                scheduler.addProcess(processLength)
                print(scheduler)
            elif processLength == 0:
                print("Process cannot have zero length")
            elif scheduler.readyProcessCount < 1:
                processLength = 0
                print("Must have at least 1 process")

        except TypeError:
            print("Not a number, type exit to leave.")
        except ValueError:
            print("Not a number, type exit to leave.")

    print(scheduler)


def getSchedulingMethod():
    print("Scheduling methods:\n---------------------------\nRR = Round Robin\n---------------------------")

    schedulingMethod = "notSpecified"
    while schedulingMethod == "notSpecified":
        schedulingMethod = userInput("Please enter the desired scheduling method: ").upper()
        if schedulingMethod == "RR":
            return schedulingMethod
        else:
            print("Not a valid scheduling method, type exit to leave.")
            schedulingMethod = "notSpecified"


def getTimeSlice():
    timeSlice = 0
    while timeSlice == 0:
        try:
            timeSlice = int(userInput("Please enter the time slice length: "))
            if timeSlice > 0:
                return timeSlice
            else:
                print("Time slice cannot be less than one, type exit to leave.")
                timeSlice = 0
        except TypeError:
            print("Not a number, type exit to leave.")
        except ValueError:
            print("Not a number, type exit to leave.")

def getPrintEachStep():
    recievedInput = False

    while recievedInput == False:
        printEachStep = userInput("Do you wish to print each step of the scheduling? Y/N: ").upper()
        if printEachStep == "Y":
            recievedInput = True
        elif printEachStep == "N":
            recievedInput = True
        else:
            print("Not valid input, type exit to leave.")
    
    return True if getPrintEachStep=="Y" else False

def runSchedule():
    schedulingMethod = getSchedulingMethod()
    timeSlice = getTimeSlice()
    printEachStep = getPrintEachStep()

    scheduler.schedule(schedulingMethod,timeSlice,printEachStep)

    print("\n---------------------------\nFinal:\n" +str(scheduler))
    print("Wait times:\n---------------------------\nTotal wait time: "+ str(scheduler.totalWaitTime()) + "\nAverage wait time: " + str(scheduler.averageWaitTime()) + "\n---------------------------")
    print("Processing times:\n---------------------------\nTotal Processing time: "+ str(scheduler.totalProcessingTime()) + "\nAverage Processing time: " + str(scheduler.averageProcessingTime()) + "\n---------------------------")

def finishedOptions(scheduler):
    startAgain = False
    while not startAgain:
        print("Options - enter one of these commands to do something with your schedule:\n---------------------------\nexit - quits program\nreset - resets schedule but keeps processes so you can try a different method or timeslice\nsort - sorts done queue by process id\n---------------------------")
        option = userInput("").lower()

        if option == ("reset"):
            scheduler.reset()
            print(scheduler)
            startAgain = True
        elif option == "sort":
            scheduler.sortDoneByProcessId()
            print(scheduler)
        else:
            print("Not a valid option, type exit to leave.")
    
    return False
            
stop = False
scheduler = scheduler.Scheduler()
getProcessLengths(scheduler)

while not stop :
    runSchedule()
    stop = finishedOptions(scheduler)


