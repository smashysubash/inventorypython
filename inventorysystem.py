import sys;
import sqlite3; 
import re  


conn=sqlite3.connect("inventory.db")
cur=conn.cursor()

class item:
     
    def __init__(self,itemNo,itemName,itemQty,itemMRP,itemRate):
      
        self.__itemName=itemName
        self.__itemNo=itemNo
        self.__itemQty=itemQty
        self.__itemMRP=itemMRP
        self.__itemRate=itemRate
        
    def getitemname(self):
        return self.__itemName
    
    def getitemno(self):
        return self.__itemNo

    def getitemmrp(self):
        return self.__itemMRP

    def getitemrate(self):
        return self.__itemRate
    
    def getitemQty(self):
        return self.__itemQty

    # def getemail(self):
    #     return self.__email

    # def setname(self, value):
    #     self.__name = value

    # def settelephoneno(self, value):
    #     self.__telephoneno = value

    # def setemail(self, value):
    #     self.__email = value

    # def getpersontype(self):
    #     return self.__persontype
    
    # def setpersontype(self,value):
    #     self.__persontype=value

    def validateinteger(self):
            
        if(self.__itemQty.isnumeric() and self.__itemNo.isnumeric() and self.__itemRate.isnumeric() and self.__itemMRP.isnumeric()):
            return True
        else:
            print("Enter a valid input")
            return False



class start:
    n=0
    ch='n'
    def initial(self):
        print("******************************")
        print(" Inventory Management System")
        print("******************************")
        print("1. Add an Item")
        print("2. Sell an item")
        print("3. view item list")
        print("4. Exit")
        n=int(input("Select your choice"))
        if n==1:
            self.additem()
        elif n==2:
            self.sellitem()
        elif n==3:
            self.viewitem()
        elif n==4:
            print("Thank You!!!")
            sys.exit
           
    
    def additem(self):
        try:

            # conn.execute('''CREATE TABLE item (ItemNo INT NOT NULL, NAME  TEXT NOT NULL,Quantity int  NOT NULL,MRP INT NOT NULL,Rate INT NOT NULL);''')

            #conn.execute('''CREATE TABLE professor (NAME  TEXT NOT NULL,telephoneno INT NOT NULL,email text NOT NULL,pid int,dept  text,desig text,basic real, sal real);''')
            # conn.execute('''drop table item''')

            #conn.execute('''CREATE TABLE address (addressline text NOT NULL,city  TEXT    NOT NULL,zipcode INT     NOT NULL,state         text, customerid  int);''')
            itemNo=(input("Enter item no. "))           
            itemName=input("Enter item Name ")
            itemQty = (input("Enter the quantity"))
            itemMRP=(input("Enter item MRP "))
            itemRate=input("Enter item Rate ")
            itemobj=item(itemNo,itemName,itemQty,itemMRP,itemRate)

            if(itemobj.validateinteger()):     
    #           # insert record in item table
                conn.execute("""insert into item values (?,?,?,?,?)""",(itemobj.getitemno(),itemobj.getitemname(),itemobj.getitemQty(),itemobj.getitemmrp(),itemobj.getitemrate()))  
            else:
                print("Invalid Input")
                start.gotooptions(self)  
        except sqlite3.DatabaseError as e:
            print("Error details: ",e)
        finally:
            conn.commit()
            
  
    
    def viewitem(self):
        cur.execute("select * from item")
        for n in cur.fetchall():
            print(n) 

    # def viewallprofessor(self):
    #     cur.execute("select * 1from Professor")
    #     for n in cur.fetchall():
    #         print(n)  

    def gotooptions(self):
        ch=input("Do you wish to continue(y/n)")
        if(ch=='y' or ch=='Y'):
            start.initial(self)



obj=start()
obj.initial()
obj.gotooptions()

