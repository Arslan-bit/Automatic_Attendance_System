from tkinter import *

import tkinter.messagebox
from Functions_A_A_S import ObjectDAtaBAss

window = Tk()
window.geometry('500x400')
window.title("Log IN For Run")
frame0 = Frame(bg= 'black')
frame0.pack(fill= BOTH,expand = 1)
frame1 = Frame(frame0,bg='#5B6466')


login_lable = Label(frame1,text = "Enter The User Name",bd=6, font=('Helvetica', 10, 'bold'))
login_entry = Entry(frame1,width = 25,bd=5)
pass_lable = Label(frame1,text = "Enter The Password",bd=5, font=('Helvetica', 10, 'bold'))
pass_entry = Entry(frame1,width = 25,bd=5)


# --------------------------------------------------------------------------------------
def Show_wrong_password():
    if ObjectDAtaBAss.login(login_entry.get(), pass_entry.get()) == 0:
        tkinter.messagebox.showinfo("Wrong","User Name And Password Is Wrong")


# -----------------------------------------------------------------------------------------

login_button = Button(frame1,height = 2,width =12,bd=5, font=('Helvetica', 10, 'bold'),text = "Log In",command=lambda:[
    Show_wrong_password(),login_entry.delete('0','end'),pass_entry.delete('0','end')])





change_button = Button(frame1,text = "Change The Password",bd=4,width=18,height=2, font=('Helvetica', 10, 'bold'),command = lambda: [Change_Password()])



login_lable.pack(padx=10,pady=10)
login_entry.pack(padx=6,pady=6)
pass_lable.pack(padx=6,pady=6)
pass_entry.pack(padx=6,pady=6)
login_button.pack(padx=6,pady=6)
change_button.pack(padx=6,pady=6)




frame1.pack(fill = BOTH,expand = 1,padx=20,pady=20)



def Change_Password():

    old_username_lable = Label(frame1, text="Enter The Old username",bd=5, font=('Helvetica', 10, 'bold'))
    old_username_entry = Entry(frame1, width=25,bd=5)
    new_username_lable = Label(frame1, text="Enter The New username",bd=5, font=('Helvetica', 10, 'bold'))
    new_username_entry = Entry(frame1, width=25,bd=5)
    old_password_lable = Label(frame1, text="Enter The Old Password",bd=5, font=('Helvetica', 10, 'bold'))
    old_password_entry = Entry(frame1, width=25,bd=5)
    new_password_lable = Label(frame1, text="Enter The New Password",bd=5, font=('Helvetica', 10, 'bold'))
    new_password_entry = Entry(frame1, width=25,bd=5)

    def Data_Cannot_Save():
        if ObjectDAtaBAss.change_password(old_username_entry.get(), new_username_entry.get(), old_password_entry.get(),new_password_entry.get()) == 1:
            tkinter.messagebox.showinfo('Change The Password', 'Successfull')
        else:
            tkinter.messagebox.showinfo('Wrong', 'Cannot Save Plzz Chak the Old User Name And Password')




    login_button = Button(frame1, text="Save",bd=5, font=('Helvetica', 10, 'bold'),height = 3,width =12,command = lambda :[
        Data_Cannot_Save()])


    old_username_lable.pack(padx=10, pady=10)
    old_username_entry.pack(padx=6, pady=6)
    new_username_lable.pack(padx=6, pady=6)
    new_username_entry.pack(padx=6, pady=6)
    old_password_lable.pack(padx=10, pady=10)
    old_password_entry.pack(padx=6, pady=6)
    new_password_lable.pack(padx=6, pady=6)
    new_password_entry.pack(padx=6, pady=6)
    login_button.pack(padx=6, pady=6)



window.mainloop()



