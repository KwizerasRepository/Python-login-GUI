from tkinter import *
from tkinter import messagebox

userslogin = [{'HouseNo.':"B1451",
                'Password':"KwaKhumz23"},
              {'HouseNo.':"B1448",
                'Password':"B1450"},
                {'HouseNo.':"B1453",
                 'Password':"B1455"}]
count = 0



def login():
    
    HouseNo = entry1.get()
    password = entry2.get()

    if (HouseNo=="" and password==""):
        messagebox.showinfo("","Blank Not Allowed")
    
    else:
        for i in userslogin:
      
            if (HouseNo== userslogin[i]['HouseNo.'] and password==userslogin[i]['Password']):
                messagebox.showinfo("","Sign in Successful")
                count+=1
        
            elif count == len(userslogin):
                messagebox.showinfo("","Incorrect HouseNo. or Password")


global entry1
global entry2

root = Tk()
root.configure(bg='#90EE90')

Userlbl = Label(root, text='Username ', font=('Areal', 15), bg='#90EE90', fg='white')
Userlbl.place(x=250, y=190)

Passlbl = Label(root, text='Password ', font=('Areal', 15), bg='#90EE90', fg='white')
Passlbl.place(x=250, y=340)

Userentry = Entry(root, font=('Areal', 11))
Userentry.place(x=400, y=200)

Passentry = Entry(root, font=('Areal', 11), show='*')
Passentry.place(x=400, y=350)

Logbtn = Button(root, text='Login', bg='#90EE90', font=('Areal', 10), bd=2, command=login)
Logbtn.place(x=450, y=400)

root.mainloop()