from tkinter import *
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox


class Student:
    def __init__(self, root):

        self.root = root
        self.root.title("Student Management System")

        self.root.geometry("1350x700")
        title = Label(self.root, text='Students list', relief=GROOVE, font=('times new roman', 60, 'bold'), bd=10,
                      bg='yellow', fg='red')
        title.place(x=0, y=0, width=1350, height=100)

        self.Name_var = StringVar()
        self.Age_var = StringVar()
        self.Gender_var = StringVar()
        self.DOB_var = StringVar()
        self.Contact_var = StringVar()
        self.Address_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        frame = Frame(self.root, bg='crimson', relief=GROOVE, bd=10)
        frame.place(x=0, y=100, width=500, height=600)

        name = Label(frame, text='Name', font=('times new roman', 20, 'bold'), bg='white', fg='black')
        name.place(x=30, y=10, width=150, height=50)
        text_name = Entry(frame, textvariable=self.Name_var, font=('times new roman', 20, 'bold'), bg='white')
        text_name.place(x=230, y=10, width=200, height=50)

        Age = Label(frame, text='Age', font=('times new roman', 20, 'bold'), bg='white', fg='black')
        Age.place(x=30, y=80, width=150, height=50)
        text_Age = Entry(frame, textvariable=self.Age_var, font=('times new roman', 20, 'bold'), bg='white')
        text_Age.place(x=230, y=80, width=200, height=50)

        Gender = Label(frame, text='Gender', font=('times new roman', 20, 'bold'), bg='white', fg='black')
        Gender.place(x=30, y=150, width=150, height=50)
        text_Gender = ttk.Combobox(frame, textvariable=self.Gender_var, font=('times new roman', 20, 'bold'))
        text_Gender['values'] = ("Male", "Female", "Other")
        text_Gender.place(x=230, y=150, width=200, height=50)

        Contact = Label(frame, text='Contact', font=('times new roman', 20, 'bold'), bg='white', fg='black')
        Contact.place(x=30, y=220, width=150, height=50)
        text_Contact = Entry(frame, textvariable=self.Contact_var, font=('times new roman', 20, 'bold'), bg='white')
        text_Contact.place(x=230, y=220, width=200, height=50)

        DOB = Label(frame, text='DOB', font=('times new roman', 20, 'bold'), bg='white', fg='black')
        DOB.place(x=30, y=290, width=150, height=50)
        text_DOB = Entry(frame, textvariable=self.DOB_var, font=('times new roman', 20, 'bold'), bg='white')
        text_DOB.place(x=230, y=290, width=200, height=50)

        Address = Label(frame, text='Address', font=('times new roman', 20, 'bold'), bg='white', fg='black')
        Address.place(x=30, y=360, width=150, height=50)
        self.text_Address = Text(frame, font=('times new roman', 10, 'bold'), bg='white')
        self.text_Address.place(x=230, y=360, width=200, height=100)

        ADD = Button(frame, text='Add', command=self.add_student, font=('times new roman', 20, 'bold'), bg='grey',
                     fg='white')
        ADD.place(x=20, y=480, width=80, height=40)

        delete = Button(frame, text='Delete',  font=('times new roman', 20, 'bold'), bg='grey',
                        fg='white')
        delete.place(x=120, y=480, width=80, height=40)

        Update = Button(frame, text='Update', font=('times new roman', 20, 'bold'), bg='grey',
                        fg='white')
        Update.place(x=220, y=480, width=80, height=40)

        Clear = Button(frame, text='Clear', font=('times new roman', 20, 'bold'), bg='grey',
                       fg='white')
        Clear.place(x=320, y=480, width=80, height=40)

        Manage = Frame(self.root, bg='crimson', relief=GROOVE, bd=10)
        Manage.place(x=550, y=100, width=800, height=600)

        search = Label(Manage, text='Search by', font=('times new roman', 20, 'bold'), bg='crimson', fg='white')
        search.place(x=0, y=20)

        text_search = ttk.Combobox(Manage, textvariable=self.search_by, font=('times new roman', 20, 'bold'))
        text_search['values'] = ("Name", "Contact", "Address")
        text_search.place(x=150, y=20, width=150, height=50)

        search1 = Entry(Manage, textvariable=self.search_txt, font=('times new roman', 20, 'bold'), bg='white')
        search1.place(x=350, y=5, width=150, height=85)

        search2 = Button(Manage, text='Search', font=('times new roman', 20, 'bold'),
                         bg='grey', fg='white')
        search2.place(x=530, y=20, width=100, height=50)

        ShowAll = Button(Manage, text='Show All', command=self.fetch_data, font=('times new roman', 20, 'bold'),
                         bg='grey', fg='white')
        ShowAll.place(x=660, y=20, width=100, height=50)

        table_frame = Frame(Manage, bg='white', relief=GROOVE, bd=10)
        table_frame.place(x=10, y=100, width=760, height=400)

        scrollx = Scrollbar(table_frame, orient=HORIZONTAL)
        scrolly = Scrollbar(table_frame, orient=VERTICAL)
        self.table = ttk.Treeview(table_frame, columns=("Name", "Age", "Gender", "DOB", "Contact", "Address"),
                                  xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.table.xview)
        scrolly.config(command=self.table.yview)
        self.table.heading("Name", text="Name")
        self.table.heading("Age", text="Age")
        self.table.heading("Gender", text="Gender")
        self.table.heading("DOB", text="DOB")
        self.table.heading("Contact", text="Contact")
        self.table.heading("Address", text="Address")
        self.table['show'] = ['headings']
        self.table.column("Name", width=100)
        self.table.column("Age", width=100)
        self.table.column("Gender", width=100)
        self.table.column("DOB", width=100)
        self.table.column("Contact", width=100)
        self.table.column("Address", width=100)
        self.table.pack(fill=BOTH, expand=1)

        self.fetch_data()

    def add_student(self):
        if self.Name_var.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="student management system")
            cur = con.cursor()

            cur.execute("INSERT INTO `student management system` VALUES(%s,%s,%s,%s,%s,%s)", (self.Name_var.get(),
                                                                                              self.Age_var.get(),
                                                                                              self.Gender_var.get(),
                                                                                              self.DOB_var.get(),
                                                                                              self.Contact_var.get(),
                                                                                              self.text_Address.get(
                                                                                                  '1.0', END)
                                                                                              ))
            messagebox.showinfo("Done", "New student added")
            con.commit()
            self.fetch_data()
            con.close()

    def fetch_data(self):
        con = mysql.connect(host="localhost", user="root", password="", database="student management system")
        cur = con.cursor()

        cur.execute("SELECT * FROM `student management system`")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.table.delete(*self.table.get_children())
            for row in rows:
                self.table.insert('', END, values=row)
        con.commit()
        con.close()

    def clear_data(self):
        self.Name_var.set(""),
        self.Age_var.set(""),
        self.Gender_var.set(""),
        self.DOB_var.set(""),
        self.Contact_var.set(""),
        self.text_Address.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row = self.table.focus()
        contents = self.table.item(cursor_row)
        row = contents['values']
        self.Name_var.set(row[0]),
        self.Age_var.set(row[1]),
        self.Gender_var.set(row[2]),
        self.DOB_var.set(row[3]),
        self.Contact_var.set(row[4]),
        self.text_Address.delete("1.0", END)
        self.text_Address.insert(END, row[5])

    def update_data(self):
        con = mysql.connect(host="localhost", user="root", password="", database="student management system")
        cur = con.cursor()

        cur.execute(
            "UPDATE `student management system` SET Age=%s,Gender=%s,DOB=%s,Contact=%s,Address=%s WHERE Name=%s",
            (self.Age_var.get(),
             self.Gender_var.get(),
             self.DOB_var.get(),
             self.Contact_var.get(),
             self.text_Address.get('1.0', END),
             self.Name_var.get()
             ))
        messagebox.showinfo("Done", "Student info updated")
        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()

    def delete_data(self):
        con = mysql.connect(host="localhost", user="root", password="", database="student management system")
        cur = con.cursor()
        cur.execute("DELETE FROM `student management system` WHERE Name=%s", self.Name_var.get())
        messagebox.askyesno("Delete", "Do you want delete the student")
        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()

    def search_data(self):
        con = mysql.connect(host="localhost", user="root", password="", database="student management system")
        cur = con.cursor()
        cur.execute("SELECT * FROM `student management system` WHERE " + str(self.search_by.get()) + " LIKE '" + str(
            self.search_txt.get()) + "'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.table.delete(*self.table.get_children())
            for row in rows:
                self.table.insert('', END, values=row)
        con.commit()
        con.close()


root = Tk()
ob = Student(root)
root.mainloop()
