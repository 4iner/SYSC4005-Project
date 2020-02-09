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
import time

from classes.Shared import Shared


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

    t1 = time.time()
    # start threads
    i1.start()
    i2.start()
    w1.start()
    w2.start()
    w3.start()
    ind.start()
    ind.join()

    tf = Shared.timeFactor
    t2 = time.time()
    tim = t2-t1
    th2 = tim * tf
    th= w1.counter  /  th2
    th1= w2.counter  /  th2
    th3= w3.counter  /  th2

    Shared.log("throughput time for workstation1: "+str(th*60)+" p1 per hour")
    Shared.log("throughput time for workstation2: "+str(th1*60)+" p2 per hour")
    Shared.log("throughput time for workstation3: "+str(th3*60)+ " p3 per hour")

    Shared.log("idle time for inspector1: "+ str(bb.blockedTime * tf)+ " minutes")
    Shared.log("idle time for inspector2: " +str(b4.blockedTime*tf + b5.blockedTime*tf)+ " minutes")



if __name__ == "__main__":
    main()
