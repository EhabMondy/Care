
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import tkinter as tk


class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in) 
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

if __name__ == "__main__":


    root = Tk()
    root.title("CareServices Employee")
    root.geometry('1000x500')

    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    # c.execute("""CREATE TABLE IF NOT EXISTS Employee (id TEXT NOT NULL PRIMARY KEY ,
    #            name TEXT NOT NULL,ID_Nationality TEXT NOT NULL,address TEXT NOT NULL,brith_day TEXT NOT NULL,
    #            Social_Situation TEXT NOT NULL,Monthly_Salary TEXT NOT NULL,Qualification TEXT NOT NULL,
    #            Occupation TEXT NOT NULL)
    #            """)

    C_N=Label(root,text='CareServices',font=("arial",40,"bold"))
    C_N.grid(row=1,column=5)

    id_lbl = Label(root,text='ID',font=("arial",12,"bold"))
    id_lbl.grid(row=2,column=1)

    id_ent = EntryWithPlaceholder(root,"ادخل الرقم التوظيفى",)
    id_ent.grid(row=2,column=2)

    name_lbl = Label(root,text='Name',font=("arial",12,"bold"))
    name_lbl.grid(row=2,column=3)

    name_ent = EntryWithPlaceholder(root,"أسم الموظـــــــــــف")
    name_ent.grid(row=2,column=4)

    nation_lbl = Label(root,text='ID Nationality',font=("arial",12,"bold"))
    nation_lbl.grid(row=3,column=1)

    nation_ent = EntryWithPlaceholder(root,"أدخل الرقم القومى")
    nation_ent.grid(row=3,column=2)

    address_lbl = Label(root,text='Address',font=("arial",12,"bold"))
    address_lbl.grid(row=3,column=3)

    address_ent = EntryWithPlaceholder(root,"العنـــــــــــوان")
    address_ent.grid(row=3,column=4)

    brith_lbl = Label(root,text='Brith Day',font=("arial",12,"bold"))
    brith_lbl.grid(row=4,column=1)

    brith_ent = EntryWithPlaceholder(root,"تاريخ الميلاد")
    brith_ent.grid(row=4,column=2)

    situation_lbl = Label(root,text='Social Situation',font=("arial",12,"bold"))
    situation_lbl.grid(row=4,column=3)

    situation_ent = EntryWithPlaceholder(root,"الحالة الاإجتماعية")
    situation_ent.grid(row=4,column=4)

    salary_lbl = Label(root,text='Monthly Salary',font=("arial",12,"bold"))
    salary_lbl.grid(row=5,column=1)

    salary_ent = EntryWithPlaceholder(root,"الراتـــــــــــــب")
    salary_ent.grid(row=5,column=2)

    qualification_lbl = Label(root,text='Qualification',font=("arial",12,"bold"))
    qualification_lbl.grid(row=5,column=3)

    qualification_ent = EntryWithPlaceholder(root,"المؤهل الدراسى")
    qualification_ent.grid(row=5,column=4)

    occupation_lbl = Label(root,text='Occupation',font=("arial",12,"bold"))
    occupation_lbl.grid(row=6,column=1)

    occupation_ent = EntryWithPlaceholder(root,"الوظيفــــــــــة")
    occupation_ent.grid(row=6,column=2)

    tree = ttk.Treeview(root,columns=(1,2,3,4,5,6,7,8,9),show="headings",height=10)
    tree.place(x=5,y=300)

    vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    vsb.place(x=5 + 1550 + 2, y=300, height=208 + 20)
    tree.configure(yscrollcommand=vsb.set)

    tree.heading(1, text='ID')
    tree.heading(2, text='Name')
    tree.heading(3, text='ID Nationality ')
    tree.heading(4, text='Address')
    tree.heading(5, text='Brith Day')
    tree.heading(6, text='Social Situation')
    tree.heading(7, text='Monthly Salary')
    tree.heading(8, text='Qualification ')
    tree.heading(9, text='Occupation')

    tree.column(1, width=50, anchor='n')
    tree.column(2, width=200, anchor='n')
    tree.column(3, width=150, anchor='n')
    tree.column(4, width=150, anchor='n')
    tree.column(5, width=150, anchor='n')
    tree.column(6, width=150, anchor='n')
    tree.column(7, width=150, anchor='n')
    tree.column(8, width=150, anchor='n')
    tree.column(9, width=150, anchor='n')




    def get_items_list_empolyee():
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Employee (id TEXT NOT NULL PRIMARY KEY ,
                 name TEXT NOT NULL,ID_Nationality TEXT NOT NULL,address TEXT NOT NULL,brith_day TEXT NOT NULL,
                 Social_Situation TEXT NOT NULL,Monthly_Salary TEXT NOT NULL,Qualification TEXT NOT NULL,
                 Occupation TEXT NOT NULL)
                 """)

        id_query_empolyee = "SELECT id FROM Employee"
        id_list_empolyee = c.execute(id_query_empolyee)
        my_id_empolyee = id_list_empolyee.fetchall()
        int_id_empolyee = [x[0] for x in my_id_empolyee]
        return int_id_empolyee


    getitems_list_empolyee = get_items_list_empolyee()


    def get_items_empolyee():
        id_employee = id_ent.get()
        name_employee = name_ent.get()
        id_nationality_employee = nation_ent.get()
        address_employee = address_ent.get()
        brith_day_employee = brith_ent.get()
        social_situation_employee = situation_ent.get()
        monthly_salary_employee = salary_ent.get()
        qualification_employee = qualification_ent.get()
        occupation_employee = occupation_ent.get()

        if id_employee == 'ادخل الرقم التوظيفى' or name_employee == 'أسم الموظـــــــــــف' or id_nationality_employee == 'أدخل الرقم القومى' or address_employee == 'العنـــــــــــوان' or brith_day_employee == 'تاريخ الميلاد' or social_situation_employee == 'الحالة الاإجتماعية' or monthly_salary_employee == 'الراتـــــــــــــب' or qualification_employee == 'المؤهل الدراسى' or occupation_employee == 'الوظيفــــــــــة':
            messagebox.showinfo("Error", "Please Fill all entries")

        else:
            sql_empolyee = "INSERT INTO Employee (id, name, ID_Nationality, address, brith_day, Social_Situation, Monthly_Salary, Qualification, Occupation) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql_empolyee, (id_employee,name_employee , id_nationality_employee,address_employee ,brith_day_employee , social_situation_employee, monthly_salary_employee,qualification_employee,occupation_employee ))
            conn.commit()
            # self.get_data()
            # messagebox.showinfo('Success', 'Successfully add Empolyee')

            tree.insert("",'end',values=(id_employee,name_employee , id_nationality_employee,address_employee ,brith_day_employee , social_situation_employee, monthly_salary_employee,qualification_employee,occupation_employee))
            # id_ent.delete(0, END)
            # name_ent.delete(0, END)
            # nation_ent.delete(0, END)
            # address_ent.delete(0, END)
            # brith_ent.delete(0, END)
            # situation_ent.delete(0, END)
            # salary_ent.delete(0, END)
            # qualification_ent.delete(0, END)
            # occupation_ent.delete(0, END)






    def search_list_imp_id():
       ssql_s = "SELECT id, name, ID_Nationality, address, brith_day, Social_Situation, Monthly_Salary, Qualification, Occupation FROM Employee WHERE id=?"
       result = c.execute(ssql_s,(id_ent.get()))
       for r in result:
           id_1 = r[0]
           id_2 = r[1]
           id_3 = r[2]
           id_4 = r[3]
           id_5 = r[4]
           id_6 = r[5]
           id_7 = r[6]
           id_8 = r[7]
           id_9 = r[8]
           id_ent.insert(0, str(id_1))
           name_en.insert(0, str(id_2))
           nation_ent.insert(0, str(id_3))
           address_ent.insert(0, str(id_4))
           brith_ent.insert(0, str(id_5))
           situation_ent.insert(0, str(id_6))
           salary_ent.insert(0, str(id_7))
           qualification_ent.insert(0, str(id_8))
           occupation_ent.insert(0, str(id_9))
           id_ent.delete(0,END)
           name_en.delete(0,END)
           nation_ent.delete(0,END)
           address_ent.delete(0,END)
           brith_ent.delete(0,END)
           situation_ent.delete(0,END)
           salary_ent.delete(0,END)
           qualification_ent.delete(0,END)
           occupation_ent.delete(0,END)
    conn.commit()   

    #    def search_list_items(self, *args, **kwargs):
            # ssql_c = "SELECT id, name, stock, much, cp, sp, vender, vender_phone FROM inventory WHERE id=? OR name=?"
            # result = c.execute(ssql_c, (self.id_item_it.get(),self.name_e_it.get()))
            # for r in result:
            #     self.it1 = r[0]
            #     self.it2 = r[1]
            #     self.it3 = r[2]
            #     self.it4 = r[3]
            #     self.it5 = r[4]
            #     self.it6 = r[5]
            #     self.it10 = r[6]
            #     self.it11 = r[7]
            # conn.commit()
            # # self.get_items(result)
            # self.id_item_it.delete(0,END)
            # self.id_item_it.insert(0, str(self.it1))

            # self.name_e_it.delete(0,END)
            # self.name_e_it.insert(0,str(self.it2))

            # self.stock_e_it.delete(0,END)
            # self.stock_e_it.insert(0, str(self.it3))

            # # self.combo_stock.delete(0,END)
            # self.combo_stock.insert(0, str(self.it4))

            # self.cp_e_it.delete(0,END)
            # self.cp_e_it.insert(0, str(self.it5))

            # self.sp_e_it.delete(0,END)
            # self.sp_e_it.insert(0, str(self.it6))

            # self.vendor_e_it.delete(0,END)
            # self.vendor_e_it.insert(0, str(self.it10))

            # self.vendor_phone_e_it.delete(0,END)
            # self.vendor_phone_e_it.insert(0, str(self.it11))


    save_butt = Button(root, text='حفظ',command=get_items_empolyee)
    save_butt.grid(row=7,column=5)

    search_butt = Button(root, text='بحث رقم الموظف',command=search_list_imp_id)
    search_butt.grid(row=7,column=2)

    search1_butt = Button(root, text='بحث أسم الموظف',command=get_items_empolyee)
    search1_butt.grid(row=7,column=3)


root.mainloop()
