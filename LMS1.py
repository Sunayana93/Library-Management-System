from tkinter import*
from tkinter import ttk
import mysql.connector

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        #====================variable==================================
        self.emailid_var=StringVar()
        self.title_var=StringVar()
        self.name_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.bookname_var=StringVar()
        self.duedate_var=StringVar()
        self.days_var=StringVar()
        self.latefine_var=StringVar()
        self.dateoverdue_var=StringVar()


        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
         #================dataframeleft===============       
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",14,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMemebr=Label(DataFrameLeft,bg="powder blue",textvariable=self.emailid_var,text="emailid",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblMemebr.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Signup","Admin Login")
        comMember.grid(row=0,column=1)


        lblEmail_Id=Label(DataFrameLeft,bg="powder blue",textvariable=self.emailid_var,text="Email_Id",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblEmail_Id.grid(row=1,column=0,sticky=W)
        txtEmail_Id=Entry(DataFrameLeft,font=("times new roman",14,"bold"),width=29)
        txtEmail_Id.grid(row=1,column=1)

        lblPassword=Label(DataFrameLeft,bg="powder blue",text="password",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblPassword.grid(row=2,column=0,sticky=W)
        txtpassword=Entry(DataFrameLeft,font=("times new roman",14,"bold"),width=29)
        txtpassword.grid(row=2,column=1)
        #def generate_random_password():
          #  len=int(input("enter password len:"))
           # random.shuffle(CHARACTERS)
            #password=[]
            #for i in range(len):
             #   password.append(random.choice(CHARACTERS))
              #  random.shuffle(password)
               # print("".join(password))
                #generate_random_password()

         #=============== Data Frame for Right=======================
                
        DataFrameRight=LabelFrame(frame,bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",14,"bold"),text="Book Details")
        DataFrameRight.place(x=910,y=5,width=500,height=350)

        self.txtBox=Text(DataFrameRight, font=("times new roman",14,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listscrollbar=Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0,column=1,sticky="ns")

        ListBooks=['Head Firt Book', 'Learn Python','Python Programming','Joss Ellif guru','Machine Python', 'Advance Python','Guru Of Python','Advamce Python','The Alogrithm','Fluent Python','Red Python']
        listBox=Listbox(DataFrameRight,font=("times new roman",14,"bold"),width=20,height=16)
        listBox.grid(row=0,column=0,padx=4)
        listscrollbar.config(command=listBox.yview)

        for item in ListBooks:
            listBox.insert(END,item)


        #==================Buttons FRame=========================
        framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(framebutton,text="Add Data",font=("times new roman",14,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(framebutton,text="Show Data",font=("times new roman",14,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)
        
        btnAddData=Button(framebutton,text="Update",font=("times new roman",14,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)
        

        btnAddData=Button(framebutton,text="Delete",font=("times new roman",14,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)
        
        btnAddData=Button(framebutton,text="Reset",font=("times new roman",14,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(framebutton,text="Exit",font=("times new roman",14,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)
        
        
        
        
        #==================Information FRame=========================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=210)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,padx=20,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("emailid","title","name","mobile","bookid","bookname","duedate","days","latefine","dateoverdue"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        
        self.library_table.heading("emailid",text="EmailID")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("name",text="Name")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="BookID")
        self.library_table.heading("bookname",text="Book Name")
        
        self.library_table.heading("duedate",text="Due Date")
        self.library_table.heading("days",text="Days")
        self.library_table.heading("latefine",text="Late Fine")
        self.library_table.heading("dateoverdue",text="Date over Due")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Panda@123",database="db_name")   
        my_cursor=conn.cursor()
        my_cursor.execute("library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",()) 

        

if __name__ =="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root) 
    root.mainloop()





