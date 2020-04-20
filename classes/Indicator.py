import threading
import time

from classes.Shared import Shared

# this indicator class checks if any inspectors has completed their service time
class Indicator(threading.Thread):

    def __init__(self, threads, blackbox):
        super(Indicator, self).__init__(name="Indicator")
        self.isdone = None
        self.threads = threads
        self.blackbox = blackbox
        self.string = ""

    def run(self):
        for x in range(22):
            

            for thread in range(2, 5):
                self.threads[thread].counter = 0
            self.threads[0].bufferbox.blockedTime = 0
            self.threads[1].buffer2.blockedTime = 0
            self.threads[1].buffer3.blockedTime = 0
            self.threads[0].bufferbox.bt = time.time()
            self.threads[1].buffer2.bt = time.time()
            self.threads[1].buffer3.bt = time.time()
            t1 = time.time();
            tf = Shared.timeFactor

            time.sleep(tf/20)
            t2 = time.time()
            tim = t2-t1
            th2 = tim * tf
            th= self.threads[2].counter  /  th2
            th1= self.threads[3].counter  /  th2
            th3= self.threads[4].counter  /  th2

            self.string += ("%f %f %f %f %f\n" % (th*60, th1*60, th3*60, (self.threads[0].bufferbox.blockedTime)/th2 * tf, (self.threads[1].buffer2.blockedTime*tf + self.threads[1].buffer3.blockedTime*tf)/th2))

        while True:
            # checks inspector 1 and 2 if they're done
            for thread in range(0, 1):
                if self.threads[thread].indicator:
                    self.isdone = True
                    break
            # if done, get out of the loop
            if self.isdone:
                break

        #array [w1,w2,w3,idle1,idle2]
        # print out results
        time.sleep(1)
        Shared.log("Manufacturer finished.")
        for thread in range(2, 5):
            Shared.log("Workstation {} made {} P{} Product(s)".format(thread - 1, self.threads[thread].counter, thread - 1))
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("\t\t\tReplication Data")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print()
        print(self.string)
        self.blackbox.endTime = time.time()
        self.blackbox.roundCheck()