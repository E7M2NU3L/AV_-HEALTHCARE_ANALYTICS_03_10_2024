import mysql.connector as db
import logging
from mysql_results import RunQueries

# connect to the database
class DBConnect:
    def __init__(self, host : str, user : str, password : str, database : str) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def db_connect(self):
        connection = db.connect(
            host=self.host,      
            user=self.user,      
            password=self.password,  
            database=self.database 
        )
        if connection is not None:
            logging.info("Connected to the MySQL database")
            print("Connected to the MySQL database")
            return connection
        else:
            logging.error("Error: Unable to connect to the database")

def connect_to_database(host : str, user : str, password : str, database : str):
    instance = DBConnect(host=host, user=user, password=password, database=database)
    connection = instance.db_connect()
    return connection

if __name__ == "__main__":
    conn = connect_to_database(host="localhost", user="root", password="Emm3nAr0k@1908!", database="av_healthcare_databasee")
    cursor = conn.cursor()

    runner = RunQueries(cursor)

    admission_reports = runner.admission_type_report()
    print(admission_reports)

    hospital_department_reports = runner.hospital_department_statistics()
    print(hospital_department_reports)

    patient_reports = runner.fetch_patient_details()
    print(patient_reports)
    
    cursor.close()
    conn.close()