import sqlite3
import tkinter
import re
#*****creating a connection to our database and then creating cursors*****
conn=sqlite3.connect('c:memory.db')
c=conn.cursor()
#************************TABLE HAS BEEN CREATED IN OUR DATABASE****************
#c.execute("""CREATE TABLE Information (
#  name text,
# number text,
#email text
#)""")
#%%***************CREATING A MAIN WINDOW FOR OUR GUI AND ADDING FRAME,LISTBOX,SCROLL*********
window=tkinter.Tk()
window.geometry('500x500')
window.title('Virtual Contact Book')
name_var=tkinter.StringVar()
number_var=tkinter.StringVar()
email_var=tkinter.StringVar()
frame=tkinter.Frame(window)
frame.pack(side="top", anchor='ne')
scroll = tkinter.Scrollbar(frame, orient="vertical")
select = tkinter.Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config (command=select.yview)
scroll.pack(side="right", fill='y')
select.pack(side="left",  fill="both", expand=1)
 #%%****************APPLYING CONCEPTS OF OOP TO OPTIMIZE OUR PROGRAM**********
class contactbook:

#********DISPLAYS CHANGES ON THE GUI LISTBOX*********************
    
  def insert_list(self):
    select.delete(0,'end')
    with  conn:
      c.execute("SELECT *FROM Information name")
      d=c.fetchall()
    for i in range(len(d)):
      select.insert("end",d[i][0])
          
#*********VIEWS THE DETAILS OF THE SELECTED CONTACT************
  def view_contacts(self):
    try:
      with  conn:
        c.execute("SELECT *FROM Information name")
        d=c.fetchall()
      name,number,email=d[select.curselection()[0]]
      name_var.set(name)
      number_var.set(number)
      email_var.set(email)
    except:
      pass
      
#***SETS THE ENTRY BOXES WITH THE DETAILS OF THE CONTACT TO BE MODIFIED***
  def edit_contacts(self):
    try:
      with  conn:
        c.execute("SELECT *FROM Information name")
        d=c.fetchall()
      name,number,email=d[select.curselection()[0]]
      name_var.set(name)
      number_var.set(number)
      email_var.set(email)
      b2.config(state='disabled')
      b3.config(state='disabled')
      b4.config(state='disabled')
      reset.config(state='disabled')
      okay.config(state='normal')
    except:
        pass
#***UPDATES THE TABLE WITH THE NEW ENTRIES PROVIDED BY THE USER******
  def edit(self):
    try:
      with  conn:
        c.execute("SELECT *FROM Information name")
        d=c.fetchall()
      name,number,email=d[select.curselection()[0]]
      c.execute("""UPDATE Information 
        SET name=:name,number=:number,email=:email
        WHERE name=:n""",{'name':name_var.get(),'number':number_var.get(),'email':email_var.get(),'n':name})
      name_var.set("")
      number_var.set("")
      email_var.set("")
      okay.config(state='disabled')
      b2.config(state='normal')
      b3.config(state='normal')
      b4.config(state='normal')
      reset.config(state='normal')
      obj.insert_list()
    except:
      pass
        
#**********ADDS A CONTACT TO THE TABLE********
  def add_contacts(self):
    try:
     t1=name_var.get()
     t2=number_var.get()
     t3=email_var.get()
     if(t1!="" and t2!="" and t3!=""):
       lst=[]
       with  conn:
          c.execute("SELECT *FROM Information name")
          d=c.fetchall()
       for i in range(len(d)):
         if(t1==d[i][0]):
          for j in range(len(d)):
           x=re.findall(t1,d[j][0])
           lst.extend(x)
           
       if(len(lst)!=0):
        t1=t1+str(len(lst))
       with conn:
        c.execute("INSERT INTO Information VALUES(:name,:number,:email)",{'name':t1,'number':t2,'email':t3})
       obj.insert_list()
       name_var.set("")
       number_var.set("")
       email_var.set("")
     else:
      pass
    except:
     pass
     print("Invalid Action,Please try again!")
#**********DELETES A CONTACT FROM THE TABLE****************
  def delete_contacts(self):
    try:
      with  conn:
        c.execute("SELECT *FROM Information name")
        d=c.fetchall()
      n,number,email=d[select.curselection()[0]]
      with conn:
        c.execute("DELETE FROM Information WHERE name=:t",{'t':n})
      obj.insert_list()
    except:
      pass
        
obj=contactbook()
#%%***********INITIAL DATA BEEN ADDED TO TABLE FOR REFERENCING********
contactlist = [
        ['Esha Shelar',  '7045706148','esha.shelar@somaiya.edu'],
        ['Arva Kachwala','9920463305', 'arva.kachwala@somaiya.edu'],
        ['Anisha Sah',   '9819814377','anisha.sah@somaiya.edu'],
        ['Saraunsh Jadhav','9820983908','saraunsh.jadhav@somaiya.edu'],
        ['vallari kulkarni',   '7718939746','vallari.kulkarni@somaiya.edu'],
        ['Dhruv Nouni' , '8169141966' , 'dhruv.nouni@somaiya.edu'],
          ]
#for i in range (len(contactlist)):
 #with conn:
  #c.execute("INSERT INTO Information VALUES(:name,:number,:email)",{'name':contactlist[i][0],'number':contactlist[i][1],'email':contactlist[i][2]})
obj.insert_list()
#%%*******ENTRY BOXES,LABELS AND BUTTONS HAVE BEEN CREATED*********
label1=tkinter.Label(window,text="Name").place(x=0,y=0)
e1 = tkinter.Entry(window,textvariable=name_var).place(x=60,y=0)
label1=tkinter.Label(window,text='Number').place(x=0,y=50)
e2 = tkinter.Entry(window,textvariable=number_var).place(x=60,y=50)
label1=tkinter.Label(window,text='Email-id').place(x=0,y=100)
e3 = tkinter.Entry(window,textvariable=email_var).place(x=60,y=100)
b1=tkinter.Button(window,text='edit  ',command=obj.edit_contacts)
b1.place(x=20,y=150)
b2=tkinter.Button(window,text='add   ',command=obj.add_contacts)
b2.place(x=100,y=150)
b3=tkinter.Button(window,text='view',command=obj.view_contacts)
b3.place(x=20,y=200)
b4=tkinter.Button(window,text='delete',command=obj.delete_contacts)
b4.place(x=100,y=200)
okay=tkinter.Button(window,text='OK ',command=obj.edit,state='disabled')
okay.place(x=180,y=150)
reset=tkinter.Button(window,text='reset',command=lambda:[name_var.set(""),number_var.set(""),email_var.set("")])
reset.place(x=180,y=200)
window.mainloop()
conn.commit()
conn.close()

