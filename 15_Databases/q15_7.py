import random

import pyodbc

if __name__ == '__main__':
    server = 'localhost'
    database = 'Ctci'
    username = 'sa'
    password = 'passW0rd'
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    for i in range(1, 101, True):
        sql = f"INSERT INTO Ctci.dbo.Q15_7_Students VALUES ({i}, 'Student{i}', 'Address{i}');"
        print(sql)
        cursor.execute(sql)

    for i in range(1, 11, True):
        sql = f"INSERT INTO Ctci.dbo.Q15_7_Courses VALUES ({i}, 'Course{i}', {random.randint(1, 10)});"
        print(sql)
        cursor.execute(sql)

    for i in range(1, 101, True):
        # pick 3 numbers of course
        courses = random.sample(list(range(1, 11)), 5)
        for c in courses:
            sql = f"INSERT INTO Ctci.dbo.Q15_7_CourseEnrollment VALUES ({c}, {i}, {random.randint(1, 4)}, {random.randint(1, 4)});"
            print(sql)
            cursor.execute(sql)

    cnxn.commit()
    cursor.close()
    cnxn.close()
