import tkinter
from tkinter import *

root=Tk()
root.title("Grade calculator")
root.geometry("500x400")
root.resizable(False,False)
root.configure(bg="#f2f3f5")

def calculation():
    english=int(englishentry.get())
    Java=int(Javaentry.get())
    python=int(Pythonentry.get())
    total=(english+Java+python)
    Label(text=f"{total}",font="arial 15 bold").place(x=250,y=170)

    average=int(total/3)
    Label(text=f"{average}",font="arial 15 bold").place(x=250,y=210)

    if(average>50):
        grade="PASS"
    else:
        grade="Fail"

    Label(text=f"{grade}",font="arial 15 bold",fg="blue").place(x=250,y=270)   

#subject
sub1=Label(root,text="English:",font="arial 10")
sub2=Label(root,text="Java:",font="arial 10")
sub3=Label(root,text="Python:",font="arial 10")
total=Label(root,text="Total:",font="arial 10")
avg=Label(root,text="Average:",font="arial 10")
grade=Label(root,text="Grade:",font="arial 10")


sub1.place(x=50,y=20)
sub2.place(x=50,y=70)
sub3.place(x=50,y=120)
total.place(x=50,y=170)
avg.place(x=50,y=210)
grade.place(x=50,y=250)


englishvalue=StringVar()
Javavalue=StringVar()
Pythonvalue=StringVar()

englishentry=Entry(root,textvariable=englishvalue,font="arial 15",width=15)
Javaentry=Entry(root,textvariable=Javavalue,font="arial 15",width=15)
Pythonentry=Entry(root,textvariable=Pythonvalue,font="arial 15",width=15)

englishentry.place(x=250,y=20)
Javaentry.place(x=250,y=70)
Pythonentry.place(x=250,y=120)

Button(text="Calculate",font="arial 15", bg="white",bd=10,command=calculation).place(x=50,y=300)
Button(text="Exit",font="arial 15", bg="white",bd=10,width=8,command=lambda:exit()).place(x=350,y=300)

root.mainloop()
