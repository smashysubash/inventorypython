import sys;
import sqlite3;   


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

    def validateinteger(self):
            
        if(self.__itemQty.isnumeric() and self.__itemNo.isnumeric() and self.__itemRate.isnumeric() and self.__itemMRP.isnumeric()):
            return True
        else:
            print("Enter a valid input")
            return False
        
    def validatetable(self):
        cur.execute("select itemNo from item")    
        for n in cur.fetchall():
            if(n[0]==int(self.__itemNo)):
                return False
        return True 


class start:
    n=0
    ch='n'
    def initial(self):
        print("******************************")
        print(" Inventory Management System")
        print("******************************")
        print("1. Add an Item")
        print("2. Update an item")
        print("3. Delete an item")
        print("4. view item list")
        print("5. Exit")
        n=int(input("Select your choice "))
        if n==1:
            self.additem()
        elif n==2:
            self.updateitem()
        elif n==3:
            self.deleteitem()
        elif n==4:
            self.viewitem()
        elif n==5:
            print("Thank You!!!")
            sys.exit
           
    
    def additem(self):
        try:
            conn.execute("CREATE TABLE if not exists item (ItemNo INT NOT NULL, NAME VARCHAR(20) NOT NULL, Quantity int NOT NULL, MRP INT NOT NULL, Rate INT NOT NULL)")

            itemNo=(input("Enter item no. "))           
            itemName=input("Enter item Name ")
            itemQty = (input("Enter the quantity"))
            itemMRP=(input("Enter item MRP "))
            itemRate=input("Enter item Rate ")
            itemobj=item(itemNo,itemName,itemQty,itemMRP,itemRate)

            if(itemobj.validateinteger() and itemobj.validatetable()):     
    #           # insert record in item table
                conn.execute("""insert into item values (?,?,?,?,?)""",(itemobj.getitemno(),itemobj.getitemname(),itemobj.getitemQty(),itemobj.getitemmrp(),itemobj.getitemrate()))  
            else:
                print("Invalid Input")
        except sqlite3.DatabaseError as e:
            print("Error details: ",e)
        finally:
            conn.commit()
        start.gotooptions(self)  
        
    def viewitem(self):
        try:
            cur.execute("select * from item")    
            for n in cur.fetchall():
                print(n) 
            
        except sqlite3.DatabaseError as e:
            print("Error details: ",e)
        obj.gotooptions()



    def updateitem(self):
        try:
            itemno=input("Enter item no. ")
            itemqty=input("Enter the updatable quantity ")
            if(itemqty.isnumeric() and itemno.isnumeric()):
                conn.execute("""update item set Quantity= ? where itemNo= ? """,(itemqty,itemno) )
            else:
                print("Invalid Input")
                start.gotooptions(self)
            
        except sqlite3.DatabaseError as e:
            print("Error details: ",e)
        finally:
            conn.commit()

    def deleteitem(self):
        try:
            itemno=input("Enter item no. ")
            if(itemno.isnumeric()):
                conn.execute("""delete from item where itemNo= ? """,[itemno] )
            else:
                print("Invalid Input")
                start.gotooptions(self)
                

        except sqlite3.DatabaseError as e:
            print("Error details: ",e)
        finally:
            conn.commit()            

    def gotooptions(self):
        ch=input("Do you wish to continue(y/n)")
        if(ch=='y' or ch=='Y'):
            start.initial(self)

    # def checktable(){
    #     if(SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}')
    # }

obj=start()
obj.initial()
obj.gotooptions()
