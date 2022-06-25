import datetime
from tkinter import *
from tkinter import font as f
from tkcalendar import *
# from tkinter.ttk import Progressbar
# import datetime as dt
# from dateutil.relativedelta import relativedelta
# import time
# from PIL import ImageTk, Image
# import random
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import funtions as fn
# import threading



class AdminPage(Frame):
    def __init__(self, master):
        super(AdminPage, self).__init__(master)
        self.master=master
        self.grid()

        self.font1=f.Font(family='Yu Gothic UI Semilight', size=30, weight='normal')
        self.font2 = f.Font(family='Yu Gothic UI Semilight', size=13, weight='normal')
        self.font3 = f.Font(family='Yu Gothic UI Light', size=9)
        self.font4 = f.Font(family='Yu Gothic UI Light', size=13)
        self.font5 = f.Font(family='Yu Gothic UI Light', size=11, weight='normal')
        self.font6 = f.Font(family='Yu Gothic UI Light', size=13, weight='normal',underline=True)

        self.blackcolor = '#080808'
        self.redcolor = '#E50914'
        self.darkredcolor='#BF0000'
        self.bluecolor = "#110445"
        self.darkbluecolor="#080B35"
        self.greycolor = '#242124'
        self.greencolor='#00f18c'
        self.darkgreencolor='#48BF91'
        self.whitecolor = 'white'
        self.darkgreycolor = '#221F1F'
        self.lightgreycolor = '#F1F1F1'
        self.lightergreycolor = '#ECECEC'
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TCombobox', fieldbackground=self.lightgreycolor, background=self.lightgreycolor,
                        foreground=self.greencolor)
        style.map('TCombobox', fieldbackground=[('readonly', self.lightgreycolor)])
        style.map('TCombobox', selectbackground=[('readonly', self.lightgreycolor)])
        style.map('TCombobox', foreground=[('readonly', self.greencolor)])
        self.create_widgets()
        self.selected = [True, False, False, False]
        self.fn = [self.f1, self.f2, self.f3, self.f4]
        self.navbtns = [self.dashbtn, self.trainsbtn, self.schedulebtn, self.addadminbtn]
        self.navimg = [self.dashicon1,self.trainicon1,self.scheduleicon1,self.addusericon1]
        self.navimg2 = [self.dashicon2,self.trainicon2,self.scheduleicon2,self.addusericon2]

    def create_widgets(self):
        self.logo = ImageTk.PhotoImage(Image.open("trainplus.png"))
        self.navphoto=ImageTk.PhotoImage(Image.open("admin-with-cogwheels.png"))
        self.dashicon1 = ImageTk.PhotoImage(Image.open("dashboard.png"))
        self.dashicon2 = ImageTk.PhotoImage(Image.open("dashboard (1).png"))
        self.trainicon1 = ImageTk.PhotoImage(Image.open("train (4).png"))
        self.trainicon2 = ImageTk.PhotoImage(Image.open("train (3).png"))
        self.scheduleicon1 = ImageTk.PhotoImage(Image.open("date.png"))
        self.scheduleicon2 = ImageTk.PhotoImage(Image.open("date (1).png"))
        self.addusericon1 = ImageTk.PhotoImage(Image.open("invite.png"))
        self.addusericon2 = ImageTk.PhotoImage(Image.open("invite (1).png"))
        self.addimg = ImageTk.PhotoImage(Image.open("add.png"))

        # NAVIGATION BAR SEGMENT
        self.navbar=Frame(self.master,width=250,height=670,bg=self.bluecolor)
        self.navbar.grid(row=0,column=0,sticky=NW)
        Label(self.navbar,bg=self.bluecolor,text='ADMIN',font=self.font1,fg=self.greencolor).grid(row=1,column=0,columnspan=2,pady=(10,40))
        Label(self.navbar,bg=self.bluecolor,image=self.navphoto).grid(row=0,column=0,columnspan=2,padx=70,pady=(20,10))

        self.dashbtn=Button(self.navbar,text=' D A S H B O A R D',image=self.dashicon2,compound=LEFT,bg=self.bluecolor,
                            font=self.font4,width=220,command=lambda :self.cmd(0),fg=self.greencolor,border=0,cursor='hand2')
        self.dashbtn.grid(row=2,column=1,pady=(6,0),sticky=NW)
        self.f1=Frame(self.navbar,width=6,height=35,bg=self.greencolor)
        self.f1.grid(row=2,column=0,pady=(6,0),sticky=NW)
        self.dashbtn.bind("<Enter>",lambda e: self.nav_enter(0))
        self.dashbtn.bind("<Leave>",lambda e: self.nav_leave(0))


        self.trainsbtn=Button(self.navbar,text=' T R A I N S\t',image=self.trainicon1,compound=LEFT,bg=self.bluecolor,
                            font=self.font4,width=220,fg=self.whitecolor,command=lambda :self.cmd(1),border=0,cursor='hand2')
        self.trainsbtn.grid(row=3,column=1,pady=(6,0),sticky=NW)
        self.f2=Frame(self.navbar,width=6,height=35,bg=self.bluecolor)
        self.f2.grid(row=3,column=0,pady=(6,0),sticky=NW)
        self.trainsbtn.bind("<Enter>",lambda e: self.nav_enter(1))
        self.trainsbtn.bind("<Leave>",lambda e: self.nav_leave(1))

        self.schedulebtn=Button(self.navbar,text=' S C H E D U L E S',image=self.scheduleicon1,compound=LEFT,bg=self.bluecolor,
                            font=self.font4,width=207,fg=self.whitecolor,command=lambda :self.cmd(2),border=0,cursor='hand2')
        self.schedulebtn.grid(row=4,column=1,pady=(6,0),sticky=NW)
        self.f3=Frame(self.navbar,width=6,height=35,bg=self.bluecolor)
        self.f3.grid(row=4,column=0,pady=(6,0),sticky=NW)
        self.schedulebtn.bind("<Enter>",lambda e: self.nav_enter(2))
        self.schedulebtn.bind("<Leave>",lambda e: self.nav_leave(2))

        self.addadminbtn=Button(self.navbar,text=' A D M I N\t',image=self.addusericon1,compound=LEFT,bg=self.bluecolor,
                            font=self.font4,width=220,fg=self.whitecolor,command=lambda :self.cmd(3),border=0,cursor='hand2')
        self.addadminbtn.grid(row=5,column=1,pady=(6,0),sticky=NW)
        self.f4=Frame(self.navbar,width=6,height=35,bg=self.bluecolor)
        self.f4.grid(row=5,column=0,pady=(6,0),sticky=NW)
        self.addadminbtn.bind("<Enter>",lambda e: self.nav_enter(3))
        self.addadminbtn.bind("<Leave>",lambda e: self.nav_leave(3))

        self.logoutbtn=Button(self.navbar,text='L O G O U T',bg=self.darkbluecolor,font=self.font4,fg=self.whitecolor,
                              command=lambda: self.master.destroy(),border=0,padx=87,pady=5,cursor='hand2')
        self.logoutbtn.grid(row=6,column=0,columnspan=2,pady=(180,10))

        # TRAIN MANAGEMENT PAGE
        self.trainspage=Frame(self.master,bg=self.whitecolor)
        self.trainspage.grid(row=0,column=1,sticky=NSEW)
        Label(self.trainspage,bg=self.whitecolor,text='MANAGE TRAINS',font=self.font1,
              fg=self.bluecolor).grid(row=0,column=0,sticky=NW,padx=(20),pady=(0,30))
        self.traintop=Frame(self.trainspage,bg=self.whitecolor)
        self.traintop.grid(row=1,column=0,columnspan=2,sticky=NW,pady=(0,40))
        self.newtrain=Button(self.traintop,text='ADD NEW TRAIN',bg=self.whitecolor,fg=self.bluecolor,border=0,cursor='hand2',font=self.font4)
        self.newtrain.grid(row=1,column=0,padx=(26,0),sticky=NW)
        self.trf1=Frame(self.traintop,bg=self.whitecolor,width=134,height=3)
        self.trf1.grid(row=2,column=0,padx=(26,0),sticky=NW)
        self.viewtrain=Button(self.traintop,text='VIEW TRAINS',padx=10,bg=self.lightgreycolor,fg=self.bluecolor,border=0,cursor='hand2',font=self.font4)
        self.viewtrain.grid(row=1,column=1,padx=(0,550),sticky=NW)
        self.trf2=Frame(self.traintop,bg=self.bluecolor,width=124,height=3)
        self.trf2.grid(row=2,column=1,padx=(0,0),sticky=NW)
        ttk.Separator(self.traintop,orient='horizontal').grid(row=3,column=0,columnspan=2,padx=26,sticky=EW)


        # ADD NEW TRAIN PAGE
        self.newtrainfrm = Frame(self.trainspage, bg=self.whitecolor)
        # self.newtrainfrm.grid(row=2, column=0, sticky=NW, padx=26, columnspan=2)
        Label(self.newtrainfrm,text='TRAIN NAME: ',bg=self.whitecolor,fg=self.bluecolor,font=self.font4).grid(row=0,column=0,pady=(25,0),sticky=NW)
        self.trainname=Entry(self.newtrainfrm,bg=self.whitecolor,width=30,fg=self.darkgreencolor,border=0,font=self.font4)
        self.trainname.grid(row=0,column=1,pady=(25,0),sticky=NW)
        # ttk.Separator(self.newtrainfrm,orient='horizontal').grid(row=1,column=1,sticky=EW)
        Frame(self.newtrainfrm,bg=self.bluecolor,width=300,height=2).grid(row=1,column=1,sticky=NW)
        Label(self.newtrainfrm,text='FIRST CLASS CAPACITY: ',bg=self.whitecolor,fg=self.bluecolor,font=self.font4).grid(row=2,column=0,pady=(25,0), sticky=NW)
        self.fc_capacity=Entry(self.newtrainfrm,bg=self.whitecolor,width=6,fg=self.darkgreencolor,border=0,font=self.font4)
        self.fc_capacity.grid(row=2,column=1,pady=(25,0),sticky=NW)
        Frame(self.newtrainfrm, bg=self.bluecolor, width=60, height=2).grid(row=3, column=1, sticky=NW)
        Label(self.newtrainfrm,text='SECOND CLASS CAPACITY: ',bg=self.whitecolor,fg=self.bluecolor,font=self.font4).grid(row=4,column=0,pady=(25,0), sticky=NW)
        self.bc_capacity=Entry(self.newtrainfrm,bg=self.whitecolor,width=6,fg=self.darkgreencolor,border=0,font=self.font4)
        self.bc_capacity.grid(row=4,column=1,pady=(25,0),sticky=NW)
        Frame(self.newtrainfrm, bg=self.bluecolor, width=60, height=2).grid(row=5, column=1, sticky=NW)
        Label(self.newtrainfrm,text='REGULAR COACH CAPACITY: ',bg=self.whitecolor,fg=self.bluecolor,font=self.font4).grid(row=6,column=0,pady=(25,0), sticky=NW)
        self.rc_capacity=Entry(self.newtrainfrm,bg=self.whitecolor,width=6,fg=self.darkgreencolor,border=0,font=self.font4)
        self.rc_capacity.grid(row=6,column=1,pady=(25,0),sticky=NW)
        Frame(self.newtrainfrm, bg=self.bluecolor, width=60, height=2).grid(row=7, column=1, sticky=NW)
        self.addtrainbtn=Button(self.newtrainfrm,text='S U B M I T',pady=3,padx=5,bg=self.greencolor,font=self.font4,
                                fg=self.whitecolor,border=0,cursor='hand2')
        self.addtrainbtn.grid(row=8,column=1,sticky=NE)



        # VIEW LIST OF TRAINS PAGE
        self.viewtrainfrm = Frame(self.trainspage, bg=self.whitecolor, width=774, height=200)
        self.scrolly = Scrollbar(self.viewtrainfrm)
        self.scrolly.pack(side=RIGHT, fill=Y)
        self.scrollx = Scrollbar(self.viewtrainfrm, orient='horizontal')
        self.scrollx.pack(side=BOTTOM, fill=X)
        self.trainstree = ttk.Treeview(self.viewtrainfrm, height=13, yscrollcommand=self.scrolly.set,
                                        xscrollcommand=self.scrollx.set,
                                        style="mystyle.Treeview", selectmode='browse')
        self.trainstree.pack(fill=X)
        self.viewtrainfrm.pack_propagate(0)
        self.scrolly.config(command=self.trainstree.yview)
        self.scrollx.config(command=self.trainstree.xview)
        self.load_treeview_data()
        self.viewtrainfrm.grid(row=2,column=0, sticky=NW, padx=26, columnspan=2)



    def load_treeview_data(self):
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=self.font5,
                        rowheight=30)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", borderwidth=1, background=self.bluecolor,
                        foreground=self.whitecolor, relief='flat',
                        font=self.font4)  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        header = ("Train number", "Train name", "F.C. capacity", "B.C. capacity", "R.C. capacity")
        self.trainstree['columns'] = (header)
        self.trainstree.column("#0", width=0, stretch=NO)
        for i in header:
            self.trainstree.column(i, anchor=W, width=120, minwidth=130)
        # self.trainstree.column("source", anchor=W, width=100, minwidth=200)
        # self.trainstree.column("destination", anchor=W, width=100, minwidth=200)
        # self.trainstree.column("Passenger name", anchor=W, width=100, minwidth=200)

        self.trainstree.heading("#0", text="", anchor=W)
        for i in header:
            self.trainstree.heading(i, text=i.upper(), anchor=W)
        data = fn.get_all_trains()
        counter = 0
        for record in data:
            self.trainstree.insert(parent='', index='end', iid=counter, values=(record))
            counter += 1



    def cmd(self,n):
        for i in range(len(self.navbtns)):
            self.navbtns[i].config(fg=self.whitecolor, image=self.navimg[i])
            self.fn[i].config(bg=self.bluecolor)
            self.selected[i] = False
        self.navbtns[n].config(fg=self.greencolor, image=self.navimg2[n])
        self.fn[n].config(bg=self.greencolor)
        self.selected[n] = True
    def nav_enter(self, n):
        if self.selected[n]:
            self.navbtns[n].config(fg=self.darkgreencolor)
            self.fn[n].config(bg=self.darkgreencolor)
        else:
            self.navbtns[n].config(fg=self.greencolor,image=self.navimg2[n])
            self.fn[n].config(bg=self.greencolor)

    def nav_leave(self, n):
        if self.selected[n]:
            self.navbtns[n].config(fg=self.greencolor)
            self.fn[n].config(bg=self.greencolor)
        else:
            self.navbtns[n].config(fg=self.whitecolor, image=self.navimg[n])
            self.fn[n].config(bg=self.bluecolor)


root=Tk()
root.resizable(0, 0)
root.configure(bg='white')
root.geometry('1100x670+133+10')
root.title('TRAIN PLUS+')
root.iconbitmap('hyperloop.ico')
apk = AdminPage(root)
apk.mainloop()