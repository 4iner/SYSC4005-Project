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

    def run(self):
        while True:
            # checks inspector 1 and 2 if they're done
            for thread in range(0, 1):
                if self.threads[thread].indicator:
                    self.isdone = True
                    break
            # if done, get out of the loop
            if self.isdone:
                break
        # print out results
        time.sleep(1)
        Shared.log("Manufacturer finished.")
        for thread in range(2, 5):
            Shared.log("Workstation {} made {} P{} Product(s)".format(thread - 1, self.threads[thread].counter, thread - 1))
        self.blackbox.roundCheck()
