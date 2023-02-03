import dbConnection

class Summary:
    def __init__(self):
        self.Db=dbConnection.get_connection()
        self.Cursor=dbConnection.get_cursor(self.Db)


    def filterOut(self,name,test):
        cursor=self.Cursor
        if name =="All" and test=="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and services.ServiceName=%s;"
            cursor.execute(query,(test,))

        elif name!="All" and test !="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and services.ServiceName=%s and CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ')=%s;"
            cursor.execute(query,(test,name))

        elif name!='All' and test=="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ')=%s;"
            cursor.execute(query,(test,))

        elif name=="All" and test !="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and services.ServiceName=%s;"
            cursor.execute(query,(test,))

        result=cursor.fetchall()
        return result

    def filter_byTest(self,name,test):
        cursor=self.Cursor
        if name =="All" and test=="All":
            print('a')
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and services.ServiceName=%s;"
            cursor.execute(query,(test,))
        elif name!="All" and test !="All":
            print('b')
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and services.ServiceName=%s and CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ')=%s;"
            cursor.execute(query,(test,name))

        result=cursor.fetchall()
        return result

    def filter_byName(self,name,test):
        cursor=self.Cursor
        if test =="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and tests.MedTechID=medtechs.id and CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ')=%s;"
            cursor.execute(query,(name,))

        else:
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and tests.MedTechID=medtechs.id and CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ')=%s and services.ServiceName=%s;"
            cursor.execute(query,(name,test))
        result=cursor.fetchall()
        return result



