import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import os
import mysql.connector
import dotenv
from dotenv import load_dotenv
import string
import time

load_dotenv()
try :
  def main_app():
    db_user = os.environ['db_username']
    db_pass = os.environ['db_password']
    db_host = os.environ['db_hostname']
    db_name = os.environ['db_name']
    db_table = os.environ['db_table']
    db_table_primary = os.environ['db_table_primary']
    db_column1 = os.environ['db_column1']
    db_column2 = os.environ['db_column2']
    db_column3 = os.environ['db_column3']

    mydb = mysql.connector.connect (
      host = db_host,
      user = db_user,
      password = db_pass,
      database = db_name
    )
    cursor = mydb.cursor()

    top =tk.Tk()
    top.title("Database Table Editing Tool")
    top.geometry("500x500")


    def table_contents():

      newWindow = Toplevel(top)
      newWindow.title("Users List")

      # The Restart Function

      def restart():
        newWindow.destroy()
        table_contents()

        # New Connection To Refresh The Database

      mydb = mysql.connector.connect (
      host = db_host,
      user = db_user,
      password = db_pass,
      database = db_name
        )
      cursor = mydb.cursor()

        # sets the geometry of toplevel
      newWindow.geometry("840x600")

        # The SQL To Fetch The Rows
      sql_id = """ SELECT {} FROM `{}` """.format(db_table_primary, db_table)
      cursor.execute(sql_id)
      result_id = cursor.fetchall()

      sql_username = """ SELECT {} FROM `{}` """.format(db_column1, db_table)
      cursor.execute(sql_username)
      result_username = cursor.fetchall()

      sql_userid = """ SELECT {} FROM `{}` """.format(db_column2, db_table)
      cursor.execute(sql_userid)
      result_userid = cursor.fetchall()

      sql_msg = """ SELECT {} FROM `{}` """.format(db_column3, db_table)
      cursor.execute(sql_msg)
      result_msg = cursor.fetchall()

      #
      # The ID Label, Table, And Delete Button
      #

      id_lb = Label(newWindow, text="{}".format(db_table_primary))
      id_lb.grid(row=0, column=0)

      id = Listbox(newWindow, height = 10, width = 16, bg = "white", activestyle = 'dotbox', font = "Helvetica", fg = "Black")
      for thelist in result_id:
        id.insert(1, thelist)
        id.grid(row=1, column=0)

       # To Get A Selected Entry In The Listbox

      def id_delete():
        for i in id.curselection():
            item = str(id.get(i))
            cleanitem = item.translate(str.maketrans('', '', string.punctuation))
            sql_delete = """ DELETE FROM `{}` WHERE `{}` = '{}' """.format(db_table,db_table_primary, cleanitem)
            cursor.execute(sql_delete)
            mydb.commit()
            #Label(newWindow, text="Row : {} Was Deleted Succesfully".format(cleanitem)).grid(row=5, column=2)
            restart()
        # The Delete Button
      Button(newWindow, text="Delete", command=id_delete ,activebackground="grey", activeforeground="grey").grid(row=2, column=0)

      # CONFIRMATION BUTTON

      def confirm_delete_all():
        delete_all = Toplevel(top)
        delete_all.title("Delete All Confirmation")
        delete_all.geometry("300x300")
        Button(delete_all, text="CONFIRM DELETE ALL", command=delete_all_func, activebackground="grey", activeforeground="grey", pady=10).place(relx=0.5, rely=0.5, anchor=CENTER)
        global close_confirmation
        def close_confirmation():
          delete_all.destroy()

      # THE DELETE ALL FUNCTION
      def delete_all_func():
        for contents in result_id:
          item = str(contents)
          cleanitem = item.translate(str.maketrans('', '', string.punctuation))
          sql_delete_all = """ DELETE FROM `{}` WHERE `{}` = '{}' """.format(db_table, db_table_primary, cleanitem)
          cursor.execute(sql_delete_all)
          mydb.commit()
        restart()
        close_confirmation()



      # THE DELETE ALL BUTTON

      Button(newWindow, text="Delete All", command=confirm_delete_all, activebackground="grey", activeforeground="grey").grid(row=4, column=0)

      #
      # The Username Label, Table
      #

      uname_lb = Label(newWindow, text="{}".format(db_column1))
      uname_lb.grid(row=0, column=1)

      uname = Listbox(newWindow, height = 10, width = 16, bg = "white", activestyle = 'dotbox', font = "Helvetica", fg = "Black")
      for thelist in result_username:
        uname.insert(1, thelist)
        uname.grid(row=1, column=1)

      # To Get The Selected From Listbox And Edit It

      def username_editing():
        for i in uname.curselection():
            item = str(uname.get(i))
            cleanitem = item.translate(str.maketrans('', '', string.punctuation))
            # Get The Entry
            username_edit = username_edited.get()
            # The SQL
            sql_delete = """ UPDATE `{}` SET `{}`='{}' WHERE `{}` = '{}' """.format(db_table, db_column1, username_edit,db_column1, cleanitem)
            cursor.execute(sql_delete)
            mydb.commit()
            restart()

      # To Make A Button And A Place To Type The New Text

      def username_edit_button():
        Label(newWindow, text="").grid(row=5)
        global username_edited
        username_edited = Entry(newWindow, width = 30)
        username_edited.grid(row=6,column=2)
        Label(newWindow, text="").grid(row=7)
        Button(newWindow, text="Apply Edit",command=username_editing, activebackground="grey", activeforeground="grey", pady=10).grid(row=8, column=2)

      # The Edit Button

      Button(newWindow, text="Edit", command=username_edit_button ,activebackground="grey", activeforeground="grey").grid(row=2, column=1)

      #
      # The UserId Label, Table
      #

      uid_lb = Label(newWindow, text="{}".format(db_column2))
      uid_lb.grid(row=0, column=2)

      uid = Listbox(newWindow, height = 10, width = 16, bg = "white", activestyle = 'dotbox', font = "Helvetica", fg = "Black")
      for thelist in result_userid:
        uid.insert(1, thelist)
        uid.grid(row=1, column=2)
      # To Get The Selected From Listbox And Edit It

      def userid_editing():
        for i in uid.curselection():
            item = str(uid.get(i))
            cleanitem = item.translate(str.maketrans('', '', string.punctuation))
            # Get The Entry
            userid_edit = userid_edited.get()
            # The SQL
            sql_delete = """ UPDATE `{}` SET `{}`='{}' WHERE `{}` = '{}' """.format(db_table, db_column2, userid_edit, db_column2, cleanitem)
            cursor.execute(sql_delete)
            mydb.commit()
            restart()

      # To Make A Button And A Place To Type The New Text

      def userid_edit_button():
        Label(newWindow, text="").grid(row=5)
        global userid_edited
        userid_edited = Entry(newWindow, width = 30)
        userid_edited.grid(row=6,column=2)
        Label(newWindow, text="").grid(row=7)
        Button(newWindow, text="Apply Edit",command=userid_editing, activebackground="grey", activeforeground="grey", pady=10).grid(row=8, column=2)

      # The Edit Button

      Button(newWindow, text="Edit", command=userid_edit_button ,activebackground="grey", activeforeground="grey").grid(row=2, column=2)

      # The Message Content Label, Table

      msg_lb = Label(newWindow, text="{}".format(db_column3))
      msg_lb.grid(row=0, column=3)

      msg_content = Listbox(newWindow, height = 10, width = 25, bg = "white", activestyle = 'dotbox', font = "Helvetica", fg = "Black")
      for thelist in result_msg:
       msg_content.insert(1, thelist)
       msg_content.grid(row=1, column=3)

         # To Get The Selected From Listbox And Edit It

      def msg_editing():
        for i in msg_content.curselection():
            item = str(msg_content.get(i))
            cleanitem = item.translate(str.maketrans('', '', string.punctuation))
            # Get The Entry
            msg_edit = msg_edited.get()
            # The SQL
            sql_delete = """ UPDATE `{}` SET `{}`='{}' WHERE `{}` = '{}' """.format(db_table, db_column3, msg_edit, db_column3, cleanitem)
            cursor.execute(sql_delete)
            mydb.commit()
            restart()

      # To Make A Button And A Place To Type The New Text

      def msg_edit_button():
        Label(newWindow, text="").grid(row=5)
        global msg_edited
        msg_edited = Entry(newWindow, width = 30)
        msg_edited.grid(row=6,column=2)
        Label(newWindow, text="").grid(row=7)
        Button(newWindow, text="Apply Edit",command=msg_editing, activebackground="grey", activeforeground="grey", pady=10).grid(row=8, column=2)

      # The Edit Button

      Button(newWindow, text="Edit", command=msg_edit_button ,activebackground="grey", activeforeground="grey").grid(row=2, column=3)

      ###
      Label(newWindow, text="").grid(row=3, column=0)

      # Refresh Button
      refresh = Button(newWindow, text="Refresh", command=restart, activebackground='grey', activeforeground='grey', pady=10)
      refresh.grid(row=4, column=2)

      ## Reset ID To Zero

      Label(newWindow, text="").grid(row=7, column=0)

      def reset_primary():
        sql_reset_id = """ alter table {} AUTO_INCREMENT=1; """.format(db_table)
        Label(newWindow, text="The Table Must Be Empty For This To Work").grid(row=7, column=2)
        cursor.execute(sql_reset_id)
        mydb.commit()

      reset = Button(newWindow, text="Reset {} To Zero".format(db_table_primary), command=reset_primary, activebackground='grey', activeforeground='grey', pady=10)
      reset.grid(row=9, column=2)


    def db_insert():
      inpuser = inputuser.get()

      inpuid = inputuserid.get()

      inpmsg = inputmsg.get()

      lbl.config(text = "{} Input Successful: ".format(db_column1)+inpuser)
      sql = """ INSERT INTO `{}` ({}, {}, {}, {}) VALUES (0, '{}', '{}', '{}')""".format(db_table, db_table_primary, db_column1, db_column2, db_column3, inpuser, inpuid, inpmsg)
      cursor.execute(sql)
      mydb.commit()

    # TextBox Creation
    username = tk.Label(top, text = "Add {} Here".format(db_column1))
    username.pack()

    inputuser = Entry(top, width = 15)
    inputuser.pack()

    username = tk.Label(top, text = "Add {} Here".format(db_column2))
    username.pack()

    inputuserid = Entry(top, width = 15)
    inputuserid.pack()

    usermsg = tk.Label(top, text = "Add {} Here".format(db_column3))
    usermsg.pack()

    inputmsg = Entry(top, width = 15)
    inputmsg.pack()


    empty_space = tk.Label(top, text="")
    empty_space.pack()

    upload_btn = Button(top, text="Upload To Database", command=db_insert, activeforeground="red", activebackground="blue", pady=10)
    upload_btn.pack()

    empty_space = tk.Label(top, text="")
    empty_space.pack()

    mylist = Button(top, text="Show Table Contents", command= table_contents, activebackground="blue", activeforeground="magenta", pady=10)
    mylist.pack()

    lbl = tk.Label(top, text = "Made By MortexAG")
    lbl.pack(side="bottom")
    top.mainloop()
  main_app()

