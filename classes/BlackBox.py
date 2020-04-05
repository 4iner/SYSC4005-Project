from array import *
import time

class Blackbox:
    def __init__(self):
        # Making 1-D Arrays
        self.inspector1 = []
        self.inspector2 = []
        self.workstation1 = []
        self.workstation2 = []
        self.workstation3 = []  
        # Converting 1-D to 2-D Arrays      
        self.inspector1.append([])
        self.inspector2.append([])
        self.workstation1.append([])
        self.workstation2.append([])
        self.workstation3.append([])
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
        #self.printArr(self.workstation1)
        print()
        print("Blackbox Results")
        print()

        print("Workstation 1 Average -> {}".format(self.averageArr(self.workstation1[0], self.workstation1[1])))
        print("Workstation 1 Arrival Rate -> {}".format(self.arrivalRate(self.workstation1[0], self.workstation1[1])))
        print("Workstation 1 Little's Law -> {}".format(self.arrivalRate(self.workstation1[0], self.workstation1[1]), self.averageArr(self.workstation1[0], self.workstation1[1])))
        print("Workstation 1 Equal Length -> {}".format(self.equalLength(self.workstation1[0], self.workstation1[1])))
        print("Workstation 1 Clock -> {}".format(self.clockCheck(self.workstation1[0], self.workstation1[1])))
        print()
        print("Workstation 2 Average -> {}".format(self.averageArr(self.workstation2[0], self.workstation2[1])))
        print("Workstation 2 Equal Length -> {}".format(self.equalLength(self.workstation2[0], self.workstation2[1])))
        print("Workstation 2 Clock -> {}".format(self.clockCheck(self.workstation2[0], self.workstation2[1])))
        print()
        print("Workstation 3 Average -> {}".format(self.averageArr(self.workstation3[0], self.workstation3[1])))
        print("Workstation 3 Equal Length -> {}".format(self.equalLength(self.workstation3[0], self.workstation3[1])))
        print("Workstation 3 Clock -> {}".format(self.clockCheck(self.workstation3[0], self.workstation3[1])))
        print()
        print("Inspector 1 Average -> {}".format(self.averageArr(self.inspector1[0], self.inspector1[1])))
        print("Inspector 1 Equal Length -> {}".format(self.equalLength(self.inspector1[0], self.inspector1[1])))
        print("Inspector 1 Clock -> {}".format(self.clockCheck(self.inspector1[0], self.inspector1[1])))
        print()
        print("Inspector 2 Average -> {}".format(self.averageArr(self.inspector2[0], self.inspector2[1])))
        print("Inspector 2 Equal Length -> {}".format(self.equalLength(self.inspector2[0], self.inspector2[1])))
        print("Inspector 2 Clock -> {}".format(self.clockCheck(self.inspector2[0], self.inspector2[1])))


    def equalLength(self, array1, array2):
        return len(array1) == len(array2)

    def clockCheck(self, array1, array2):
        if not (self.equalLength(array1, array2)):
            return False
        for x in range(len(array1)):
            if (array1[x] > array2[x]):
                return False
        return True

    def averageArr(self, array1, array2):
        count = 0
        if not (self.equalLength(array1, array2)):
            return -1
        elif len(array1) == 0:
            return 0
        for x in range(len(array1)):
            count += array2[x] - array1[x]
        return count/len(array1)

    def arrivalRate(self, array1, array2):
        if not (self.equalLength(array1, array2)):
            return -1
        totalSum = 0
        for x in range(len(array1)):
            totalSum += array2[x] - array1[x]
        return len(array1)/totalSum

    def littleLaw(self, arrival, average):
        return arrival * average

    def printArr(self, array):
        for x in range(len(array[0])):
            print("Array: {}".format(array[0][x]))


# import numpy

# class Validation:
#     def __init__(self, n):
#         if n == 1:
#             self.validate_data(1000, 'data/servinsp1.dat', 'Inspector 1 - Component 1')
#             self.validate_data(1000, 'data/servinsp22.dat', 'Inspector 2 - Component 2')
#             self.validate_data(1000, 'data/servinsp23.dat', 'Inspector 2 - Component 3')
#             self.validate_data(1000, 'data/ws1.dat', 'Workstation 1')
#             self.validate_data(1000, 'data/ws2.dat', 'Workstation 2')
#             self.validate_data(1000, 'data/ws3.dat', 'Workstation 3')
#         elif n == 2:
#             self.validate_data(30000, 'data/servinsp1.dat', 'Inspector 1 - Component 1')
#             self.validate_data(30000, 'data/servinsp22.dat', 'Inspector 2 - Component 2')
#             self.validate_data(30000, 'data/servinsp23.dat', 'Inspector 2 - Component 3')
#             self.validate_data(30000, 'data/ws1.dat', 'Workstation 1')
#             self.validate_data(30000, 'data/ws2.dat', 'Workstation 2')
#             self.validate_data(30000, 'data/ws3.dat', 'Workstation 3')

#     def validate_data(self, n, data, name):
#         # Finding the average of the given data from .dat
#         input_data = open(data).read().splitlines()
#         a_mean = 0
#         for x in range(0, 300):
#             a_mean += float(input_data[x])
#         a_mean = a_mean / 300

#         # Finding the average of the random data 
#         r_mean = 0
#         for x in range(0, n):
#             r_mean += self.random_mean(input_data)
#         r_mean = r_mean / n

#         print(name)
#         # Comparing the two means
#         print('Actual Mean: ', a_mean)
#         print('Random Mean: ', r_mean)
#         print('Yield(%):    ', (abs(a_mean - r_mean) / a_mean) * 100, '\n')

#     def random_mean(self, input_data):
#         total = 0
#         for x in range(0, 300):
#             total += float(input_data[x])
#         mean = total / 300
#         #   Return random mean 
#         return numpy.random.exponential(mean, 1)[0]


