from Tkinter import *
import ttk
import time

# This file will convert the amounts from Kilogram to Gram and vice versa .
# But this is just a simple example .
# You can understand as well as develop your earnings .
# Source_Name_Make = HALIM _ HIOUANI .
# This file is for vulnerable people in Python .
#
# This Python file uses the following encoding: utf-8


def Root():
    ARRAY = ['halim', 'hiouani']

    if ENTRY_A.get() == ARRAY[0] and ENTRY_B.get() == ARRAY[1]:
        ROOT.destroy()
        ROOt = Tk()
        ROOt.title('LOGIN')
        ROOt.geometry('400x210+500+150')
        ROOt.resizable(0, 0)
        FRAMe = Frame(ROOt, relief=GROOVE, borderwidth=2, bg='yellow')
        framE = Frame(FRAMe, width=300, height=120, bg='light blue').pack()
        Label(framE, text='Welcome, I\'m ' + ARRAY[0]).place(x=80, y=50)
        Label(framE, text="I'm Student in University ALGERIA \n I'm Tell is 1.60 m And My Old is 22 Yours"). \
            place(x=70, y=80)
        Label(framE, text='STATE YOU', fg='blue').place(relx=.260, rely=.085)
        FRAMe.pack(pady=30)
        ttk.Button(ROOt, text='QUIT', command=ROOt.destroy, width=6).place(x=340, y=175)
        ROOt.mainloop()
    else:
        global LABEL_C
        LABEL_C.configure(text='PASSWORD ERROR', fg='red')


ROOT = Tk()
ROOT.title('LOGIN')
ROOT.geometry('300x250+500+150')
ROOT.resizable(0, 0)

FRAME = Frame(ROOT, relief=GROOVE, borderwidth=2, bg='blue')

frame = Frame(FRAME, width=250, height=150).pack()
Label(ROOT, text=time.ctime(), fg='blue').place(x=20, y=10)
Label(frame, text='Welcome', fg='red').place(relx=.250, rely=.14)

LABEL_A = ttk.Label(frame, text='Name :').place(x=40, y=70)

ENTRY_A = ttk.Entry(frame, width=20)
ENTRY_A.bind('<Return>', Root)
ENTRY_A.place(x=90, y=70)

LABEL_B = ttk.Label(frame, text='pass :').place(x=40, y=100)

ENTRY_B = ttk.Entry(frame, width=20)
ENTRY_B.bind('<Return>', Root)
ENTRY_B.place(x=90, y=100)

LABEL_C = Label(frame)
LABEL_C.place(x=60, y=150)

ttk.Button(frame, text='CHECK', width=7, command=Root).place(x=215, y=150)

FRAME.pack(pady=45)

ttk.Button(ROOT, text='EXIT', width=5, command=ROOT.destroy).place(x=247, y=218)

ROOT.mainloop()
