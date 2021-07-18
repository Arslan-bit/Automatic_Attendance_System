from sqlite3 import *



conn = connect("Automatic Attendance System.db")


class Automatic_Attendance_System():


    def Add_Student(self,name , f_name , cnic , age , phone_no,semester,Tid,Time):


        conn = connect("Automatic Attendance System.db")
        cur = conn.cursor()
        sqlQuery = "INSERT INTO Students_Recodes VALUES( NULL " + ",'" + str(name) + "','" + str(f_name) + "','" + str(cnic)\
                   + "'," + str(age) + "," + str(phone_no) + "," + str(semester)+ "," + str(Tid)+ ",'" + str(Time) + "')"

        cur.execute(sqlQuery)
        conn.commit()
        conn.close()




    def Add_Teacher(self,name , f_name , cnic , age , phone_no,subject):


        conn = connect("Automatic Attendance System.db")
        cur = conn.cursor()
        sqlQuery = "INSERT INTO Teacher_Recodes VALUES( NULL "  + ",'" + str(name) + "','" + str(f_name) + "','" + str(cnic)\
                   + "'," + str(age) + "," + str(phone_no) + ",'" + str(subject) + "')"

        cur.execute(sqlQuery)
        conn.commit()
        conn.close()

    def Update_Student_Recode(self,Set,AA ,Where ,BB):


        conn = connect("Automatic Attendance System.db")
        cur = conn.cursor()

        if Set == 'name':
            sqlQuery =  "UPDATE Students_Recodes SET  "  + "" + str(Set)+ " = '" + str(AA) + "' WHERE " + str(Where)+ " = " + str(BB) + ""
            cur.execute(sqlQuery)
            conn.commit()
            conn.close()

        elif Set == 'f_name':
            sqlQuery =  "UPDATE Students_Recodes SET  "  + "" + str(Set)+ " = '" + str(AA) + "' WHERE " + str(Where)+ " = " + str(BB) + ""
            cur.execute(sqlQuery)
            conn.commit()
            conn.close()

        elif Set == 'cnic':
            sqlQuery =  "UPDATE Students_Recodes SET  "  + "" + str(Set)+ " = '" + str(AA) + "' WHERE " + str(Where)+ " = " + str(BB) + ""
            cur.execute(sqlQuery)
            conn.commit()
            conn.close()

        else:
            sqlQuery = "UPDATE Students_Recodes SET  " + "" + str(Set) + " = " + str(AA) + " WHERE " + str(Where) + " = " + str(BB) + ""
            cur.execute(sqlQuery)
            conn.commit()
            conn.close()



    def Update_Teacher_Recode(self,Set,AA ,Where ,BB):


        conn = connect("Automatic Attendance System.db")
        cur = conn.cursor()

        if Set == 'name':
            sqlQuery =  "UPDATE Teacher_Recodes SET  "  + "" + str(Set)+ " = '" + str(AA) + "' WHERE " + str(Where)+ " = " + str(BB) + ""
            cur.execute(sqlQuery)
            conn.commit()
            conn.close()

        elif Set == 'f_name':
            sqlQuery =  "UPDATE Teacher_Recodes SET  "  + "" + str(Set)+ " = '" + str(AA) + "' WHERE " + str(Where)+ " = " + str(BB) + ""
            cur.execute(sqlQuery)
            conn.commit()
            conn.close()

        elif Set == 'cnic':
            sqlQuery =  "UPDATE Teacher_Recodes SET  "  + "" + str(Set)+ " = '" + str(AA) + "' WHERE " + str(Where)+ " = " + str(BB) + ""
            cur.execute(sqlQuery)
            conn.commit()
            conn.close()

        elif Set == 'subject':
            sqlQuery =  "UPDATE Teacher_Recodes SET  "  + "" + str(Set)+ " = '" + str(AA) + "' WHERE " + str(Where)+ " = " + str(BB) + ""
            cur.execute(sqlQuery)
            conn.commit()
            conn.close()

        else:
            sqlQuery = "UPDATE Teacher_Recodes SET  " + "" + str(Set) + " = " + str(AA) + " WHERE " + str(Where) + " = " + str(BB) + ""
            cur.execute(sqlQuery)
            conn.commit()
            conn.close()


    def DLT_Student_Recode(self,BB):


        conn = connect("Automatic Attendance System.db")
        cur = conn.cursor()

        sqlQuery =  "DELETE FROM Students_Recodes "" WHERE S_id "  " = " + str(BB) + ""
        cur.execute(sqlQuery)
        conn.commit()
        conn.close()


    def DLT_Teacher_Recode(self,BB):


        conn = connect("Automatic Attendance System.db")
        cur = conn.cursor()

        sqlQuery =  "DELETE FROM Teacher_Recodes "" WHERE T_id "  " = " + str(BB) + ""
        cur.execute(sqlQuery)
        conn.commit()
        conn.close()



    def Print_Data(self):

        conn = connect("Automatic Attendance System.db")
        cur = conn.cursor()
        sqlQuery = "SELECT * FROM Students_Recodes"
        cur.execute(sqlQuery)
        # print(cur.fetchall())
        return (cur.fetchall())
        conn.commit()
        conn.close()





    def login(self, username, password):
        from GUI import All_S_M_S
        login_file = open('C:/Users/Arslan/PycharmProjects/Automatic Attendance System/login.txt', 'r')
        read_login_file = login_file.read()
        split_read_login_file = read_login_file.split()
        if username == split_read_login_file[1] and password == split_read_login_file[3]:

            All_S_M_S()

        else:
            AA = 0
            return AA

    def change_password(self, oldusername, newusername, oldpassword, newpassword):

        # print("ok1")
        login_file = open('/Users/Arslan/Desktop/login.txt', 'r')
        read_login_file = login_file.read()
        split_read_login_file = read_login_file.split()
        if oldusername == split_read_login_file[1] and oldpassword == split_read_login_file[3]:
            login_file = open('/Users/Arslan/Desktop/login.txt', 'w')
            write_login_file = login_file.write("username " + str(newusername) + " password " + str(newpassword))
            BB = 1
            return BB
        else:
            BB = 0
            return BB



    def Student_Detail(self):
        conn = connect("Automatic Attendance System.db")
        cur = conn.cursor()
        # sqlQuery = """SELECT * FROM Students_Recodes """
        sqlQuery = "SELECT Students_Recodes.S_id , Students_Recodes.name ,Students_Recodes.f_name,Students_Recodes.cnic,Students_Recodes.age,Students_Recodes.phone_no,Students_Recodes.semester,Students_Recodes.T_id " \
                   ",Teacher_Recodes.name" \
                   " FROM Students_Recodes" \
                   " INNER JOIN Teacher_Recodes" \
                   " on Teacher_Recodes.T_id = Students_Recodes.T_id"
        cur.execute(sqlQuery)
        Find = cur.fetchall()
        conn.commit()
        conn.close()
        # print(Search_Value)
        Connect = "------------------------------------------------------------------------------------------------------\n" \
                  " ID         Name    Father Name    CNIC         Age     Phone NO    Semester  T_ID     Teacher \n" \
                  "------------------------------------------------------------------------------------------------------"
        for list in Find:

            Connect = Connect + "\n"

            for tupple in list:
                Connect = Connect + str(tupple) + str("\t    ")

        return(Connect)



    def Teacher_Detail(self):
        conn = connect("Automatic Attendance System.db")
        cur = conn.cursor()
        sqlQuery = """SELECT * FROM Teacher_Recodes """
        cur.execute(sqlQuery)
        Find = cur.fetchall()
        conn.commit()
        conn.close()
        # print(Search_Value)
        Connect = "---------------------------------------------------------------------------\n" \
                  "  ID       Name     Father Name    CNIC     Age    Phone NO    Subject\n" \
                  "---------------------------------------------------------------------------"
        for list in Find:

            Connect = Connect + "\n"

            for tupple in list:
                Connect = Connect + str(tupple) + str("\t   ")

        return(Connect)



    def find_the_Data(self,AA ,Where ,BB):
        conn = connect("Automatic Attendance System.db")
        cur = conn.cursor()
        print(Where)

        sqlQuery = "SELECT " + str(AA) + " FROM Students_Recodes WHERE " + str(Where)+ " = '" + str(BB) + "'"
        # print(sqlQuery)
        # "SELECT " + str(Search_Value) + " FROM Teacher_Recodes " + str(Respect_To)
        cur.execute(sqlQuery)
        Find = cur.fetchall()
        conn.commit()
        conn.close()
        # print(Search_Value)
        Connect = "---------------------------------------------------------------------------\n" \
                  "Students ID     Name     Father Name    CNIC     Age    Phone NO    Subject\n" \
                  "---------------------------------------------------------------------------"
        for list in Find:

            Connect = Connect + "\n"

            for tupple in list:
                Connect = Connect + str(tupple) + str("\t")
        # print(Connect)

        return (Connect)


ObjectDAtaBAss = Automatic_Attendance_System()

# ObjectDAtaBAss.DLT_Teacher_Recode(1004)
# ObjectDAtaBAss.Add_Student("arslan","raza","23",21,232435,3)

# ObjectDAtaBAss.Update_Teacher_Recode("name",'arslanraza','T_id',1001 )



# print(ObjectDAtaBAss.Print_Data())

