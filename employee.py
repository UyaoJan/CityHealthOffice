from tkinter import messagebox
import random
import dbConnection,random
from datetime import date
class Employee:
    def __init__(self,id,username,password,fname,lname,age,address,role,dept,url):
        self.Db=dbConnection.get_connection()
        self.Cursor=dbConnection.get_cursor(self.Db)

        if id==None: 
            self.id=self.generateID()
        else: 
            self.id=id
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
        self.dept=dept
        self.url=url

    def return_role(self):
        return self.role

    def return_dept(self):
        return self.dept

    def get_test_id(self,test):
        cursor=self.Cursor
        query="SELECT ServiceID FROM services WHERE ServiceName=%s"
        cursor.execute(query,(test,))
        res=cursor.fetchone()
        return res
    
    def get_test_price(self,serviceid):
        cursor=self.Cursor
        query="SELECT Cost FROM services WHERE ServiceID=%s"
        cursor.execute(query,(serviceid,))
        res=cursor.fetchone()
        return res

    def get_tests_id(self,client,service):
        cursor=self.Cursor
        query="SELECT id FROM tests WHERE ClientID=%s AND ServiceID=%s"
        cursor.execute(query,(client,service))
        result=cursor.fetchone()
        return result

    def getClientTestRequests(self,clientID, testID):
        cursor=self.Cursor
        query="SELECT ServiceID FROM tests WHERE ServiceID=%s and ClientID=%s;"
        if isinstance(clientID, int):
            cursor.execute(query,(testID[0],clientID))
        elif isinstance(clientID, tuple):
            cursor.execute(query,(testID[0],clientID[0]))
        result=cursor.fetchall()
        rows=len(result)
        if rows ==0:
            return None
        else:
            return result


    def save_to_summary(self,total,idd,clientID):
        id=random.randint(0,999)
        today=date.today()
        cursor=self.Cursor
        id_query="SELECT id FROM summary"
        cursor.execute(id_query)
        id_res=cursor.fetchall()
        for i in id_res:
            if i==id:
                id=random.random(0,999)
        query="INSERT INTO summary (id,ClientID,test_id,totalcost,dateFinished) VALUES(%s,%s,%s,%s,%s)"
        values=(id,clientID,idd,total,today)
        cursor.execute(query,values)
        self.Db.commit()

        return id

    def update_summaryID_test(self,id,client,test):
        cursor=self.Cursor
        query="UPDATE tests SET summary_id=%s WHERE ClientID=%s AND ServiceID=%s"
        values=(id,client,test)
        cursor.execute(query,values)
        self.Db.commit()

    def getAllClient_Done(self):
        cursor=self.Cursor
        # query="SELECT clients.ClientID,clients.Name,services.ServiceName,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id;"
        query="SELECT clients.ClientID,clients.Name,clients.gender,services.ServiceName,clients.age,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID;"
        cursor.execute(query)
        result=cursor.fetchall()
        return result

    def register(self):
        query="INSERT INTO medtechs VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(self.id,self.fname,self.lname,self.role,self.dept,self.age,self.address,self.username,self.password,self.url)
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

    def getclientTests(self,id):
        query="SELECT tests.id,clients.ClientID,clients.Name, services.ServiceName FROM services,tests,clients WHERE services.ServiceID = tests.ServiceID AND clients.ClientID=tests.ClientID AND clients.ClientID=%s AND NOT tests.status ='done' AND NOT tests.ServiceID=15;"
        cursor=self.Cursor
        cursor.execute(query,(id,))
        result=cursor.fetchall()
        return result

    def markXray_as_done(self,id):
        query2="UPDATE tests SET status='done' WHERE id =%s"
        cursor=self.Cursor
        cursor.execute(query2,(id,))
        self.Db.commit()

    def markTest_as_done(self,id):
        query="UPDATE tests SET status='done' WHERE id =%s"
        query2="UPDATE tests SET MedTechId=%s WHERE id =%s"
        cursor=self.Cursor
        cursor.execute(query,(id,))
        cursor.execute(query2,(self.id,id))
        self.Db.commit()

    def getClient_name_Xray(self,name):
        query="SELECT clients.ClientID, clients.Name, clients.age,clients.gender,clients.bday,clients.address,tests.id FROM clients,tests WHERE clients.Name=%s AND clients.ClientID = tests.ClientID AND tests.ServiceID=15 AND tests.status='Pending' "
        cursor=self.Cursor
        cursor.execute(query,(name,))
        result=cursor.fetchone()
        return result
        

    def getClient_name(self,name):
        query="SELECT clients.ClientID, clients.Name, clients.age,clients.gender,clients.bday,clients.address,tests.id FROM clients,tests WHERE clients.Name=%s AND clients.ClientID = tests.ClientID AND NOT tests.ServiceID=15 AND NOT tests.status='done' LIMIT 1 ;"
        cursor=self.Cursor
        cursor.execute(query,(name,))
        result=cursor.fetchone()
        return result

    def getAllTest(self):
        query="SELECT ServiceName FROM services"
        cursor=self.Cursor
        cursor.execute(query)
        result=cursor.fetchall()
        return result

    def getClient(self,id):
        query="SELECT * FROM clients WHERE ClientID=%s LIMIT 1"
        cursor=self.Cursor
        cursor.execute(query,(id,))
        result=cursor.fetchone()
        return result

    def getClients_all(self):
        # query="SELECT clients.ClientID, clients.Name,clients.age,clients.gender,clients.bday,clients.address, services.ServiceName FROM clients, tests, services WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID;"
        # query="SELECT clients.ClientID, clients.Name,clients.age,clients.gender,clients.bday,clients.address FROM clients;"
        # query="SELECT clients.ClientID, clients.Name,clients.age,clients.gender,clients.bday,clients.address FROM clients,tests WHERE tests.ClientID=clients.ClientID AND tests.status='Pending'"
        query="SELECT clients.ClientID, clients.Name,clients.age,clients.gender,clients.bday,clients.address FROM clients,tests WHERE tests.ClientID=clients.ClientID AND tests.status='Pending' GROUP BY clients.ClientID"
        cursor=self.Cursor
        cursor.execute(query)
        result=cursor.fetchall()
        return result

    def getClients_lab(self):
        query="SELECT clients.ClientID, clients.Name,clients.age,clients.gender,clients.bday,clients.address, services.ServiceName FROM clients, tests, services WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.ServiceID!=15;"
        cursor=self.Cursor
        cursor.execute(query)
        result=cursor.fetchall()
        return result

    def getClients_Xray(self):
        query="SELECT clients.ClientID, clients.Name,clients.age,clients.gender,clients.bday,clients.address, services.ServiceName, tests.id FROM clients, tests, services WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.ServiceID=15;"
        cursor=self.Cursor
        cursor.execute(query)
        result=cursor.fetchall()
        return result

    def generateClient_ORNumber(self):
        num=random.randint(0,99999999)
        query="SELECT id from summary"
        cursor=self.Cursor
        cursor.execute(query)
        result=cursor.fetchall()
        for number in result:
            if number==num:
                num=random.randint(0,99999999)
        return num

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
            return Employee(acc[0],uname,passwd,acc[1],acc[2],acc[5],acc[6],acc[3],acc[4],None)
        
        else: 
            return 0

    @staticmethod 
    def editAccount(account):
        conn=dbConnection.get_connection()
        cursor=dbConnection.get_cursor(conn)
        query="UPDATE medtechs SET FirstName=%s,LastName=%s,Role=%s,department=%s,age=%s,address=%s,username=%s,password=%s WHERE id=%s"

        values=(account[1],account[2],account[3],account[4],account[5],account[6],account[7],account[8],account[0])
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
        client_insert="INSERT INTO clients VALUES(%s, %s, %s, %s, %s, %s)"
        user.Cursor.execute(client_insert, client)
        test_insert="INSERT INTO tests (ClientID, status,date,ServiceID) VALUES(%s, %s, %s, %s)"
        get_serviceID_query="SELECT ServiceID FROM services WHERE ServiceName LIKE %s LIMIT 1"
        for test in tests:
            user.Cursor.execute(get_serviceID_query,(test,))
            ServiceID=user.Cursor.fetchone()
            user.Cursor.execute(test_insert,(client[0], "Pending", date, ServiceID[0]))

        user.Db.commit()

    def addXrayFinding(self,title,body):
        add_impression_query="insert into xray_details (findings_title,findings_body) values(%s, %s)"
        cursor=self.Cursor
        cursor.execute(add_impression_query, (title,body))
        self.Db.commit()

    def getAllXrayFinding(self):
        query="SELECT * FROM xray_details"
        cursor=self.Cursor
        cursor.execute(query)
        result=cursor.fetchall()
        return result

    def getXrayFindingDetails(self,title):
        query="SELECT findings_title, findings_body FROM xray_details WHERE findings_title LIKE %s LIMIT 1"
        cursor=self.Cursor
        cursor.execute(query,(title,))
        result=cursor.fetchone()
        return result