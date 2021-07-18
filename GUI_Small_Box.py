from tkinter import *
from Functions_A_A_S import ObjectDAtaBAss
import tkinter.messagebox
from tkinter.ttk import Combobox
import time

class Box():

    def Create_Student_Detail(self):
        # from Functions_A_A_S import ObjectDAtaBAss
        window2 = Tk()
        window2.title("Automatic-Attendance-System")
        window2.geometry('400x500')
        # window2.state('zoomed')
        Frame11 = Frame(bg="black")
        Frame2 = Frame(Frame11,bg="#5B6466")
        Lable_Name = Label(Frame2, text="Enter the Student Name", width=30,bd=5,height=2, font=('Helvetica', 10, 'bold'))
        Name_Entry = Entry(Frame2, width=32,bd=5)
        Lable2_Fname = Label(Frame2, text=" Enter the Father Name",bd=5, width=30,height=2, font=('Helvetica', 10, 'bold'))
        Fname_Entry = Entry(Frame2, width=32,bd=5)
        Lable_CNIC = Label(Frame2, text="Enter the CNIC No",bd=5, width=30,height=2, font=('Helvetica', 10, 'bold'))
        CNIC_Entry = Entry(Frame2, width=32,bd=5)
        Lable2_Age = Label(Frame2, text="Enter the Student Age",bd=5, width=30,height=2, font=('Helvetica', 10, 'bold'))
        Age_Entry = Entry(Frame2, width=32,bd=5)
        Lable3_Phone = Label(Frame2, text="Enter the Phone N0",bd=5, width=30,height=2, font=('Helvetica', 10, 'bold'))
        Phone_Entry = Entry(Frame2, width=32,bd=5)
        Lable3_Semester = Label(Frame2, text="Enter the Semester", bd=5, width=30, height=2,font=('Helvetica', 10, 'bold'))
        semester_Entry = Entry(Frame2, width=32, bd=5)
        Lable3_Tid = Label(Frame2, text="Enter the Teacher ID", bd=5, width=30, height=2,font=('Helvetica', 10, 'bold'))
        Tid_Entry = Entry(Frame2, width=32, bd=5)

        Button_Save = Button(Frame2, text="Save", width=12,height=2,bd=5, font=('Helvetica', 10, 'bold')
                        ,command=lambda :[ObjectDAtaBAss.Add_Student(Name_Entry.get(),Fname_Entry.get(),CNIC_Entry.get(),Age_Entry.get(),Phone_Entry.get(),semester_Entry.get(),Tid_Entry.get(),time.ctime(time.time())),tkinter.messagebox.showinfo('Save','Your Student detail is Saved')])
        # ----------------------------------------------------------------
        Frame11.pack(fill= BOTH,expand = 1)
        Frame2.pack(fill= BOTH,expand = 1,padx=15,pady=15)
        # -----------------------------------------------------------
        Lable_Name.pack(padx=5,pady=5)
        Name_Entry.pack(padx=5,pady=5)
        Lable2_Fname .pack(padx=5,pady=5)
        Fname_Entry .pack(padx=5,pady=5)
        Lable_CNIC.pack(padx=5,pady=5)
        CNIC_Entry.pack(padx=5,pady=5)
        Lable2_Age.pack(padx=5,pady=5)
        Age_Entry.pack(padx=5,pady=5)
        Lable3_Phone.pack(padx=5,pady=5)
        Phone_Entry.pack(padx=5,pady=5)
        Lable3_Semester.pack(padx=5,pady=5)
        semester_Entry.pack(padx=5,pady=5)
        Lable3_Tid.pack(padx=5,pady=5)
        Tid_Entry.pack(padx=5,pady=5)
        # -----------------------------------------------------------------
        Button_Save.pack(padx=5,pady=5)
        window2.mainloop()


    def Create_Teacher_Detail(self):

        # from Functions_A_A_S import ObjectDAtaBAss
        window2 = Tk()
        window2.title("Automatic Attendance System")
        window2.geometry('400x500')
        # window.state('zoomed')
        Frame11 = Frame(bg="black")
        Frame2 = Frame(Frame11,bg="#5B6466")

        Lable_Name = Label(Frame2, text="Enter the Teacher Name", width=30,bd=5,height=2, font=('Helvetica', 10, 'bold'))
        Name_Entry = Entry(Frame2, width=32,bd=5)
        Lable2_Fname = Label(Frame2, text=" Enter the Father Name",bd=5, width=30,height=2, font=('Helvetica', 10, 'bold'))
        Fname_Entry = Entry(Frame2, width=32,bd=5)
        Lable_CNIC = Label(Frame2, text="Enter the CNIC No",bd=5, width=30,height=2, font=('Helvetica', 10, 'bold'))
        CNIC_Entry = Entry(Frame2, width=32,bd=5)
        Lable2_Age = Label(Frame2, text="Enter the Teacher Age",bd=5, width=30,height=2, font=('Helvetica', 10, 'bold'))
        Age_Entry = Entry(Frame2, width=32,bd=5)
        Lable3_Phone = Label(Frame2, text="Enter the Phone N0",bd=5, width=30,height=2, font=('Helvetica', 10, 'bold'))
        Phone_Entry = Entry(Frame2, width=32,bd=5)
        Lable3_Subject = Label(Frame2, text="Enter the Subject",bd=5, width=30,height=2, font=('Helvetica', 10, 'bold'))
        Subject_Entry = Entry(Frame2, width=32,bd=5)

        Button_Save = Button(Frame2, text="Save", width=12,height=2,bd=5, font=('Helvetica', 10, 'bold')
                        ,command=lambda :[ObjectDAtaBAss.Add_Teacher(Name_Entry.get(),Fname_Entry.get(),CNIC_Entry.get(),Age_Entry.get(),Phone_Entry.get(),Subject_Entry.get()),tkinter.messagebox.showinfo('Save','Your Teacher Recode is Saved')])

        # ----------------------------------------------------------------

        Frame11.pack(fill= BOTH,expand = 1)
        Frame2.pack(fill= BOTH,expand = 1,padx=15,pady=15)
        # -----------------------------------------------------------
        Lable_Name.pack(padx=5,pady=5)
        Name_Entry.pack(padx=5,pady=5)
        Lable2_Fname .pack(padx=5,pady=5)
        Fname_Entry .pack(padx=5,pady=5)
        Lable_CNIC.pack(padx=5,pady=5)
        CNIC_Entry.pack(padx=5,pady=5)
        Lable2_Age.pack(padx=5,pady=5)
        Age_Entry.pack(padx=5,pady=5)
        Lable3_Phone.pack(padx=5,pady=5)
        Phone_Entry.pack(padx=5,pady=5)
        Lable3_Subject.pack(padx=5,pady=5)
        Subject_Entry.pack(padx=5,pady=5)
        # -----------------------------------------------------------------
        Button_Save.pack(padx=5,pady=5)

        window2.mainloop()

    def Update_Student_Detail(self):


        # from Functions_A_A_S import ObjectDAtaBAss
        window22 = Tk()
        window22.title("Automatic Attendance System")
        window22.geometry('400x500')
        # window.state('zoomed')
        Frame11 = Frame(bg="black")
        Frame2 = Frame(Frame11,bg="#5B6466")

        Data = ('name', 'f_name', 'cnic', 'age', 'phone_no', 'semester')
        Data2 = ('S_id', 'cnic')
        Pack_Com = Combobox(Frame2,  value=Data, font=('Helvetica', 10, 'bold'))

        Pack_Com2 = Combobox(Frame2,  value=Data2, font=('Helvetica', 10, 'bold'))

        Lable_ = Label(Frame2, text="    ",bg="#5B6466", width=30, bd=5, height=2,font=('Helvetica', 10, 'bold'))
        Lable_Name = Label(Frame2, text="Update Student Data", width=30,bd=5,height=2, font=('Helvetica', 10, 'bold'))
        Name_Entry = Entry(Frame2, width=32, bd=5)
        Set_Entry = Entry(Frame2, width=32,bd=5)
        Lable2_Fname = Label(Frame2, text=" Student ID OR CNIC Select",bd=5, width=30,height=2, font=('Helvetica', 10, 'bold'))
        Where_Entry = Entry(Frame2, width=32,bd=5)
        Fname_Entry = Entry(Frame2, width=32,bd=5)


        Button_Save = Button(Frame2, text="Save", width=12,height=2,bd=5, font=('Helvetica', 10, 'bold')
                        ,command=lambda :[ObjectDAtaBAss.Update_Student_Recode(Set_Entry.get(),Name_Entry.get()
                        ,Where_Entry.get(),Fname_Entry.get()),tkinter.messagebox.showinfo('UPDATE','Your Teacher Recode is Update')])
        # ----------------------------------------------------------------

        Frame11.pack(fill= BOTH,expand = 1)
        Frame2.pack(fill= BOTH,expand = 1,padx=15,pady=15)
        # -----------------------------------------------------------
        Lable_.pack(padx=5,pady=5)
        Lable_Name.pack(padx=5,pady=5)
        Pack_Com.pack(padx=5, pady=5)
        Set_Entry.pack(padx=5,pady=5)
        Name_Entry.pack(padx=5,pady=5)
        Lable2_Fname .pack(padx=5,pady=5)
        Pack_Com2.pack(padx=5, pady=5)
        Where_Entry .pack(padx=5,pady=5)
        Fname_Entry .pack(padx=5,pady=5)

        Button_Save.pack(padx=5,pady=5)

        window22.mainloop()


    def Update_Teacher_Detail(self):

        window22 = Tk()
        window22.title("Automatic Attendance System")
        window22.geometry('400x500')
        # window.state('zoomed')
        Frame11 = Frame(bg="black")
        Frame2 = Frame(Frame11,bg="#5B6466")

        Data = ('name', 'f_name', 'cnic', 'age', 'phone_no', 'subject')
        Data2 = ('T_id', 'cnic')
        Pack_Com = Combobox(Frame2,  value=Data, font=('Helvetica', 10, 'bold'))

        Pack_Com2 = Combobox(Frame2,  value=Data2, font=('Helvetica', 10, 'bold'))

        Lable_ = Label(Frame2, text="    ",bg="#5B6466", width=30, bd=5, height=2,font=('Helvetica', 10, 'bold'))
        Lable_Name = Label(Frame2, text="Update Teacher Data", width=30,bd=5,height=2, font=('Helvetica', 10, 'bold'))
        Name_Entry = Entry(Frame2, width=32, bd=5)
        Set_Entry = Entry(Frame2, width=32,bd=5)
        Lable2_Fname = Label(Frame2, text=" Teacher ID OR CNIC Select",bd=5, width=30,height=2, font=('Helvetica', 10, 'bold'))
        Where_Entry = Entry(Frame2, width=32,bd=5)
        Fname_Entry = Entry(Frame2, width=32,bd=5)


        Button_Save = Button(Frame2, text="Save", width=12,height=2,bd=5, font=('Helvetica', 10, 'bold')
                        ,command=lambda :[ObjectDAtaBAss.Update_Teacher_Recode(Set_Entry.get(),Name_Entry.get()
                        ,Where_Entry.get(),Fname_Entry.get()),tkinter.messagebox.showinfo('UPDATE','Your Teacher Recode is Update')])
        # ----------------------------------------------------------------

        Frame11.pack(fill= BOTH,expand = 1)
        Frame2.pack(fill= BOTH,expand = 1,padx=15,pady=15)
        # -----------------------------------------------------------
        Lable_.pack(padx=5,pady=5)
        Lable_Name.pack(padx=5,pady=5)
        Pack_Com.pack(padx=5, pady=5)
        Set_Entry.pack(padx=5,pady=5)
        Name_Entry.pack(padx=5,pady=5)
        Lable2_Fname .pack(padx=5,pady=5)
        Pack_Com2.pack(padx=5, pady=5)
        Where_Entry .pack(padx=5,pady=5)
        Fname_Entry .pack(padx=5,pady=5)

        Button_Save.pack(padx=5,pady=5)

        window22.mainloop()




    def DLT_Students_Detail(self):

        window22 = Tk()
        window22.title("Automatic Attendance System")
        window22.geometry('400x500')
        # window.state('zoomed')
        Frame11 = Frame(bg="black")
        Frame2 = Frame(Frame11,bg="#5B6466")


        Lable_ = Label(Frame2, text="    ",bg="#5B6466", width=30, bd=5, height=2,font=('Helvetica', 10, 'bold'))
        Lable_Name = Label(Frame2, text="Enter the S_id", width=30,bd=5,height=2, font=('Helvetica', 10, 'bold'))
        Name_Entry = Entry(Frame2, width=32, bd=5)




        Button_Save = Button(Frame2, text="DELETE", width=12,height=2,bd=5, font=('Helvetica', 10, 'bold')
                        ,command=lambda :[ObjectDAtaBAss.DLT_Student_Recode(Name_Entry.get()),tkinter.messagebox.showinfo('DELETE','Your Student Recode is DLT')])

        # ----------------------------------------------------------------

        Frame11.pack(fill= BOTH,expand = 1)
        Frame2.pack(fill= BOTH,expand = 1,padx=15,pady=15)
        # -----------------------------------------------------------
        Lable_.pack(padx=5,pady=5)
        Lable_Name.pack(padx=5,pady=5)

        Name_Entry.pack(padx=5,pady=5)

        Button_Save.pack(padx=5,pady=5)

        window22.mainloop()





    def DLT_Teacher_Detail(self):

        window22 = Tk()
        window22.title("Automatic Attendance System")
        window22.geometry('400x500')
        # window.state('zoomed')
        Frame11 = Frame(bg="black")
        Frame2 = Frame(Frame11,bg="#5B6466")
        Lable_ = Label(Frame2, text="    ",bg="#5B6466", width=30, bd=5, height=2,font=('Helvetica', 10, 'bold'))
        Lable_Name = Label(Frame2, text="Enter the T_id", width=30,bd=5,height=2, font=('Helvetica', 10, 'bold'))
        Name_Entry = Entry(Frame2, width=32, bd=5)
        Button_Save = Button(Frame2, text="DELETE", width=12,height=2,bd=5, font=('Helvetica', 10, 'bold')
                        ,command=lambda :[ObjectDAtaBAss.DLT_Teacher_Recode(Name_Entry.get()),tkinter.messagebox.showinfo('DELETE','Your Teacher Recode is DLT')])
        # ----------------------------------------------------------------
        Frame11.pack(fill= BOTH,expand = 1)
        Frame2.pack(fill= BOTH,expand = 1,padx=15,pady=15)
        # -----------------------------------------------------------
        Lable_.pack(padx=5,pady=5)
        Lable_Name.pack(padx=5,pady=5)
        Name_Entry.pack(padx=5,pady=5)
        Button_Save.pack(padx=5,pady=5)
        window22.mainloop()




    def Search_Student_Detail(self):



        window22 = Tk()
        window22.title("Automatic Attendance System")
        # window22.geometry('400x500')
        window22.state('zoomed')
        Frame11 = Frame(bg="black")
        Frame2 = Frame(Frame11,bg="#5B6466")

        Data = ('*','name', 'f_name', 'cnic', 'age', 'phone_no', 'semester')
        Data2 = ('name', 'f_name', 'cnic', 'age', 'phone_no', 'semester')
        Pack_Com = Combobox(Frame2,  value=Data, font=('Helvetica', 10, 'bold'))

        Pack_Com2 = Combobox(Frame2,  value=Data2, font=('Helvetica', 10, 'bold'))

        Lable_Name = Label(Frame2, text="Search Student Recode", width=30,bd=5,height=2, font=('Helvetica', 10, 'bold'))
        Name_Entry = Entry(Frame2, width=32, bd=5)
        Lable2_Fname = Label(Frame2, text=" Select To ",bd=5, width=30,height=2, font=('Helvetica', 10, 'bold'))
        Where_Entry = Entry(Frame2, width=32,bd=5)
        Fname_Entry = Entry(Frame2, width=32,bd=5)


        Button_Search = Button(Frame2, text="Search", width=12,height=2,bd=5, font=('Helvetica', 10, 'bold')
                        ,command=lambda :[Show_Text.delete('1.0','end'),Show_Text.insert('end',ObjectDAtaBAss.find_the_Data(Name_Entry.get()
                        ,Where_Entry.get(),Fname_Entry.get()))])

        Frame333 = Frame(Frame2,bg="black")
        Show_Text = Text(Frame333)
        # ----------------------------------------------------------------

        Frame11.pack(fill= BOTH,expand = 1)
        Frame2.pack(fill= BOTH,expand = 1,padx=15,pady=15)

        # -----------------------------------------------------------

        Lable_Name.pack(padx=5,pady=5)
        Pack_Com.pack(padx=5, pady=5)

        Name_Entry.pack(padx=5,pady=5)
        Lable2_Fname .pack(padx=5,pady=5)
        Pack_Com2.pack(padx=5, pady=5)
        Where_Entry .pack(padx=5,pady=5)
        Fname_Entry .pack(padx=5,pady=5)

        Button_Search.pack(padx=5,pady=5)
        Frame333.pack(fill=BOTH, expand=1,padx=335, pady=15)
        Show_Text.pack(padx=5, pady=15)

        window22.mainloop()






Box1 = Box()

# Box1.Update_Teacher_Detail()
# Box1.DLT_Teacher_Detail()

# def on_field_change(a,s,e):
#     print(on_field_change,c.get())
#     return  c.get()
#
# root = Tk()
# v = StringVar()
# v.trace('w',on_field_change)
# c = Combobox(root, textvar=v, values=["fooo", "bar"])
# c.pack()
# print(v)
# mainloop()











