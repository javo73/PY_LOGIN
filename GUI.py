import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import Menu
from tkinter import *

def pull_user():
    #Retrieving user text from Text Box
    user = user_txt.get('1.0','end-1c')
    return user

def pull_pswd():
    #Retrieving password text from Text Box
    pswd = pswd_txt.get('1.0','end-1c')
    return pswd
        
def success_pop():
    popup=tk.Toplevel()
    popup.title('Info')
    popup.geometry('200x120')
    msg = tk.Message(popup,text= 'Succesfully Logged In!',width=200)
    msg.pack(fill=X,expand=YES)
    button = tk.Button(popup,text='OK',command=popup.destroy)
    button.pack(fill=X,expand=YES)
    state_lbl.configure(text='Logged In')   
def failure_pop():
    popup=tk.Toplevel()
    popup.title('Info')
    popup.geometry('200x120')
    msg = tk.Message(popup,text= 'User/Password Incorrect, Try Again',width=200)
    msg.pack(fill=X,expand=YES)
    button = tk.Button(popup,text='OK',command=popup.destroy)
    button.pack(fill=X,expand=YES)
    state_lbl.configure(text='Log In Error')
def chk_login():
    import login_tools
    import userdb
    if(login_tools.login_check(userdb.user_dict,pull_user(),pull_pswd())):
        success_pop()
    else:
        failure_pop()    

def log_popup():
    #Login Pop Up Window
    global user_txt
    global pswd_txt
    login_popup= tk.Toplevel(window) 
    login_popup.title("Login Pop-Up")
    init_lbl = tk.Label(login_popup, text="Enter User and Password")
    init_lbl.pack()

    user_lbl = tk.Label(login_popup,text='User:')
    user_lbl.pack()
    user_txt = tk.Text(login_popup,height=1,width=20)
    user_txt.focus_set()
    user_txt.pack()

    pswd_lbl = tk.Label(login_popup,text='Password:')
    pswd_lbl.pack()
    pswd_txt = tk.Text(login_popup,height=1,width=20)
    pswd_txt.pack()
    login_btn = tk.Button(login_popup,text='Log In',command = chk_login)
    login_btn.pack()

def new_user():
    nu_window = tk.Toplevel(window)
    nu_window.title('New User')
    init_lbl = tk.Label(nu_window,text='Provide a User Name')
    init_lbl.pack()
    
    init_txt = tk.Text(nu_window,height=1,width=10)
    init_txt.focus_set()
    init_txt.pack()
    
    init_btn = tk.Button(nu_window,text='Continue',command= usr_chk)
    def usr_chk():
        
    
    
    

window = tk.Tk() #Main Window
window.title("Javo's Login App")
window.geometry('300x300')
state_lbl=tk.Label(window,text='Not Logged In')
state_lbl.pack()
menu = Menu(window)
menu.add_command(label='Log In',command=log_popup)
menu.add_command(label='Log Out')
menu.add_command(label='Exit')
window.config(menu=menu)
user_txt = 'user' #Giving example name so i can declare it global later on
pswd_txt = 'pass' #Giving example name so i can declare it global later on
    
    

window.mainloop()
