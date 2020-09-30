
## CREATING THE main class
class hotelfarecal:
    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,
                 name='',address='',cindate='',coutdate='',rno=101):
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
        self.name=input(" Enter your name:")
        self.address=input(" Enter your address:")
        self.cindate=input(" Enter yout check in date:")
        self.coutdate=input(" Enter your checkout date: ")
        print("Your room number:",self.rno," ")
