import random
## CREATING THE main class
class hotelfarecal:
    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,
                 name='',address='',cindate='',coutdate='',rno=0):
        print(" ******** WELCOME TO HOTEL COLORADO")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno

    ## Creating the different options
    def inputdata(self):
        self.rno = random.randint(100,3000)
        self.name=input(" Enter your name:")
        self.address=input(" Enter your address:")
        self.cindate=input(" Enter yout check in date:")
        self.coutdate=input(" Enter your checkout date: ")
        print("Your room number:",self.rno," ")

    ## Creating the room rate calcualtion
    def roomrate(self):

        print("We have the following room for you:-")
        print("1. Room Type A ----> $1300 Per Night\-")
        print("2. Room Type B ----> $1000 Per Night\-")
        print("3. Room Type C ----> $700 Per Night\-")
        print("4. Room Type D ----> $400 Per Night\-")

        roomChoice = int(input("Enter the room choice-> "))
        numberOfNights = int(input("How Many Nights Did You Stay: "))

        if(roomChoice == 1):
            print("Your Room Was a Type A")
            self.s = 1300 * numberOfNights
        elif(roomChoice == 2):
            print("Your Room Was a Type B")
            self.s = 1000 * numberOfNights
        elif (roomChoice == 3):
            print("Your Room Was a Type C")
            self.s = 700 * numberOfNights
        elif (roomChoice == 4):
            print("Your Room Was a Type D")
            self.s = 400 * numberOfNights
        else:
            print("Please Enter a Room")
        print("Your Room Rate is =",self.s," ")

    ## Creating The Restaurant Bill
    def restBill(self):
        print("******RESTAURANT MENU*******")
        print("1. Wine--->$8","2. Beer--->$5","3. Coffee--->$2","4. Breakfast Combo--->$13","5. Lunch Combo--->$16",
              "6. Dinner--->$19","7. Exit")

        while (1):
            c = int(input("Enter your choice: "))

            if(c == 1):
                d = int(input("Enter the Quantity: "))
                self.r = self.r + 8 * d
            elif (c == 2):
                d = int(input("Enter the Quantity: "))
                self.r = self.r + 5 * d
            elif (c == 3):
                d = int(input("Enter the Quantity: "))
                self.r = self.r + 2 * d
            elif (c == 4):
                d = int(input("Enter the Quantity: "))
                self.r = self.r + 13 * d
            elif (c == 5):
                d = int(input("Enter the Quantity: "))
                self.r = self.r + 16 * d
            elif (c == 6):
                d = int(input("Enter the Quantity: "))
                self.r = self.r + 19 * d
            elif (c == 7):
                break
            else:
                print("Invalid Option")
            print ("Total Food Cost = $",self.r," ")










    def display(self):
        print("*****HOTEL BILL******")
        print("Customer Detail: ")
        print("Customer Name:",self.name)
        print("Customer Address:",self.address)
        print("Check In Date",self.cindate)
        print("Check Out Date",self.cindate)
        print("Room no.:",self.rno)
        print("Your Room Rate is:",self.s)
        print("Your Food Bill is:",self.r)

        self.rt = self.s + self.r

        print("Your Subtotal Bill is: ",self.rt)









def main():
    a = hotelfarecal()
    while (1):
        print("1. Enter Customer Data")
        print("2. Calculate Room Rate")
        print("3. Calculate Restaurant Bill")
        print("4. Show Total Bill")
        print("5. EXIT")

        b = int(input("Enter Your Choice:"))
        if (b == 1):
            a.inputdata()
        if (b == 2):
            a.roomrate()
        if (b == 3):
            a.restBill()
        if (b == 4):
            a.display()
        if (b == 5):
            quit()
main()









