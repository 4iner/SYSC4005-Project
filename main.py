from classes.Buffer import Buffer
from classes.Workstation1 import Workstation1
def main():
    b = Buffer()
    b.putItem("hi")
    b.putItem("hs")
    w = Workstation1(b)
    w.start()
 
if __name__ == "__main__":
    main()
