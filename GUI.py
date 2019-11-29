from tkinter import *
from tkinter.messagebox import showinfo

def pull_user():
    #Retrieving user text from Text Box
    user = user_txt.get('1.0','end-1c')
    return user

def pull_pswd():
    #Retrieving password text from Text Box
    pswd = pswd_txt.get('1.0','end-1c')
    return pswd
        
def success_pop():
    showinfo('Window','Log In Succesful!')   
def failure_pop():
    showinfo('Window','Incorrect User/Password')
def chk_login():
    import login_tools
    import userdb
    if(login_tools.login_check(userdb.user_dict,pull_user(),pull_pswd())):
        success_pop()
    else:
        failure_pop()    
 
window = Tk()
 
window.title("Javo's Login App")
window.geometry('300x300')
 
init_lbl = Label(window, text="Enter User and Password")
init_lbl.pack()

user_lbl = Label(window,text='User:')
user_lbl.pack()
user_txt = Text(window,height=1,width=20)
user_txt.pack()

pswd_lbl = Label(window,text='Password:')
pswd_lbl.pack()
pswd_txt = Text(window,height=1,width=20)
pswd_txt.pack()
login_btn = Button(window,text='Log In',command = chk_login)
login_btn.pack()
    
    

window.mainloop()
