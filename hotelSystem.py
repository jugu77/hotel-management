import random
from datetime import datetime
## CREATING THE main class
class hotelfarecal:
    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,
                 name='',address='',email='',phone='',rno=0):
        print(" ******** WELCOME TO HOTEL COLORADO ********")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.email=email
        self.phone=phone
        #self.cindate=cindate
        #self.coutdate=coutdate
        self.rno=rno

    ## Creating the different options
    def inputdata(self):
        # self.rno = random.randint(100,3000)
        self.name=input("Enter your name: ")
        self.address=input("Enter your address: ")
        self.email=input("Enter Email: ")
        self.phone=input('Enter Phone: ')
        #self.cindate=input(" Enter yout check in date (M/D/Y): ")
        #self.coutdate=input(" Enter your checkout date (M/D/Y): ")
        # print("Your room number:",self.rno," ")

    ## Creating the room rate calcualtion
    def roomrate(self):

        print("We have the following room for you:-")
        print("1. Room Type A ----> $1300 Per Night\-")
        print("2. Room Type B ----> $1000 Per Night\-")
        print("3. Room Type C ----> $700 Per Night\-")
        print("4. Room Type D ----> $400 Per Night\-")

        roomChoice = int(input("Enter the room choice-> "))
        #numberOfNights = int(input("How Many Nights Did You Stay: "))

        ## Creates a varible to take the checkin and checkout dates:
        checkIn = input("Check-in Date [DD/MM/YY]: ")
        checkOut = input("Check-out Date [DD/MM/YY]: ")
        ## Converts variables above to a datetime class to process arithmetic
        check_In = datetime.strptime(checkIn, '%d/%m/%y')
        check_Out = datetime.strptime(checkOut, '%d/%m/%y')

        ## If statement to calculate the number of nights/day a guets stayed
        if (check_In.month == check_Out.month):
            numberOfNights = check_Out.day - check_In.day
            #print("Number of Nights: " + str(numberOfNights))
        elif (check_In.month != check_Out.month):
            dayin = datetime.date(check_In)
            dayout = datetime.date(check_Out)
            numberOfNights = dayout - dayin
            #print("Number of Nights: " + str(numberOfNights))
        else:
            print("Enter a value")
        print("Number of Nights: " + str(numberOfNights))

        if(roomChoice == 1):
            self.rno = random.randint(3000,4000)
            print("Your Room Was a Type A")
            print("Your Room Number Is: ",self.rno," ")
            self.s = 1300 * numberOfNights
        elif(roomChoice == 2):
            self.rno = random.randint(2000, 3000)
            print("Your Room Was a Type B")
            print("Your Room Number Is: ", self.rno, " ")
            self.s = 1000 * numberOfNights
        elif (roomChoice == 3):
            self.rno = random.randint(1100, 2000)
            print("Your Room Was a Type C")
            print("Your Room Number Is: ", self.rno, " ")
            self.s = 700 * numberOfNights
        elif (roomChoice == 4):
            self.rno = random.randint(100, 1100)
            print("Your Room Was a Type D")
            print("Your Room Number Is: ", self.rno, " ")
            self.s = 400 * numberOfNights
        else:
            print("Please Enter a Room")
        print("Your Room Rate is: $",self.s," ")

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
            print ("Total Food Cost: $",self.r," ")

    # Creating the Laundry Bill
    def laundryBill(self):
        print("*****LAUNDRY SERVICE*****")
        print("1. Shorts--->$5","2. Pants--->$7","3. Shirt--->$6","4. Jeans--->$8","5. Suit--->$25","6. Exit")

        while (1):
            e = int(input("Enter your choice: "))
            if (e == 1):
                f = int(input("Enter the quantity: "))
                self.t = self.t + 3 * f
            elif (e == 2):
                f = int(input("Enter the quantity: "))
                self.t = self.t + 7 * f
            elif (e == 3):
                f = int(input("Enter the quantity: "))
                self.t = self.t + 6 * f
            elif (e == 4):
                f = int(input("Enter the quantity: "))
                self.t = self.t + 8 * f
            elif (e == 5):
                f = int(input("Enter the quantity: "))
                self.t = self.t + 25 * f
            elif (e == 6):
                break
            else:
                print("Enter a Valid Option")
            print("Total Laundry Cost $",self.t," ")

    # Creating the Confference Room Rental
    def confRent(self):
        print("*****CONFERENCE ROOM MENU******")
        print("1. 10 People--->$40","2. 30 People--->$65","3. 60 People--->$120","4. 100+ People--->$200","5. Exit")

        while (1):
            g = int(input("Enter Choice: "))

            if (g == 1):
                h = int(input("Number of Hours: "))
                self.p = self.p + 40 * h
            elif (g == 2):
                h = int(input("Number of Hours: "))
                self.p = self.p + 65 * h
            elif (g == 3):
                h = int(input("Number of Hours: "))
                self.p = self.p + 120 * h
            elif (g == 4):
                h = int(input("Number of Hours: "))
                self.p = self.p + 200 * h
            elif (g == 5):
                break
            else:
                print("Invalid Option")
            print("Total Conference Bill = $",self.p," ")

## PRITNING THE HOTEL BILL ####
    def display(self):
        print("*****HOTEL BILL******")
        print("Customer Name: ",self.name)
        print("Customer Address: ",self.address)
        print("Email Address: ",self.email)
        print("Phone Number: ",self.phone)
        print("Room No: ",self.rno)
        print('-'*40)
        print("Your Room Rate: $",self.s)
        print("Your Food Bill: $",self.r)
        print("Your Laundry Bill: $",self.t)
        print("Your Conference Bill: $",self.p)

        #Calculate Room Rate with tax
        tax = (.029 * self.s)
        self.rt = self.s + tax
        # Calculates additional charges on services
        self.a = self.r + self.t + self.p
        print('-'*40)
        print("Your Subtotal Bill: $",self.rt)
        print("Additional Services Charges: $",self.a)
        print('-' * 40)
        print("Grand Total: $",self.rt+self.a," ")
        print("<------------------------- END --------------------->")


def main():
    a = hotelfarecal()
    while (1):
        print("1. Enter Customer Data ")
        print("2. Calculate Room Rate ")
        print("3. Calculate Restaurant Bill ")
        print("4. Calculate Laundry Bill ")
        print("5. Calculate Conference Bill ")
        print("6. Show Total Bill")
        print("7. EXIT")

        b = int(input("Enter Your Choice: "))
        if (b == 1):
            a.inputdata()
        if (b == 2):
            a.roomrate()
        if (b == 3):
            a.restBill()
        if (b == 4):
            a.laundryBill()
        if (b == 5):
            a.confRent()
        if (b == 6):
            a.display()
        if (b == 7):
            quit()
main()









