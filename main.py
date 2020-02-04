from classes.Buffer import Buffer

def main():
    b = Buffer()
    b.putItem("hello")
    print(""+b.getItem())
    print(str(b.putItem("hi")) +" "+str(b.putItem("hi")) + " " + str(b.putItem("hi")))
 
if __name__ == "__main__":
    main()