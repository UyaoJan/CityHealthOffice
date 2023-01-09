from tkinter import messagebox
import dbConnection,random
class Employee:
    def __init__(self,id,username,password,fname,lname,age,address,role,url):
        self.Db=dbConnection.get_connection()
        self.Cursor=dbConnection.get_cursor(self.Db)

        if id==None: 
            self.id=self.generateID()
        else: 
            self.id=id
        self.username=username
        self.password=password
        self.fname=fname
        self.lname=lname
        self.age=age
        self.address=address
        self.role=role
        self.url=url

    def register(self):
        query="INSERT INTO medtechs VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(self.id,self.fname,self.lname,self.role,self.age,self.address,self.username,self.password,self.url)
        self.Cursor.execute(query,values)
        self.Db.commit()

    @staticmethod
    def getAllEmployees():
        query="SELECT * FROM medtechs"
        conn=dbConnection.get_connection()
        cursor=dbConnection.get_cursor(conn)
        cursor.execute(query)
        result =cursor.fetchall()
        return result

    @staticmethod 
    def deleteEmployee(id):
        query_del="DELETE FROM medtechs WHERE id=%s"
        conn=dbConnection.get_connection()
        cursor=dbConnection.get_cursor(conn)
        cursor.execute(query_del,(id,))
        conn.commit()


    @staticmethod
    def findAccount(id):
        query_find="SELECT * FROM medtechs WHERE id=%s"
        conn=dbConnection.get_connection()
        cursor=dbConnection.get_cursor(conn)
        cursor.execute(query_find,(id,))
        acc = cursor.fetchone()
        return acc

    @staticmethod
    def login(uname,passwd):
        query_find="SELECT * FROM medtechs WHERE username=%s and password=%s"
        conn=dbConnection.get_connection()
        cursor=dbConnection.get_cursor(conn)
        cursor.execute(query_find,(uname,passwd))
        acc = cursor.fetchone()
        if acc:
            return Employee(acc[0],uname,passwd,acc[1],acc[2],acc[4],acc[5],acc[3],None)
        
        else: 
            messagebox.showerror("Credentials Not Found","Username and Password do not Match")

    @staticmethod 
    def editAccount(account):
        conn=dbConnection.get_connection()
        cursor=dbConnection.get_cursor(conn)
        query="UPDATE medtechs SET FirstName=%s,LastName=%s,Role=%s,age=%s,address=%s,username=%s,password=%s WHERE id=%s"

        values=(account[1],account[2],account[3],account[4],account[5],account[6],account[7],account[0])
        cursor.execute(query,values)
        conn.commit()


    @staticmethod
    def generateID():
        ID = random.randint(1, 9999)
        conn=dbConnection.get_connection()
        cursor=dbConnection.get_cursor(conn)
        query="SELECT id FROM medtechs"
        cursor.execute(query)
        result=cursor.fetchall()

        for i in result:
            if ID == i :
                ID = random.randint(1, 9999)
                break
            else:
                continue
        return ID

    @staticmethod
    def addNewClient(user,client,tests,date):
        print("Filing User",user.fname)
        print("Client Info ",client)
        print("Requested Tests ", tests)
        print("Requested at ", date)
        
        client_insert="INSERT INTO clients VALUES(%s, %s, %s, %s, %s, %s)"
        user.Cursor.execute(client_insert, client)

        test_insert="INSERT INTO tests (ClientID, MedTechID,status,date,ServiceID) VALUES(%s, %s, %s, %s, %s)"
        get_serviceID_query="SELECT ServiceID FROM services WHERE ServiceName LIKE %s LIMIT 1"
        # user.Cursor.execute(get_serviceID_query,(tests,))
        for test in tests:
            user.Cursor.execute(get_serviceID_query,(test,))
            ServiceID=user.Cursor.fetchone()
            user.Cursor.execute(test_insert,(client[0],user.id, "Pending", date, ServiceID[0]))

        user.Db.commit()