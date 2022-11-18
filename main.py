from tkinter import *
from tkinter import ttk
from Branch import *
from functions import *
from plot import *
branches = []
freq = [0 for i in range(300)]

root = Tk()
root.geometry('700x700+500+50')
root.resizable(False , False)
root.title('CAD Simulation Project')
root.config(background='white')
root.iconbitmap('C:\\Users\\Lenovo\\Downloads\\1490200233-14_82259.ico')

#Input frame

fr1 = Frame(width='300',height = '700' ,bg='#16a085')
fr1.place(x=0,y=0)

#Entre number of nodes

lab2 = Label(fr1 , text='Starting Node' , fg='white' , bg= '#2c3e50')
lab2.place(x=10,y=50)
ent2 = Entry(fr1 , justify='center' ,fg= 'black' , bg = '#ecf0f1')
ent2.place(x=150 , y = 50)
lab3 = Label(fr1 , text='Ending Node' , fg='white' , bg= '#2c3e50')
lab3.place(x=10,y=80)
ent3 = Entry(fr1 , justify='center' ,fg= 'black' , bg = '#ecf0f1')
ent3.place(x=150 , y = 80)
lab4 = Label(fr1 , text='Voltage Source' , fg='white' , bg= '#2c3e50')
lab4.place(x=10,y=120)
ent4 = Entry(fr1 , justify='center' ,fg= 'black' , bg = '#ecf0f1')
ent4.place(x=150 , y = 120)
lab5 = Label(fr1 , text='Current Source' , fg='white' , bg= '#2c3e50')
lab5.place(x=10,y=150)
ent5 = Entry(fr1 , justify='center' ,fg= 'black' , bg = '#ecf0f1')
ent5.place(x=150 , y = 150)
lab6 = Label(fr1 , text='Resistance' , fg='white' , bg= '#2c3e50')
lab6.place(x=10,y=180)
ent6 = Entry(fr1 , justify='center' ,fg= 'black' , bg = '#ecf0f1')
ent6.place(x=150 , y = 180)


def add_branches():
    start = int(ent2.get())
    freq[start] = 1
    ent2.delete(0,END)
    end = int(ent3.get())
    freq[end] = 1
    ent3.delete(0,END)
    V = 0 ; I = 0 ; R = 0
    if(ent4.get != ""):
        V = int(ent4.get())
    if(ent5.get != ""):
        I = int(ent5.get())
    if(ent6.get != ""):
        R = int(ent6.get())
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)
    branches.append(Branch(start,end,V,I,R))

add_branch = Button(fr1 , text = "Add Branch" , command=add_branches)
add_branch.place(x = 20 , y = 210)

#Matirices frame

fr2 = Frame(width='400',height = '350' ,bg='#95a5a6')
fr2.place(x=300,y=0)
fr3 = Frame(width='400',height = '350' ,bg='#7f8c8d')
fr3.place(x=300,y=350)

def display():
    Nodes_number = freq.count(1)
    JB = find_JB(Nodes_number , branches)
    VB = find_VB(Nodes_number , branches)
    JB_list = [round(item[0] , 2) for item in JB.tolist()]
    VB_list = [round(item[0] , 2) for item in VB.tolist()]
    JB_display = Label(fr2 , text= f"JB = \n{JB_list}")
    JB_display.place(x = 20 , y = 20)
    VB_display = Label(fr2 , text= f"VB = \n{VB_list}")
    VB_display.place(x = 20 , y = 120)
    Plot_graph(branches)
    freq.clear()
    branches.clear()


run = Button(fr1 , text = "Run" , command=display)
run.place(x = 250 , y = 210)

#Graph frame


root.mainloop()