########################################################################
  
  
except:
  
  def signin_app():

    top =tk.Tk()
    top.title("Sign In First Time Only")
    top.geometry("500x500")
      # Sign in Button

    def signin():
      Signin = Toplevel(top)
      Signin.title("Sign in")
      Signin.geometry("400x500")

      # Insert The Database Hostname here

      db_host = tk.Label(Signin, text = "Add Database Host Here")
      db_host.pack()

      db_inputhost = Entry(Signin, width = 20)
      db_inputhost.pack()


      # Insert The Database Username here

      db_username = tk.Label(Signin, text = "Add Database Username Here")
      db_username.pack()

      db_inputuser = Entry(Signin, width = 15)
      db_inputuser.pack()

      # Insert The Database Password here

      db_pass = tk.Label(Signin, text = "Add Database Password Here")
      db_pass.pack()

      db_inputpass = Entry(Signin, width = 15)
      db_inputpass.pack()

      # Insert The Database name here

      db_name = tk.Label(Signin, text = "Add Database Name Here")
      db_name.pack()

      db_inputname = Entry(Signin, width = 15)
      db_inputname.pack()

      # Insert The Database Table Name here

      db_table_name = tk.Label(Signin, text = "Add Database Table Name Here")
      db_table_name.pack()

      db_input_table = Entry(Signin, width = 15)
      db_input_table.pack()

      # Insert The Table Primary (Auto Incriment) here

      db_table_primary = tk.Label(Signin, text = "Add Table Primary (Auto Incriment) Here")
      db_table_primary.pack()

      db_input_table_primary = Entry(Signin, width = 15)
      db_input_table_primary.pack()

        # Insert The Database First Column Name here

      db_column1 = tk.Label(Signin, text = "Add Database Column 1 Name Here")
      db_column1.pack()

      db_input_column1 = Entry(Signin, width = 15)
      db_input_column1.pack()

          # Insert The Database Second Column Name here

      db_column1 = tk.Label(Signin, text = "Add Database Column 2 Name Here")
      db_column1.pack()

      db_input_column2 = Entry(Signin, width = 15)
      db_input_column2.pack()

          # Insert The Database Third Column Name here

      db_column3 = tk.Label(Signin, text = "Add Database Column 3 Name Here")
      db_column3.pack()

      db_input_column3 = Entry(Signin, width = 15)
      db_input_column3.pack()

      def submit_signin():

        db_inputusersign = db_inputuser.get()
        db_inputpasssign = db_inputpass.get()
        db_inputhostsign = db_inputhost.get()
        db_inputnamesign = db_inputname.get()
        db_input_table_sign = db_input_table.get()
        db_input_table_primary_sign = db_input_table_primary.get()
        db_input_column1_sign = db_input_column1.get()
        db_input_column2_sign = db_input_column2.get()
        db_input_column3_sign = db_input_column3.get()

        ### MYSQL ###
        try:
          mydb = mysql.connector.connect (
          host = db_inputhostsign,
          user = db_inputusersign,
          password = db_inputpasssign,
          database = db_inputnamesign
          )
          cursor = mydb.cursor()
          global acstate
          acstate = "Signed In"
          global acstate_color
          acstate_color = "Green"
          file = open("./.env", 'w')
          signin = "db_password = {} \ndb_username = {} \ndb_hostname = {} \ndb_name = {} \ndb_table = {} \ndb_table_primary = {} \ndb_column1 = {} \ndb_column2 = {} \ndb_column3 = {}".format(db_inputpasssign, db_inputusersign, db_inputhostsign, db_inputnamesign , db_input_table_sign, db_input_table_primary_sign, db_input_column1_sign, db_input_column2_sign, db_input_column3_sign)
          file.write(signin)
          file.close()
          readme = open("README.txt", 'w')
          readme.write("You Can Change Your DataBase Data By Editing The '.env' File As A Normal Text File But Keep Everything Vertically Arranged Or Just Delete It And Sign in Again")
          readme.close()
          Label(Signin, text="Sign in Successful Restart The Program To Access The Tool", bg="green").pack()
        except:
          acstate = "Not Signed In"
          acstate_color = "red"
          Label(Signin, text="Error Signing In ", bg="Red").pack()

      Label(top, text="").pack()
      Label(Signin, text="").pack()
      Button(Signin, text="Sign in", activebackground="grey", activeforeground="grey", command=submit_signin).pack()
      Label(Signin, text="").pack()
      Label(Signin, text="Made By MortexAG").pack()

    Label(top, text="").pack()

    Button(top, text="Sign In", command=signin , activebackground="grey", activeforeground="grey").pack()

    # To Set Account State
    acstate = "Not Signed in"
    acstate_color = "red"


    Label(top, text="").pack()

    def account_state():
      messagebox.showinfo(title="State",message="Account State: "+acstate)

    Button(top, text="Sign in State", command=account_state, activebackground="grey", activeforeground="grey").pack()
    Label(top, text="").pack()

    lbl = tk.Label(top, text = "Made By MortexAG")
    lbl.pack(side="bottom")
    top.mainloop()
  signin_app()