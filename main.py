from tkinter import *
from tkinter import ttk
#Background page required

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

lab1 = Label(fr1 , text='Number of nodes' , fg='white' , bg= '#2c3e50')
lab1.place(x=10,y=20)
ent1 = Entry(fr1 , justify='center' ,fg= 'black' , bg = '#ecf0f1')
ent1.place(x=150 , y = 20)

#Entre number of branches

lab2 = Label(fr1 , text='Number of branches' , fg='white' , bg= '#2c3e50')
lab2.place(x=10,y=50)
ent2 = Entry(fr1 , justify='center' , fg= 'black' , bg = '#ecf0f1')
ent2.place(x=150 , y = 50)

#Matirices frame

fr2 = Frame(width='400',height = '350' ,bg='#95a5a6')
fr2.place(x=300,y=0)

#Graph frame

fr3 = Frame(width='400',height = '350' ,bg='#7f8c8d')
fr3.place(x=300,y=350)

root.mainloop()