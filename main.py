from classes.Buffer import Buffer
from classes.Buffer23 import Buffer23
from classes.BufferBox import BufferBox
from classes.Component import Component
from classes.Indicator import Indicator
from classes.Inspector1 import Inspector1
from classes.Inspector2 import Inspector2
from classes.Workstation1 import Workstation1
from classes.Workstation2 import Workstation2
from classes.Workstation3 import Workstation3
from helper import getValWei, getValXP
import shutil
import os


def main():
    # create buffers for the components. b1,b2,b3 hold C1, b4 holds C2, b5 holds C3
    b1 = Buffer()
    b2 = Buffer()
    b3 = Buffer()
    b4 = Buffer23() # c2 buffer
    b5 = Buffer23() # c3 buffer

    # create threads given the buffers
    bb = BufferBox(b1, b2, b3)
    i1 = Inspector1([Component.C1], bb)
    i2 = Inspector2([Component.C2, Component.C3], b4, b5)
    w1 = Workstation1(bb)
    w2 = Workstation2(bb, b4)
    w3 = Workstation3(bb, b5)

    # making the threads daemon, so if one of the threads stop then the program stops
    # similar to a manufacturing facility, if they don't have the components then no
    # products can be made
    i1.daemon = True
    i2.daemon = True
    w1.daemon = True
    w2.daemon = True
    w3.daemon = True

    # indicator to see when a inspector or workstation has completed their commands
    ind = Indicator([i1, i2, w1, w2, w3])

    # Prompt user for type of data, generated/given
    print("Enter 1 for Given data, 2 to Generate data")
    genOrGiven = int(input())
    if(genOrGiven == 2):
        # print("Deleting previous generated data...")
        # shutil.rmtree("data_generated")
        # print("Making directory...")
        # os.mkdir("data_generated")
       
        print("Please enter the preferred size of your data: ")
        size = input()
        size = int(size)

        # Generated data is created with parameters calculated from the data. The report should contain these values.
        writeTo('data_generated/ws1.dat','exponential',size,mean=4.604417)
        writeTo('data_generated/ws2.dat','exponential',size,mean=11.09261)
        writeTo('data_generated/ws3.dat','weibull',size,alpha=9,beta=1)
        writeTo('data_generated/servinsp1.dat','weibull',size,alpha=11,beta=1.2)
        writeTo('data_generated/servinsp22.dat','exponential',size,mean=15.5369)
        writeTo('data_generated/servinsp23.dat','exponential',size,mean=20.63276)

        i1.datadir = 'data_generated/servinsp1.dat'
        i2.datadir1 = 'data_generated/servinsp22.dat'
        i2.datadir2 = 'data_generated/servinsp23.dat'
        w1.datadir = 'data_generated/ws1.dat'
        w2.datadir = 'data_generated/ws2.dat'
        w3.datadir = 'data_generated/ws3.dat'
            

    else: 
        
        pass

    # # start threads
    i1.start()
    i2.start()
    w1.start()
    w2.start()
    w3.start()
    ind.start()

def writeTo(file, dist, size, mean=0, alpha=0, beta=0):
    if dist == "weibull":
        with open(file, 'w') as file:
            for i in range(size):
                file.write(str(getValWei(alpha,beta)))
                if(i == size - 1):
                    pass
                else:
                    file.write('\n')
    elif dist == "exponential":
        with open(file, 'w') as file:
            for i in range(size):
                file.write(str(getValXP(mean)))
                if(i == size - 1):
                    pass
                else:
                    file.write('\n')
            

if __name__ == "__main__":
    main()
