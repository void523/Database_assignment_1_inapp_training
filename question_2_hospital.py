import sqlite3
import os
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'hospital.db')


def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con

con = db_connect()
cur = con.cursor()


def hospital_tab(Hospital_Id, Hospital_Name, Bed_Count):
    hospital_sql = """
    INSERT INTO hospital (Hospital_Id,Hospital_Name,Bed_Count) VALUES (?,?,?)"""
    cur.execute(hospital_sql, (Hospital_Id, Hospital_Name, Bed_Count))


def doctor_tab(Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience):
    doctor_sql = """
    INSERT INTO doctor (Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience) VALUES (?,?,?,?,?,?,?)"""
    cur.execute(doctor_sql, (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience))

def doc_speciality_list(Speciality, Salary):
    try:
        sql_query = "SELECT * FROM doctor WHERE Speciality = ? and Salary > ?"
        cur.execute(sql_query, (Speciality, Salary))
        results = cur.fetchall()
        print("Details of  doctors whose specialty is", Speciality, "and salary greater than", Salary, "\n")
        for row in results:
            print("Doctor Id: ", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
    except:
        print("Error while retrieving data")

def hospital_name_info(Hospital_Id):
    try:
        sql_query = "SELECT * FROM hospital WHERE Hospital_Id = ?"
        cur.execute(sql_query, Hospital_Id)
        result = cur.fetchone()
        return result[1]
    except:
        print("Error while retrieving data.")

def doc_info(Hospital_Id):
    try:
        hospital_name = hospital_name_info(Hospital_Id)
        name_query = "SELECT * FROM doctor WHERE Hospital_Id =?"
        cur.execute(name_query,Hospital_Id)
        doc_hos = cur.fetchall()

        print("Printing Doctors of ", hospital_name, "Hospital")
        for row in doc_hos:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Hospital Name:", hospital_name)
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
    except:
        print("Error while retrieving doctor's data")


'''
creating hospital table
'''

hospital_sql = """
CREATE TABLE hospital(
    Hospital_Id INTEGER NOT NULL PRIMARY KEY,
    Hospital_Name TEXT NOT NULL,
    Bed_Count INTEGER NOT NULL);
    """
cur.execute(hospital_sql)

'''
Inserting into hospital Table
'''

hospital_tab('1', 'Mayo Clinic', 200)
hospital_tab('2', 'Cleveland Clinic', 400)
hospital_tab('3', 'Johns Hopkins', 1000)
hospital_tab('4', 'UCLA Medical Center', 1500)

'''
creating doctor table
'''

doctor_sql = '''
CREATE TABLE doctor(
    Doctor_Id INTEGER NOT NULL PRIMARY KEY,
    Doctor_Name TEXT NOT NULL,
    Hospital_Id INTEGER NOT NULL,
    Joining_Date TEXT NOT NULL,
    Speciality TEXT NOT NULL,
    Salary INTEGER NOT NULL,
    Experience TEXT);
    '''
cur.execute(doctor_sql)

'''
Inserting into doctor Table
'''

doctor_tab('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', 'None')
doctor_tab('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', 'None')
doctor_tab('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', 'None')
doctor_tab('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', 'None')
doctor_tab('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', 'None')
doctor_tab('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', 'None')
doctor_tab('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', 'None')

list_of_doc = input('Do you want to get  the list Of doctors as per the given specialty and salary? (Y/N): ')
if list_of_doc == 'Y' or 'y':
    doc = input("Enter Doctor's Speciality: ")
    sal = input('Enter the salary information: ')
else:
    exit()
doc_speciality_list(doc, sal)

hos_name = input("Do you want to fetch all the doctors as per the given Hospital Id (Y/N): ")
if hos_name == 'Y' or 'y':
    hos_id = input("Enter Hospital ID [1,2,3,4]: ")
    doc_info(hos_id)
else:
    exit()