import numpy

class Validation:
    def __init__(self, n):
        if n == 1:
            self.validate_data(1000, 'data/servinsp1.dat', 'Inspector 1 - Component 1')
            self.validate_data(1000, 'data/servinsp22.dat', 'Inspector 2 - Component 2')
            self.validate_data(1000, 'data/servinsp23.dat', 'Inspector 2 - Component 3')
            self.validate_data(1000, 'data/ws1.dat', 'Workstation 1')
            self.validate_data(1000, 'data/ws2.dat', 'Workstation 2')
            self.validate_data(1000, 'data/ws3.dat', 'Workstation 3')
        elif n == 2:
            self.validate_data(30000, 'data/servinsp1.dat', 'Inspector 1 - Component 1')
            self.validate_data(30000, 'data/servinsp22.dat', 'Inspector 2 - Component 2')
            self.validate_data(30000, 'data/servinsp23.dat', 'Inspector 2 - Component 3')
            self.validate_data(30000, 'data/ws1.dat', 'Workstation 1')
            self.validate_data(30000, 'data/ws2.dat', 'Workstation 2')
            self.validate_data(30000, 'data/ws3.dat', 'Workstation 3')

    def validate_data(self, n, data, name):
        # Finding the average of the given data from .dat
        input_data = open(data).read().splitlines()
        a_mean = 0
        for x in range(0, 300):
            a_mean += float(input_data[x])
        a_mean = a_mean / 300

        # Finding the average of the random data 
        r_mean = 0
        for x in range(0, n):
            r_mean += self.random_mean(input_data)
        r_mean = r_mean / n

        print(name)
        # Comparing the two means
        print('Actual Mean: ', a_mean)
        print('Random Mean: ', r_mean)
        print('Yield(%):    ', (abs(a_mean - r_mean) / a_mean) * 100, '\n')

    def random_mean(self, input_data):
        total = 0
        for x in range(0, 300):
            total += float(input_data[x])
        mean = total / 300
        #   Return random mean 
        return numpy.random.exponential(mean, 1)[0]


