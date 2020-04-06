from array import *
import time

class Blackbox:
    def __init__(self):
        # Making 1-D Arrays
        self.component1 = []
        self.component2 = []
        self.component3 = []
        self.inspector1 = []
        self.inspector2 = []
        self.workstation1 = []
        self.workstation2 = []
        self.workstation3 = []  
        # Converting 1-D to 2-D Arrays   
        self.component1.append([])
        self.component2.append([])
        self.component3.append([]) 
        self.inspector1.append([])
        self.inspector2.append([])
        self.workstation1.append([])
        self.workstation2.append([])
        self.workstation3.append([])
        self.component1.append([])
        self.component2.append([])
        self.component3.append([]) 
        self.inspector1.append([])
        self.inspector2.append([])
        self.workstation1.append([])
        self.workstation2.append([])
        self.workstation3.append([])
        
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
    # "No. items in the queue" = "arrival rate" x "average time spent in the queue"

    def roundCheck(self):
        # Checking Equal Length Arrays
        # Checking Clock Times if all are in order 

        print()
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("\t\t\tBlackbox Results")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")



        print("Component 1 Clock \t\t-> \t{}".format(self.clockCheck(self.component1[0], self.component1[1])))
        print("Component 1 Remainders? \t-> \t{}".format(self.remainders(self.component1[0], self.component1[1])))
        print("Component 1 Average \t\t-> \t{}".format(self.averageArr(self.component1[0], self.component1[1])))
        print("Component 1 Arrival Rate \t-> \t{}".format(self.arrivalRate(self.component1[0], self.component1[1])))
        print("Component 1 Little's Law \t-> \t{}".format(self.littleLaw(self.arrivalRate(self.component1[0], self.component1[1]), self.averageArr(self.component1[0], self.component1[1]))))
        print()
        print("Component 2 Clock \t\t-> \t{}".format(self.clockCheck(self.component2[0], self.component2[1])))
        print("Component 2 Remainders? \t-> \t{}".format(self.remainders(self.component2[0], self.component2[1])))
        print("Component 2 Average \t\t-> \t{}".format(self.averageArr(self.component2[0], self.component2[1])))
        print("Component 2 Arrival Rate \t-> \t{}".format(self.arrivalRate(self.component2[0], self.component2[1])))
        print("Component 2 Little's Law \t-> \t{}".format(self.littleLaw(self.arrivalRate(self.component2[0], self.component2[1]), self.averageArr(self.component2[0], self.component2[1]))))
        print()
        print("Component 3 Clock \t\t-> \t{}".format(self.clockCheck(self.component3[0], self.component3[1])))
        print("Component 3 Remainders? \t-> \t{}".format(self.remainders(self.component3[0], self.component3[1])))
        print("Component 3 Average \t\t-> \t{}".format(self.averageArr(self.component3[0], self.component3[1])))
        print("Component 3 Arrival Rate \t-> \t{}".format(self.arrivalRate(self.component3[0], self.component3[1])))
        print("Component 3 Little's Law \t-> \t{}".format(self.littleLaw(self.arrivalRate(self.component3[0], self.component3[1]), self.averageArr(self.component3[0], self.component3[1]))))
        print()
        print("Inspector 1 Clock \t\t-> \t{}".format(self.clockCheck(self.inspector1[0], self.inspector1[1])))
        print("Inspector 1 Average \t\t-> \t{}".format(self.averageArr(self.inspector1[0], self.inspector1[1])))
        print("Inspector 1 Arrival Rate \t-> \t{}".format(self.arrivalRate(self.inspector1[0], self.inspector1[1])))
        print("Inspector 1 Little's Law \t-> \t{}".format(self.littleLaw(self.arrivalRate(self.inspector1[0], self.inspector1[1]), self.averageArr(self.inspector1[0], self.inspector1[1]))))
        print()
        print("Inspector 2 Clock \t\t-> \t{}".format(self.clockCheck(self.inspector2[0], self.inspector2[1])))
        print("Inspector 2 Average \t\t-> \t{}".format(self.averageArr(self.inspector2[0], self.inspector2[1])))
        print("Inspector 2 Arrival Rate \t-> \t{}".format(self.arrivalRate(self.inspector2[0], self.inspector2[1])))
        print("Inspector 2 Little's Law \t-> \t{}".format(self.littleLaw(self.arrivalRate(self.inspector2[0], self.inspector2[1]), self.averageArr(self.inspector2[0], self.inspector2[1]))))
        print()
        print("Workstation 1 Clock \t\t-> \t{}".format(self.clockCheck(self.workstation1[0], self.workstation1[1])))
        print("Workstation 1 Average \t\t-> \t{}".format(self.averageArr(self.workstation1[0], self.workstation1[1])))
        print("Workstation 1 Arrival Rate \t-> \t{}".format(self.arrivalRate(self.workstation1[0], self.workstation1[1])))
        print("Workstation 1 Little's Law \t-> \t{}".format(self.littleLaw(self.arrivalRate(self.workstation1[0], self.workstation1[1]), self.averageArr(self.workstation1[0], self.workstation1[1]))))
        print()
        print("Workstation 2 Clock \t\t-> \t{}".format(self.clockCheck(self.workstation2[0], self.workstation2[1])))
        print("Workstation 2 Average \t\t-> \t{}".format(self.averageArr(self.workstation2[0], self.workstation2[1])))
        print("Workstation 2 Arrival Rate \t-> \t{}".format(self.arrivalRate(self.workstation2[0], self.workstation2[1])))
        print("Workstation 2 Little's Law \t-> \t{}".format(self.littleLaw(self.arrivalRate(self.workstation2[0], self.workstation2[1]), self.averageArr(self.workstation2[0], self.workstation2[1]))))
        print()
        print("Workstation 3 Clock \t\t-> \t{}".format(self.clockCheck(self.workstation3[0], self.workstation3[1])))
        print("Workstation 3 Average \t\t-> \t{}".format(self.averageArr(self.workstation3[0], self.workstation3[1])))
        print("Workstation 3 Arrival Rate \t-> \t{}".format(self.arrivalRate(self.workstation3[0], self.workstation3[1])))
        print("Workstation 3 Little's Law \t-> \t{}".format(self.littleLaw(self.arrivalRate(self.workstation3[0], self.workstation3[1]), self.averageArr(self.workstation3[0], self.workstation3[1]))))

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
            count += array2[x] - array1[x]
        return count/len(array2)

    def arrivalRate(self, array1, array2):
        if self.averageArr(array1, array2) == 0:
            return 0.0
        totalSum = 0
        for x in range(len(array2)):
            totalSum += array2[x] - array1[x]
        return (len(array2)-1)/totalSum

    def littleLaw(self, arrival, average):
        return arrival * average

    def printArr(self, array):
        for x in range(len(array[0])):
            print("Array: {}".format(array[0][x]))

