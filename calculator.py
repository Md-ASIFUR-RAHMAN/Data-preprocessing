#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import * 

root = Tk()

root.title("Ayon's calculator")


inpu = Entry(0,width = 50,bg = "gray",fg= "white",borderwidth = 5)
inpu.grid(row = 0,column = 0,columnspan = 3,padx= 10,pady = 10)

def button_click(number):
    
    current = inpu.get()
    inpu.delete(0,END)
    inpu.insert(0, str(current + str(number)))
    


def button_clear():
    inpu.delete(0,END)
    
    
    



def add():
    num1 = inpu.get()
    global num1_int
    
    num1_int = int(num1)
    inpu.delete(0,END)

def equal():
    num2 = inpu.get()
    global num2_int
    
    num2_int = int(num2)
    inpu.delete(0,END)
    inpu.insert(0,num1_int + num2_int)
    


button1 = Button(root,padx=40,pady=20,text = "1",bg = "brown",command = lambda : button_click(1))
button2 = Button(root,padx=40,pady=20,text = "2",bg = "brown",command = lambda : button_click(2))
button3 = Button(root,padx=40,pady=20,text = "3",bg = "brown",command = lambda : button_click(3))
button4 = Button(root,padx=40,pady=20,text = "4",bg = "pink",command = lambda : button_click(4))
button5 = Button(root,padx=40,pady=20,text = "5",bg = "pink",command = lambda : button_click(5))
button6 = Button(root,padx=40,pady=20,text = "6",bg = "pink",command = lambda : button_click(6))
button7 = Button(root,padx=40,pady=20,text = "7",bg = "brown",command = lambda : button_click(7))
button8 = Button(root,padx=40,pady=20,text = "8",bg = "brown",command = lambda : button_click(8))
button9 = Button(root,padx=40,pady=20,text = "9",bg = "brown",command = lambda : button_click(9))
button0 = Button(root,padx=40,pady=20,text = "0",bg = "pink",command = lambda : button_click(0))

button_add = Button(root,padx=40,pady=20,text = "+",bg = "pink", command = add)
button_equal = Button(root,padx=40,pady=20,text = "=",bg = "pink",command = equal)
button_clear = Button(root,padx=40,pady=20,text = "CL",bg = "pink",command= button_clear)

button1.grid(row =3, column = 0 )
button2.grid(row =3, column = 1 )
button3.grid(row =3, column = 2 )

button4.grid(row =2, column = 0 )
button5.grid(row =2, column = 1 )
button6.grid(row =2, column = 2 )

button7.grid(row =1, column = 0 )
button8.grid(row =1, column = 1 )
button9.grid(row =1, column = 2 )

button0.grid(row = 4, column = 0 )
button_add.grid(row = 4, column = 1 )
button_equal.grid(row = 4, column = 2 )
button_clear.grid(row = 4, column = 3 )


root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




