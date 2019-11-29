from tkinter import *
 
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
login_btn = Button(window,text='Log In')
login_btn.pack()

window.mainloop()
