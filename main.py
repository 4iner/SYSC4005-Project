from classes.Buffer import Buffer
from classes.Component import Component
from classes.Inspector1 import Inspector1
from classes.Inspector2 import Inspector2
from classes.Workstation1 import Workstation1
from classes.Workstation2 import Workstation2
from classes.Workstation3 import Workstation3


def main():
    b1 = Buffer()
    b2 = Buffer()
    b3 = Buffer()
    i1 = Inspector1([Component.C1], [b1, b2, b3])
    i2 = Inspector2([Component.C2, Component.C3], b2, b3)
    w1 = Workstation1(b1)
    w2 = Workstation2(b1, b2)
    w3 = Workstation3(b1, b3)
    i1.start()
    i2.start()
    w1.start()
    w2.start()
    w3.start()

if __name__ == "__main__":
    main()
