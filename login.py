from tkinter import *
from tkinter import font as f
from PIL import ImageTk, Image
import random
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import funtions as fn


class LandingPage(Frame):
    def __init__(self, master):
        super(LandingPage, self).__init__(master)
        self.master=master
        self.grid()
        self.font1=f.Font(family='Yu Gothic UI Light', size=25, weight='normal')
        self.font2 = f.Font(family='Yu Gothic UI Light', size=11, weight='normal')
        self.font3 = f.Font(family='Yu Gothic UI Light', size=18)
        self.font4 = f.Font(family='Yu Gothic UI Light', size=13)
        self.font5 = f.Font(family='Yu Gothic UI Light', size=11, weight='normal',underline=True)

        self.blackcolor = '#080808'
        self.darkredcolor='#ED4B3A'
        self.bluecolor = "#110445"
        self.greycolor = '#242124'
        self.greencolor='#00f18c'
        self.whitecolor = 'white'
        self.darkgreycolor = '#221F1F'
        self.lightgreycolor = '#8B8D97'

        self.slide=0
        self.create_widgets()
        self.slideshow()

    def create_widgets(self):
        self.img = PhotoImage(file=f"railly logo green.png")
        self.entryimg =ImageTk.PhotoImage(Image.open("textBox1.png").resize((250,30)))
        self.entryimg2 = ImageTk.PhotoImage(Image.open("textBox1.png").resize((150, 30)))
        self.toggle_btn_img = ImageTk.PhotoImage(Image.open("view.png"))
        self.toggle_btn_img2 = ImageTk.PhotoImage(Image.open("hide.png"))
        self.login_btn = ImageTk.PhotoImage(Image.open("loginButton.png").resize((150,35)))
        self.back_btn = ImageTk.PhotoImage(Image.open("back-button.png"))
        self.trainimg = ImageTk.PhotoImage(Image.open("train2.png"))
        self.routeimg=ImageTk.PhotoImage(Image.open("route.png"))
        self.payimg=ImageTk.PhotoImage(Image.open("hand.png"))
        self.qrcodeimg=ImageTk.PhotoImage(Image.open("QR-Code-01-128.png"))
        self.test = ImageTk.PhotoImage(Image.open("regular.png"))
        self.trainimg2=ImageTk.PhotoImage(Image.open("point1.png").resize((128,128)))

        self.logo=Label(self.master,image=self.img,bg=self.bluecolor)
        self.logo.grid(row=0,column=0,padx=5,pady=(5,0),sticky=NW)


        self.login_frm=Frame(self.master,bg=self.bluecolor,width=400,height=200)
        self.login_frm.grid(row=1,column=1,padx=5,sticky=NW)
        Label(self.login_frm, text="L O G I N", font=self.font1, bg=self.bluecolor,
              fg=self.whitecolor).grid(row=0,column=0,sticky=W,pady=(0,20))
        Label(self.login_frm,text="U S E R N A M E",font=self.font2,bg=self.bluecolor,fg=self.greencolor).grid(row=1,column=0,sticky=W)
        label2=Label(self.login_frm,image=self.entryimg,bg=self.bluecolor)
        label2.grid(row=2,column=0,columnspan=2)
        self.username=Entry(self.login_frm,bg=self.whitecolor,width=30,border=0,font=self.font2,fg=self.blackcolor)
        self.username.grid(row=2,column=0,padx=(0,0),columnspan=2)
        Label(self.login_frm,text="P A S S W O R D",font=self.font2,bg=self.bluecolor,fg=self.greencolor).grid(row=3,column=0,sticky=W,pady=(20,0))
        Label(self.login_frm,image=self.entryimg,bg=self.bluecolor).grid(row=4,column=0,columnspan=2)
        self.password=Entry(self.login_frm,bg=self.whitecolor,show='•',width=26,border=0,font=self.font2,fg=self.blackcolor)
        self.password.grid(row=4,column=0,padx=(0,0))
        self.toggle_btn=Button(self.login_frm,image=self.toggle_btn_img,border=0,cursor='hand2',bg=self.whitecolor,
                               command=lambda: self.toggle_password(self.password,self.toggle_btn))
        self.toggle_btn.grid(row=4,column=1,sticky=W)
        Label(self.login_frm, image=self.login_btn, bg=self.bluecolor).grid(row=5, column=0,sticky=W,pady=30)
        Button(self.login_frm, text='L O G I N',font=self.font2,fg=self.bluecolor,padx=38, border=0, cursor='hand2',
               bg=self.greencolor,command=self.login_action).grid(row=5,column=0,sticky=W,pady=30,padx=5)
        Label(self.login_frm, text="DON'T HAVE AN ACCOUNT?", font=self.font2, bg=self.bluecolor, fg=self.whitecolor).grid(row=6, column=0, sticky=W)
        self.signup_btn=Label(self.login_frm, text="SIGN UP", font=self.font5,cursor='hand2', bg=self.bluecolor, fg=self.greencolor)
        self.signup_btn.grid(row=6, column=0,columnspan=2, sticky=E)
        self.signup_btn.bind("<Button-1>",self.go_signup)
        self.signup_btn.bind("<Enter>",self.on_enter)
        self.signup_btn.bind("<Leave>",self.on_leave)



        self.jumbotron=Frame(self.master,bg=self.bluecolor)
        self.jumbotron.grid(row=1,column=2,padx=(80,0),sticky=NW)
        self.jumbo_img=Label(self.jumbotron, image=self.trainimg, bg=self.bluecolor)
        self.jumbo_img.grid(row=0, column=0, sticky=N)
        self.jumbo_head=Label(self.jumbotron, text="LOGIN TO THE APP", font=self.font4, bg=self.bluecolor, fg=self.greencolor)
        self.jumbo_head.grid(row=1, column=0, sticky=N,pady=(10,0))
        self.jumbo_body=Label(self.jumbotron, text="Choose a username and password.\nLogin to the application and\n begin your journey with RAILLY",
                              font=self.font4, bg=self.bluecolor, fg=self.whitecolor)
        self.jumbo_body.grid(row=2,column=0,sticky=N)





        self.signup_frm = Frame(self.master, bg=self.bluecolor)
        # self.signup_frm.grid(row=1, column=1, padx=5, sticky=NW)
        Button(self.signup_frm, image=self.back_btn, border=0, cursor='hand2',command=self.go_back, bg=self.bluecolor).grid(row=0,column=0,sticky=W,pady=(2, 8))
        Label(self.signup_frm, text="S I G N  U P", font=self.font1, bg=self.bluecolor,
              fg=self.whitecolor).grid(row=0, column=0, sticky=NW,columnspan=2, pady=(0, 10),padx=(40,0))

        Label(self.signup_frm, text="F I R S T  N A M E", font=self.font2, bg=self.bluecolor,
              fg=self.greencolor).grid(row=1, column=0,padx=(0,10), sticky=W)
        Label(self.signup_frm,image=self.entryimg2, bg=self.bluecolor,
              fg=self.greencolor).grid(row=2, column=0,padx=(0,10), sticky=W)
        self.f_name=Entry(self.signup_frm, bg=self.whitecolor, width=17, border=0, font=self.font2,fg=self.blackcolor)
        self.f_name.grid(row=2, column=0,padx=(0,10))
        Label(self.signup_frm, text="M I D D L E  N A M E", font=self.font2, bg=self.bluecolor,
              fg=self.greencolor).grid(row=1, column=1,padx=(0,10), sticky=W)
        Label(self.signup_frm,image=self.entryimg2, bg=self.bluecolor,
              fg=self.greencolor).grid(row=2, column=1,padx=(0,10), sticky=W)
        self.m_name=Entry(self.signup_frm, bg=self.whitecolor, width=17, border=0, font=self.font2,fg=self.blackcolor)
        self.m_name.grid(row=2, column=1,padx=(0,10))
        Label(self.signup_frm, text="L A S T  N A M E", font=self.font2, bg=self.bluecolor,
              fg=self.greencolor).grid(row=1, column=2, sticky=W)
        Label(self.signup_frm,image=self.entryimg2, bg=self.bluecolor,
              fg=self.greencolor).grid(row=2, column=2, sticky=W)
        self.l_name=Entry(self.signup_frm, bg=self.whitecolor, width=17, border=0, font=self.font2,fg=self.blackcolor)
        self.l_name.grid(row=2, column=2)
        Label(self.signup_frm, text="E M A I L  A D D R E S S", font=self.font2, bg=self.bluecolor, fg=self.greencolor).grid(
            row=3,pady=(5,0), column=0, sticky=W)
        Label(self.signup_frm, image=self.entryimg, bg=self.bluecolor).grid(row=4, column=0, columnspan=2,sticky=W)
        self.email = Entry(self.signup_frm, bg=self.whitecolor, width=30, border=0, font=self.font2,
                              fg=self.blackcolor)
        self.email.grid(row=4, column=0, columnspan=2,sticky=W,padx=(5,0))
        Label(self.signup_frm, text="P H O N E  N U M B E R", font=self.font2, bg=self.bluecolor, fg=self.greencolor).grid(
            row=5,pady=(5,0), column=0, sticky=W)
        Label(self.signup_frm, image=self.entryimg, bg=self.bluecolor).grid(row=6, column=0, columnspan=2,sticky=W)
        self.phone = Entry(self.signup_frm, bg=self.whitecolor, width=30, border=0, font=self.font2,
                              fg=self.blackcolor)
        self.phone.grid(row=6, column=0, columnspan=2,sticky=W,padx=(5,0))
        Label(self.signup_frm, text="U S E R N A M E (cannot be changed later)", font=self.font2,
              bg=self.bluecolor, fg=self.greencolor).grid(pady=(5,0),
            row=7, column=0,columnspan=2, sticky=W)
        Label(self.signup_frm, image=self.entryimg, bg=self.bluecolor).grid(row=8, column=0, columnspan=2,sticky=W)
        self.username_ent = Entry(self.signup_frm, bg=self.whitecolor, width=30, border=0, font=self.font2,
                              fg=self.blackcolor)
        self.username_ent.grid(row=8, column=0, padx=(5, 0), columnspan=2,sticky=W)
        Label(self.signup_frm, text="P A S S W O R D", font=self.font2, bg=self.bluecolor, fg=self.greencolor).grid(
            row=9, column=0, sticky=W, pady=(5, 0))
        Label(self.signup_frm, image=self.entryimg, bg=self.bluecolor).grid(row=10, column=0, columnspan=2,sticky=W)
        self.password_ent = Entry(self.signup_frm, bg=self.whitecolor, show='•', width=26, border=0, font=self.font2,
                              fg=self.blackcolor)
        self.password_ent.grid(row=10, column=0, padx=(5, 0),columnspan=2,sticky=W)
        self.toggle_btn2=Button(self.signup_frm, image=self.toggle_btn_img, border=0, cursor='hand2', bg=self.whitecolor,
                                command=lambda: self.toggle_password(self.password_ent,self.toggle_btn2))
        self.toggle_btn2.grid(row=10,column=1,padx=(60,0),sticky=W)
        Label(self.signup_frm, image=self.login_btn, bg=self.bluecolor).grid(row=10, column=2, sticky=W)
        Button(self.signup_frm, text='S U B M I T', font=self.font2, fg=self.bluecolor, padx=33, border=0, cursor='hand2',
               bg=self.greencolor,command=self.signup_action).grid(row=10, column=2,padx=(5,0), sticky=W)
        Label(self.signup_frm, image=self.trainimg2, bg=self.bluecolor).grid(row=6, column=2, sticky=N,columnspan=2,rowspan=4)


    def slideshow(self):
        if self.slide==5:
            self.slide=1
        if self.slide==1:
            self.jumbo_img.config(image=self.routeimg)
            self.jumbo_head.config(text='CHOOSE YOUR ROUTE')
            self.jumbo_body.config(text='Choose the origin and destination of\nyour journey and view the route,\nstation information and other details')
        elif self.slide == 2:
            self.jumbo_img.config(image=self.payimg)
            self.jumbo_head.config(text='MAKE PAYMENT')
            self.jumbo_body.config(text='Pay for your ticket via Internet banking,\nbank cards,wallet,the choice is yours')
        elif self.slide==3:
            self.jumbo_img.config(image=self.qrcodeimg)
            self.jumbo_head.config(text='TRAVEL WITHOUT HASSLES')
            self.jumbo_body.config(text='Use your QR ticket to gain\nentry and exit at RAILLY listed\n stations and enjoy a hassle free journey')
        elif self.slide==4:
            self.jumbo_img.config(image=self.trainimg)
            self.jumbo_head.config(text='LOGIN TO THE APP')
            self.jumbo_body.config(text='Choose a username and password.\nLogin to the application and\n begin your journey with RAILLY')
        self.slide+=1
        self.after(3000, self.slideshow)

    def go_back(self):
        self.signup_frm.grid_forget()
        self.login_frm.grid(row=1, column=1, padx=5, sticky=NW)
        self.jumbotron.grid(row=1, column=2, padx=(100, 0), sticky=NW)

    def go_signup(self,e):
        self.login_frm.grid_forget()
        self.jumbotron.grid_forget()
        self.signup_frm.grid(row=1, column=1, padx=5, sticky=NW)

    def on_enter(self,e):
        self.signup_btn.config(fg=self.whitecolor)
    def on_leave(self,e):
        self.signup_btn.config(fg=self.greencolor)

    def toggle_password(self,widget,toggle_btn):
        if widget.cget('show') == '':
            widget.config(show='•')
            toggle_btn.config(image=self.toggle_btn_img)
        else:
            widget.config(show='')
            toggle_btn.config(image=self.toggle_btn_img2)

    def login_action(self):
        check=fn.login_validate(self.username.get().lower(),self.password.get().lower())
        if check:
            self.reset(0)
            messagebox.showinfo('Login Successful',f'Welcome {check[0][3].title()}')
        else:
            messagebox.showerror('Login Failed','Invalid username or password')

    def signup_action(self):
        fname=self.f_name.get().lower()
        mname=self.m_name.get().lower()
        lname=self.l_name.get().lower()
        user=self.username_ent.get().lower()
        mail=self.email.get().lower()
        phone=self.phone.get().lower()
        password=self.password_ent.get().lower()
        data=[(user,lname,mname,fname,mail,phone,password)]
        if fname!='' and mname!='' and lname!='' and user!='' and mail!='' and phone!='' and password!='':
            if not fn.check_name(fname):
                messagebox.showerror('ERROR', 'invalid first name')
            elif not fn.check_name(mname):
                messagebox.showerror('ERROR', 'invalid middle name')
            elif not fn.check_name(fname):
                messagebox.showerror('ERROR', 'invalid last name')
            elif not fn.check_email(mail):
                messagebox.showerror('ERROR', 'invalid Email address')
            elif not fn.check_phone(phone):
                messagebox.showerror('ERROR', 'invalid phone number')
            elif not fn.check_name(user):
                messagebox.showerror('ERROR', 'invalid username')
            elif fn.check_username_exists(user):
                messagebox.showerror('ERROR', 'username taken')
            elif fn.check_email_exists(mail):
                messagebox.showerror('ERROR', 'email already exists')
            elif fn.check_phone_exists(phone):
                messagebox.showerror('ERROR', 'phone number already exists')
            elif not fn.check_pass(password):
                messagebox.showerror('ERROR','INVALID PASSWORD')
            else:
                fn.register_customer(data)
                messagebox.showinfo('SUCCESS','Sign up success, proceed to login')
                self.reset(1)
                self.go_back()

        else:
            messagebox.showerror('ERROR','ALL FIELDS ARE REQUIRED')

    def reset(self,n):
        if n==0:
            self.username.delete(0,END)
            self.password.delete(0,END)
        else:
            self.f_name.delete(0,END)
            self.m_name.delete(0,END)
            self.l_name.delete(0,END)
            self.username_ent.delete(0,END)
            self.email.delete(0,END)
            self.phone.delete(0,END)
            self.password_ent.delete(0,END)






root=Tk()
root.resizable(0, 0)
root.configure(bg='#110445')
root.geometry('800x500+283+110')
root.title('R A I L L Y')
# root.overrideredirect(1)
apk = LandingPage(root)
apk.mainloop()