import dbConnection

class Summary:
    def __init__(self):
        self.Db=dbConnection.get_connection()
        self.Cursor=dbConnection.get_cursor(self.Db)


    def filterOut(self,name,test):
        cursor=self.Cursor
        if name =="All" and test=="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID"
            cursor.execute(query)

        elif name!="All" and test !="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and services.ServiceName=%s and CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ')=%s;"
            cursor.execute(query,(test,name))

        elif name!='All' and test=="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ')=%s;"
            cursor.execute(query,(name,))

        elif name=="All" and test !="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and services.ServiceName=%s;"
            cursor.execute(query,(test,))

        result=cursor.fetchall()
        return result

    def filterYearly(self,year): 
        cursor=self.Cursor
        query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and YEAR(summary.dateFinished)=%s"
        cursor.execute(query,(year,))
        result=cursor.fetchall()
        return result

    def filterYearlyTest(self,year, name,test):
        cursor=self.Cursor
        if name =="All" and test=="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and YEAR(summary.dateFinished)=%s"
            cursor.execute(query,(year,))
        elif name!="All" and test !="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and YEAR(summary.dateFinished)=%s and services.ServiceName=%s and CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ')=%s"
            cursor.execute(query,(year,test,name))
        elif name!='All' and test=="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and YEAR(summary.dateFinished)=%s and CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ')=%s"
            cursor.execute(query,(year,name))
        elif name=="All" and test !="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and YEAR(summary.dateFinished)=%s and services.ServiceName=%s"
            cursor.execute(query,(year,test))

        result=cursor.fetchall()
        return result

    def filterMonthlyTest(self, dateFROM,dateTo, name, test):
        cursor=self.Cursor
        # query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and summary.dateFinished>=%s and summary.dateFinished<=%s"   
        # cursor.execute(query,(dateFROM,dateTo))
        if name =="All" and test=="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and summary.dateFinished>=%s and summary.dateFinished<=%s"
            cursor.execute(query,(dateFROM,dateTo))

        elif name!="All" and test !="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and services.ServiceName=%s and CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ')=%s and summary.dateFinished>=%s and summary.dateFinished<=%s;"
            cursor.execute(query,(test,name,dateFROM,dateTo))

        elif name!='All' and test=="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ')=%s and summary.dateFinished>=%s and summary.dateFinished<=%s;"
            cursor.execute(query,(name,dateFROM,dateTo))

        elif name=="All" and test !="All":
            query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and services.ServiceName=%s and summary.dateFinished>=%s and summary.dateFinished<=%s;"
            cursor.execute(query,(test,dateFROM,dateTo))

        result=cursor.fetchall()

        return result

    def filterMonthly(self, dateFROM,dateTo):
        cursor=self.Cursor
        query="SELECT clients.ClientID,clients.Name,services.ServiceName,tests.date,summary.dateFinished,CONCAT(medtechs.FirstName,' ',medtechs.LastName,' ') as medtech_name FROM clients,services,medtechs,tests,summary WHERE clients.ClientID=tests.ClientID AND tests.ServiceID=services.ServiceID AND tests.status='done' and tests.MedTechID=medtechs.id and summary.ClientID=tests.ClientID and summary.dateFinished>=%s and summary.dateFinished<=%s"   
        cursor.execute(query,(dateFROM,dateTo))
        result=cursor.fetchall()
        return result


