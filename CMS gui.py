from CMSusingOOPS import *
from tkinter import *
from tkinter import messagebox
def add_handler():
    cus=Customer()
    cus.id=var_id.get()
    cus.name=var_name.get()
    cus.age=var_age.get()
    cus.mob=var_mob.get()
    cus.addCustomer()
    messagebox.showinfo("MY CMS","CUSTOMER DATA ADDEDD SUCCESSFULLY")
    var_id.set("")
    var_name.set("")
    var_age.set("")
    var_mob.set("")

def search_handler():
   cus=Customer()
   cus.id=var_id.get()
   cus.searchCustomer()
   var_name.set(cus.name)
   var_age.set(cus.age)
   var_mob.set(cus.mob)

def delete():
    cus=Customer()
    cus.id=var_id.get()
    cus.deleteCustomer()
    messagebox.showinfo("MY CMS","Are You Sure To Delete Message")
    var_id.set("")

def modify():
    cus=Customer()
    cus.id=var_id.get()
    
    cus.name=var_name.get()
    cus.age=var_age.get()
    cus.mob=var_mob.get()
    cus.modifyCustomer()
    messagebox.showinfo("MY CMS","DATA MODIFY SUCCESSFULLY")

def allhandler(): 
    root_all=Tk()
    root_all.geometry("500x400")
    lbl_id_all=Label(root_all,text="Cust id",bg="purple",width=15,font=20)
    lbl_id_all.grid(row=0,column=0)
    lbl_name_all=Label(root_all,text="Cust name",bg="purple",width=15,font=20)
    lbl_name_all.grid(row=0,column=1)
    lbl_age_all=Label(root_all,text="Cust age",bg="purple",width=15,font=20)
    lbl_age_all.grid(row=0,column=2)
    lbl_mob_all=Label(root_all,text="Cust mobile",bg="purple",width=15,font=20)
    lbl_mob_all.grid(row=0,column=3)
    
    i=1
    for e in Customer.cus_list:
        lbl_id_data=Label(root_all,text=e.id,bg="skyblue",width=15,font=20)
        lbl_id_data.grid(row=i,column=0)
        lbl_name_data=Label(root_all,text=e.name,bg="skyblue",width=15,font=20)
        lbl_name_data.grid(row=i,column=1)
        lbl_age_data=Label(root_all,text=e.age,bg="skyblue",width=15,font=20)
        lbl_age_data.grid(row=i,column=2)
        lbl_mob_data=Label(root_all,text=e.mob,bg="skyblue",width=15,font=20)
        lbl_mob_data.grid(row=i,column=3)
        i+=1

def savehandler():
    Customer.savedata()
    messagebox.showinfo("MY CMS","data save successfully")

def loadhandler():
    Customer.load_data()
    messagebox.showinfo("MY CMS","DATA LOADED SUCCESSFULLY")
    

root=Tk()
root.geometry("700x400")

#Label
lbl_id=Label(root,text="Enter cus id:",font=20)
lbl_id.grid(row=0,column=0)
lbl_name=Label(root,text="Enter cus Name:",font=20)
lbl_name.grid(row=1,column=0)
lbl_age=Label(root,text="Enter cus age:",font=20)
lbl_age.grid(row=2,column=0)
lbl_mob=Label(root,text="Enter cus mobile:",font=20)
lbl_mob.grid(row=3,column=0)

#ENTRY
var_id=StringVar()
ent_id=Entry(root,font=20,textvariable=var_id)
ent_id.grid(row=0,column=1)
var_name=StringVar()
ent_name=Entry(root,font=20,textvariable=var_name)
ent_name.grid(row=1,column=1)
var_age=StringVar()
ent_age=Entry(root,font=20,textvariable=var_age)
ent_age.grid(row=2,column=1)
var_mob=StringVar()
ent_mob=Entry(root,font=20,textvariable=var_mob)
ent_mob.grid(row=3,column=1)

#BUTTON
btn_add=Button(root,text="ADD",font=20,width=10,height=1,bg='black',fg="white",command=add_handler)
btn_add.grid(row=4,column=0,padx=0,pady=0)
btn_search=Button(root,text="SEARCH",font=20,width=10,height=1,bg='black',fg="white",command=search_handler)
btn_search.grid(row=4,column=1,padx=0,pady=0)
btn_delete=Button(root,text="DELETE",font=20,width=10,height=1,bg='black',fg="white",command=delete)
btn_delete.grid(row=4,column=2)
btn_modify=Button(root,text="MODIFY",font=20,width=10,height=1,bg='black',fg="white",command=modify)
btn_modify.grid(row=4,column=3)
btn_all=Button(root,text="SHOW ALL",font=20,width=10,height=1,bg='black',fg="white",command=allhandler)
btn_all.grid(row=5,column=0)
btn_save=Button(root,text="SAVE",font=20,width=10,height=1,bg='black',fg="white",command=savehandler)
btn_save.grid(row=5,column=1)
btn_load=Button(root,text="LOAD",font=20,width=10,height=1,bg='black',fg="white",command=loadhandler)
btn_load.grid(row=5,column=2)
root.mainloop()
