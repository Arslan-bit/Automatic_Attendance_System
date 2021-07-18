from tkinter import *
import tkinter.messagebox
from GUI_Small_Box import Box1
from stack import *
from Que import *
from Sorting import *



def All_S_M_S():

    from Functions_A_A_S import ObjectDAtaBAss
    window = Tk()
    window.title("Automatic Attendance System")
    # root.geometry('300x400')
    window.state('zoomed')

    Frame_Title = Frame(window,bg="#110606")
    lable_Tital = Label(Frame_Title,text = "Automatic Attendance System", font=('Helvetica', 15, 'bold'), height= 2)

    Frame_Upper = Frame(Frame_Title,bg="#B8CBCF")
    Frame_Left_inUpper = Frame(Frame_Upper,bg="#7E9195")
    Frame_Left2_inUpper = Frame(Frame_Upper,bg="black")
    Frame_Left3_ininUpper = Frame(Frame_Left2_inUpper, bg="#7E9195")



    Create_Detail =Button(Frame_Left_inUpper, width = 20, height=2,bd=5, text = "  Detail Student", font=('Helvetica', 10, 'bold'),command=lambda:[Show_Text.delete('1.0','end'),Show_Text.insert('end',ObjectDAtaBAss.Student_Detail())])


    Show_Detail =Button(Frame_Left_inUpper,width = 20,height=2 ,bd=5,text = " Detail Teacher ", font=('Helvetica', 10, 'bold'),command=lambda:[ Show_Text.delete('1.0','end'),Show_Text.insert('end',ObjectDAtaBAss.Teacher_Detail())])

    THings_Detail_Button = Button(Frame_Left_inUpper, width = 20,bd=5, height=2,text = "Update Student", font=('Helvetica', 10, 'bold'),command=lambda:[Box1.Update_Student_Detail()])

    Add_Button = Button(Frame_Left_inUpper, width = 20, height=2,bd=5,text = "Update Teacher", font=('Helvetica', 10, 'bold'),command=lambda:[Box1.Update_Teacher_Detail()])

    Add_Student_Button = Button(Frame_Left_inUpper, width = 20,bd=5, height=2,text = "Add Student", font=('Helvetica', 10, 'bold'),command=lambda:[Box1.Create_Student_Detail()])


    Add_Teacher_Button = Button(Frame_Left_inUpper, width = 20,bd=5, height=2,text = "Add Teacher", font=('Helvetica', 10, 'bold'),command=lambda:[Box1.Create_Teacher_Detail()])



    DLT_student_Button = Button(Frame_Left_inUpper, width = 20,bd=5, height=2,text = "DLT Student", font=('Helvetica', 10, 'bold'),command=lambda:[Box1.DLT_Students_Detail()])


    DLT_Teacher_Button = Button(Frame_Left_inUpper, width = 20,bd=5, height=2,text = "DLT Teacher", font=('Helvetica', 10, 'bold'),command=lambda:[Box1.DLT_Teacher_Detail()])

    Button_For_Search = Button(Frame_Left_inUpper, text=" Search Student", bd=5, font=('Helvetica', 10, 'bold'),
                               width=20, height=2, command=lambda: [Show_Text.delete('1.0', 'end'),
                                                                    Box1.Search_Student_Detail()])

    Frame_Left_Button = Frame(Frame_Left_inUpper, bg="#7E9195")
    DSA_Analses_Button = Button(Frame_Left_Button, width=6, bd=5, height=2, text="DSA ",font=('Helvetica', 10, 'bold'), command=lambda: [Show_Text.delete('1.0','end'),Show_Text.insert('end',StackAll()),Show_Text.insert('end',QueAll()),Show_Text.insert('end',all_sorting()),Show_Text.insert('end',Arrey_List())])
    DBS_Analses_Button = Button(Frame_Left_Button, width=6, bd=5, height=2, text="DBS ",font=('Helvetica', 10, 'bold'), command=lambda: [])


    Show_Text = Text(Frame_Left3_ininUpper)




    # -----------------Pack---------------------




    Frame_Title.pack(fill=BOTH,side=TOP)
    lable_Tital.pack(pady = 10)
    Frame_Upper.pack(side= TOP,fill= BOTH,expand = 1,padx=15,pady=0)


    Frame_Left_inUpper.pack(side = LEFT, fill= Y,padx=25,pady=25)
    Frame_Left2_inUpper.pack(side = LEFT, fill= BOTH,padx=15,pady=25,expand = 1)
    Frame_Left3_ininUpper.pack(fill = BOTH,padx=25,pady=25,expand = 1)

    #
#-------------------------------------------------------------
    Create_Detail.pack(padx=7,pady=5)
    Show_Detail.pack(padx=5,pady=5)
    THings_Detail_Button.pack(padx=5,pady=5)
    Add_Button.pack(padx=5,pady=5)
    Add_Student_Button.pack(padx=5,pady=5)
    Add_Teacher_Button.pack(padx=5, pady=5)
    DLT_student_Button.pack(padx=5, pady=5)
    DLT_Teacher_Button.pack(padx=5, pady=5)
    Button_For_Search.pack(padx=5,pady=5)

    Frame_Left_Button.pack(fill = BOTH,expand = 1)
    DSA_Analses_Button.pack(side=LEFT,padx=20,pady=5)
    DBS_Analses_Button.pack(side=RIGHT,padx=20,pady=5)
# ---------------------------------------------------------------------------
    Show_Text.pack(padx=75,pady=40,fill=BOTH, expand=1)




    window.mainloop()




# All_S_M_S()


