from tkinter import *
from tkinter import messagebox

global entry1
global entry2

userslogin = [{'HouseNo.':"B1451",
                'Password':"KwaKhumz23"},
              {'HouseNo.':"B1448",
                'Password':"B1450"},
                {'HouseNo.':"B1453",
                 'Password':"B1455"}]
count = 1

def login():
    HouseNo=entry1.get()
    password=entry2.get()

    for i in userslogin:
      if (HouseNo=="" and password==""):
        messagebox.showinfo("","Blank Not Allowed")
        break    
    
      elif (HouseNo== userslogin[i]['HouseNo.'] and password==userslogin[i]['Password']):
            messagebox.showinfo("","Sign in Successful")
            count+=1
      
    
    if count > len(userslogin):
      messagebox.showinfo("","Incorrect HouseNo. or Password")
          
root=Tk()
root.title("House Number")
root.geometry("400x300")
root.configure(background='blue')


Label(root,text="HouseNo.").place(x=20,y=20)
Label(root,text="Password").place(x=20,y=70)

            
        

       

