from array import *
import time
from classes.Shared import Shared
import numpy as np

class Blackbox:
    def __init__(self):
        # Making 1-D Arrays
        self.component1 = []
        self.component12 = []
        self.component13 = []
        self.component2 = []
        self.component3 = []
        self.inspector1 = []
        self.inspector2 = []
        self.workstation1 = []
        self.workstation2 = []
        self.workstation3 = []  
        self.system = []  
        # Converting 1-D to 2-D Arrays   
        self.component1.append([])
        self.component12.append([])
        self.component13.append([])
        self.component2.append([])
        self.component3.append([]) 
        self.inspector1.append([])
        self.inspector2.append([])
        self.workstation1.append([])
        self.workstation2.append([])
        self.workstation3.append([])
        self.system.append([])
        self.component1.append([])
        self.component12.append([])
        self.component13.append([])
        self.component2.append([])
        self.component3.append([]) 
        self.inspector1.append([])
        self.inspector2.append([])
        self.workstation1.append([])
        self.workstation2.append([])
        self.workstation3.append([])
        self.system.append([])
        # Arrival Time Start
        self.startTime = time.time()
        self.endTime = 0
        # Temp Theory Value
        self.theoryLittle = 0
        
    # Idea with arrays
    # Each queue will have a 2D-Array arr[a,b]
    # arr -> Targeted array where it will place data
    # a -> store all the time that it has entered in the blackbox
    # b -> store all the time that it has left the blacbox
    # arr[a] -> total number of entrees
    # arr[b] -> total number of queue leaving
    # NOTE: Keep in that mind that when;
    #       a = b then there are 0 in the blackbox 
    #       a > b then there are N amount of queues that are in the blackbox
    # Little's Law --> l = lambda \times w
    # "No. items in the queue" = "arrival rate" x "Average (ω)time spent in the queue"

    def roundCheck(self):
        # Checking Clock Times if all are in order 
        # Checks if there are any components in queue
        # Averages out the time spent in box
        # Calculates the Arrival rate
        # Then computing the number of items in queue aka Little's Law
        print()
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("\t\t\tBlackbox Results")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print()
        print("Component 1 Clock \t\t-> \t{}".format(self.clockCheck(self.component1[0], self.component1[1])))
        print("Component 1 Remainders? \t-> \t{}".format(self.remainders(self.component1[0], self.component1[1])))
        print("Buffer 1 Average (ω) \t\t-> \t{}".format(self.averageArr(self.component1[0], self.component1[1])))
        print("Buffer 1 Arrival Rate (λ) \t-> \t{}".format(self.arrivalRate(self.component1[0], self.component1[1])))
        print("Buffer 1 λ x ω \t \t\t-> \t{}".format(self.actualLittleLaw(self.component1[0], self.component1[1])))
        print("Buffer 1 L \t\t\t-> \t{}".format(self.theoryLittleLaw(self.component1)))
        print("Buffer 1 Little's Law Error %\t\t{}%".format(self.yieldLittle(self.component1,self.component1[0], self.component1[1])))
        print()
        print("Component 12 Clock \t\t-> \t{}".format(self.clockCheck(self.component12[0], self.component12[1])))
        print("Component 12 Remainders? \t-> \t{}".format(self.remainders(self.component12[0], self.component12[1])))
        print("Buffer 12 Average (ω)\t\t-> \t{}".format(self.averageArr(self.component12[0], self.component12[1])))
        print("Buffer 12 Arrival Rate (λ)\t-> \t{}".format(self.arrivalRate(self.component12[0], self.component12[1])))
        print("Buffer 12 λ x ω \t\t->\t{}".format(self.actualLittleLaw(self.component12[0], self.component12[1])))
        print("Buffer 12 L \t\t\t-> \t{}".format(self.theoryLittleLaw(self.component12)))
        print("Buffer 12 Little's Law Error %\t\t{}%".format(self.yieldLittle(self.component12,self.component12[0], self.component12[1])))
        print()
        print("Component 13 Clock \t\t-> \t{}".format(self.clockCheck(self.component13[0], self.component13[1])))
        print("Component 13 Remainders? \t-> \t{}".format(self.remainders(self.component13[0], self.component13[1])))
        print("Buffer 13 Average (ω)\t\t-> \t{}".format(self.averageArr(self.component13[0], self.component13[1])))
        print("Buffer 13 Arrival Rate (λ)\t-> \t{}".format(self.arrivalRate(self.component13[0], self.component13[1])))
        print("Buffer 13 λ x ω \t\t-> \t{}".format(self.actualLittleLaw(self.component13[0], self.component13[1])))
        print("Buffer 13 L \t\t\t-> \t{}".format(self.theoryLittleLaw(self.component13)))
        print("Buffer 13 Little's Law Error %\t\t{}%".format(self.yieldLittle(self.component13,self.component13[0], self.component13[1])))
        print()
        print("Component 2 Clock \t\t-> \t{}".format(self.clockCheck(self.component2[0], self.component2[1])))
        print("Component 2 Remainders? \t-> \t{}".format(self.remainders(self.component2[0], self.component2[1])))
        print("Buffer 2 Average (ω)\t\t-> \t{}".format(self.averageArr(self.component2[0], self.component2[1])))
        print("Buffer 2 Arrival Rate (λ)\t-> \t{}".format(self.arrivalRate(self.component2[0], self.component2[1])))
        print("Buffer 2 λ x ω \t \t\t-> \t{}".format(self.actualLittleLaw(self.component2[0], self.component2[1])))
        print("Buffer 2 L \t\t\t-> \t{}".format(self.theoryLittleLaw(self.component2)))
        print("Buffer 2 Little's Law Error %\t\t{}%".format(self.yieldLittle(self.component2,self.component2[0], self.component2[1])))
        print()
        print("Component 3 Clock \t\t-> \t{}".format(self.clockCheck(self.component3[0], self.component3[1])))
        print("Component 3 Remainders? \t-> \t{}".format(self.remainders(self.component3[0], self.component3[1])))
        print("Buffer 3 Average (ω)\t\t-> \t{}".format(self.averageArr(self.component3[0], self.component3[1])))
        print("Buffer 3 Arrival Rate (λ)\t-> \t{}".format(self.arrivalRate(self.component3[0], self.component3[1])))
        print("Buffer 3 λ x ω \t \t\t-> \t{}".format(self.actualLittleLaw(self.component3[0], self.component3[1])))
        print("Buffer 3 L \t\t\t-> \t{}".format(self.theoryLittleLaw(self.component3)))
        print("Buffer 3 Little's Law Error %\t\t{}%".format(self.yieldLittle(self.component3,self.component3[0], self.component3[1])))
        print()
        print("Inspector 1 Clock \t\t-> \t{}".format(self.clockCheck(self.inspector1[0], self.inspector1[1])))
        print("Inspector 1 Inspected \t\t-> \t{} Component(s)".format((len(self.inspector1[0]))))
        print("Inspector 1 Average (ω)\t\t-> \t{}".format(self.averageArr(self.inspector1[0], self.inspector1[1])))
        print("Inspector 1 Arrival Rate (λ)\t-> \t{}".format(self.arrivalRate(self.inspector1[0], self.inspector1[1])))
        print("Inspector 1 λ x ω \t \t-> \t{}".format(self.actualLittleLaw(self.inspector1[0], self.inspector1[1])))
        print("Inspector 1 L \t\t\t-> \t{}".format(self.theoryLittleLaw(self.inspector1)))
        print("Inspector 1 Little's Law Error %\t{}%".format(self.yieldLittle(self.inspector1,self.inspector1[0], self.inspector1[1])))
        print()
        print("Inspector 2 Clock \t\t-> \t{}".format(self.clockCheck(self.inspector2[0], self.inspector2[1])))
        print("Inspector 2 Inspected \t\t-> \t{} Component(s)".format((len(self.inspector2[0]))))
        print("Inspector 2 Average (ω)\t\t-> \t{}".format(self.averageArr(self.inspector2[0], self.inspector2[1])))
        print("Inspector 2 Arrival Rate (λ)\t-> \t{}".format(self.arrivalRate(self.inspector2[0], self.inspector2[1])))
        print("Inspector 2 λ x ω \t \t-> \t{}".format(self.actualLittleLaw(self.inspector2[0], self.inspector2[1])))
        print("Inspector 2 L \t\t\t-> \t{}".format(self.theoryLittleLaw(self.inspector2)))
        print("Inspector 2 Little's Law Error %\t{}%".format(self.yieldLittle(self.inspector2,self.inspector2[0], self.inspector2[1])))
        print()
        print("Workstation 1 Clock \t\t-> \t{}".format(self.clockCheck(self.workstation1[0], self.workstation1[1])))
        print("Workstation 1 Produced \t\t-> \t{} Product(s)".format(len(self.workstation1[0])))
        print("Workstation 1 Average (ω)\t-> \t{}".format(self.averageArr(self.workstation1[0], self.workstation1[1])))
        print("Workstation 1 Arrival Rate (λ)\t-> \t{}".format(self.arrivalRate(self.workstation1[0], self.workstation1[1])))
        print("Workstation 1 λ x ω \t \t-> \t{}".format(self.actualLittleLaw(self.workstation1[0], self.workstation1[1])))
        print("Workstation 1 L\t\t\t-> \t{}".format(self.theoryLittleLaw(self.workstation1)))
        print("Workstation 1 Little's Law Error %\t{}%".format(self.yieldLittle(self.workstation1,self.workstation1[0], self.workstation1[1])))
        print()
        print("Workstation 2 Clock \t\t-> \t{}".format(self.clockCheck(self.workstation2[0], self.workstation2[1])))
        print("Workstation 2 Produced \t\t-> \t{} Product(s)".format(len(self.workstation2[0])))
        print("Workstation 2 Average (ω)\t-> \t{}".format(self.averageArr(self.workstation2[0], self.workstation2[1])))
        print("Workstation 2 Arrival Rate (λ)\t-> \t{}".format(self.arrivalRate(self.workstation2[0], self.workstation2[1])))
        print("Workstation 2 λ x ω \t \t-> \t{}".format(self.actualLittleLaw(self.workstation2[0], self.workstation2[1])))
        print("Workstation 2 L\t\t\t-> \t{}".format(self.theoryLittleLaw(self.workstation2)))
        print("Workstation 2 Little's Law Error %\t{}%".format(self.yieldLittle(self.workstation2,self.workstation2[0], self.workstation2[1])))
        print()
        print("Workstation 3 Clock \t\t-> \t{}".format(self.clockCheck(self.workstation3[0], self.workstation3[1])))
        print("Workstation 3 Produced \t\t-> \t{} Product(s)".format(len(self.workstation3[0])))
        print("Workstation 3 Average (ω)\t-> \t{}".format(self.averageArr(self.workstation3[0], self.workstation3[1])))
        print("Workstation 3 Arrival Rate (λ)\t-> \t{}".format(self.arrivalRate(self.workstation3[0], self.workstation3[1])))
        print("Workstation 3 λ x ω \t \t-> \t{}".format(self.actualLittleLaw(self.workstation3[0], self.workstation3[1])))
        print("Workstation 3 L\t\t\t-> \t{}".format(self.theoryLittleLaw(self.workstation3)))
        print("Workstation 3 Little's Law Error %\t{}%".format(self.yieldLittle(self.workstation3,self.workstation3[0], self.workstation3[1])))
        print()
        print("Entire Simulation Average\t-> \t{}".format(self.averageArr(self.system[0], self.system[1])))
        print("Entire Simulation Arrival Rate\t-> \t{}".format(self.arrivalRate(self.system[0], self.system[1])))
        print("Entire Simulation λ x ω \t-> \t{}".format(self.actualLittleLaw(self.system[0], self.system[1])))
        print("Entire Simulation L\t\t-> \t{}".format(self.theoryLittleLaw(self.system)))
        print("Entire Simulation Little's Law Error %\t{}%".format(self.yieldLittle(self.system,self.system[0], self.system[1])))
    
    
    def clockCheck(self, array1, array2):
        for x in range(len(array2)):
            if (array1[x] > array2[x]):
                return "Bad"
        return "Good"

    def remainders(self, array1, array2):
        return len(array1) - len(array2)

    def averageArr(self, array1, array2):
        count = 0
        if len(array1) == 0:
            return 0.0
        for x in range(len(array2)):
            count += (array2[x] - array1[x]) # Shared.timeFromString convert back
        return count/len(array2)

    def arrivalRate(self, array1, array2):
        if self.averageArr(array1, array2) == 0:
            return 0.0
        return (len(array2) - 1)/(self.endTime - self.startTime)

    def theoryAverageArr(self, array):
        sum = 0
        for x in range(len(array[1])):
            sum += float(array[1][x] - array[0][x])
        mean = sum / len(array[1])
        return np.random.exponential(mean, 1)[0]

    def theoryLittleLaw(self, array):
        total = 0
        for x in range(len(array[1])):
            total += self.theoryAverageArr(array)
        if total == 0:
            return -1
        self.theoryLittle = total/len(array[1]) * (len(array[1]) - 1)/(self.endTime - self.startTime)
        return self.theoryLittle

    def actualLittleLaw(self, array1, array2):
        return self.arrivalRate(array1, array2) * self.averageArr(array1, array2)

    def yieldLittle(self, array, array1, array2):
        if self.theoryLittleLaw(array) == 0:
            return -1
        return str(round((abs(self.actualLittleLaw(array1,array2) - self.theoryLittle)) / self.theoryLittle * 100, 2))

    def printArr(self, array):
        for x in range(len(array[0])):
            print("Array: {}".format(array[0][x]))

