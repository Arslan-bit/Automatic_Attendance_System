from sqlite3 import  *
conn = connect("Test.db")
cur = conn.cursor()

# sqlQuery = """CREATE TABLE students(S_id integer , name text NOT NULL,T_id integer ) """
# sqlQuery = """CREATE TABLE teachers(T_id integer , name text NOT NULL ) """

# create the tables
# sqlQuery = """INSERT INTO students VALUES(1004,'Hamza',1002,21)"""
# sqlQuery = """INSERT INTO teachers VALUES(1003,'Numan')"""
sqlQuery = "SELECT students.S_id , students.name ,students.T_id,students.age " \
           ",teachers.name FROM students INNER JOIN teachers on teachers.T_id = students.T_id"

# sqlQuery = "ALTER TABLE students ADD COLUMN agr"
# sqlQuery = "ALTER TABLE students RENAME COLUMN agr TO age"

# # # save the recode
# sqlQuery = """  SELECT f_name FROM Teacher_Recodes  """
# # # update the recode
# sqlQuery = """UPDATE  Teacher_Recodes SET name = 'Hamza' WHERE T_id = 1001"""
cur.execute(sqlQuery)
print(cur.fetchall())
conn.commit()
conn.close()