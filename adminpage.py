# import datetime
import datetime
from tkinter import *
from tkinter import font as f
from tkcalendar import *
# from tkinter.ttk import Progressbar
import datetime as dt
from dateutil.relativedelta import relativedelta
# import time
# from PIL import ImageTk, Image
# import random
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import funtions as fn
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
# import threading



class AdminPage(Frame):
    def __init__(self, master,profile):
        super(AdminPage, self).__init__(master)
        self.master=master
        self.grid()

        self.font1=f.Font(family='Yu Gothic UI Semilight', size=30, weight='normal')
        self.font2 = f.Font(family='Yu Gothic UI Semilight', size=13, weight='normal')
        self.font3 = f.Font(family='Yu Gothic UI Light', size=9)
        self.font4 = f.Font(family='Yu Gothic UI Light', size=13)
        self.font5 = f.Font(family='Yu Gothic UI Light', size=11, weight='normal')
        self.font6 = f.Font(family='Yu Gothic UI Semilight', size=11, weight='normal')
        self.font7=f.Font(family='Yu Gothic UI Semilight', size=20, weight='normal')
        self.font8=f.Font(family='Yu Gothic UI Semilight', size=15, weight='normal')

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

        self.username=profile[0]
        self.deficit=(10-len(self.username))*10.5
        self.statevar=StringVar()
        self.trainid=''
        self.sourcelist=fn.get_sources()
        self.destlist=fn.get_all_destinations()
        self.trainlst=fn.get_train_list()
        self.sourcevar=StringVar()
        self.destvar=StringVar()
        self.trainvar=StringVar()
        self.gendervar=StringVar()
        self.gend='male'
        self.date = dt.datetime.now()
        self.maxdate=self.date+relativedelta(years=0,months=2,days=0)
        self.create_widgets()
        self.selected = [True, False, False, False]
        self.fn = [self.f1, self.f2, self.f3, self.f4]
        self.navbtns = [self.dashbtn, self.trainsbtn, self.schedulebtn, self.addadminbtn]
        self.navimg = [self.dashicon1,self.trainicon1,self.scheduleicon1,self.addusericon1]
        self.navimg2 = [self.dashicon2,self.trainicon2,self.scheduleicon2,self.addusericon2]
        self.pages=[self.dashpage,self.trainspage,self.schedulepage,self.adminpage]
        self.master.protocol("WM_DELETE_WINDOW",self.close_all)

    def create_widgets(self):
        self.logo = ImageTk.PhotoImage(Image.open("trainplus.png"))
        self.logout = ImageTk.PhotoImage(Image.open("profile-user.png"))
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
        self.down=ImageTk.PhotoImage(Image.open("drop down button.png"))
        self.toggle_btn_img = ImageTk.PhotoImage(Image.open("view.png"))
        self.toggle_btn_img2 = ImageTk.PhotoImage(Image.open("hide.png"))
        self.back_img=ImageTk.PhotoImage(Image.open("back-button2.png"))
        self.dash_panel = ImageTk.PhotoImage(Image.open("admin_dashboard_img.png"))
        self.lightgreybg1 = ImageTk.PhotoImage(Image.open("lightgreybg1.png"))
        self.lightgreybg2 = ImageTk.PhotoImage(Image.open("lightgreybg2.png"))



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
                              command=self.logout_action,border=0,padx=87,pady=5,cursor='hand2')
        self.logoutbtn.grid(row=6,column=0,columnspan=2,pady=(180,10))


        # DASHBOARD
        self.dashpage = Frame(self.master, bg=self.whitecolor)
        self.dashpage.grid(row=0, column=1, sticky=NSEW)
        Label(self.dashpage, bg=self.whitecolor, text='DASHBOARD', font=self.font1,
              fg=self.bluecolor).grid(row=0, column=0, sticky=NW, padx=(20), pady=(0, 5))
        self.mainmenu = Menubutton(self.dashpage, text=self.username.upper(), compound=RIGHT, image=self.logout,
                                   border=0, font=self.font2, fg=self.bluecolor, cursor='hand2', bg=self.whitecolor)
        self.mainmenu.grid(row=0, column=1, padx=(380 + self.deficit, 21), sticky=W, pady=(0, 5))
        self.mainmenu.menu = Menu(self.mainmenu, tearoff=0)
        self.mainmenu['menu'] = self.mainmenu.menu
        self.mainmenu.menu.add_radiobutton(label='PROFILE', value='PROFILE', font=self.font2)
        ttk.Separator(self.dashpage, orient='horizontal').grid(row=1, column=0, columnspan=2, padx=26, sticky=EW)


        # DASHBOARD STATISTICS
        self.statspage = Frame(self.dashpage, bg=self.whitecolor)
        self.statspage.grid(row=2, column=0, sticky=NW,columnspan=2, padx=(20, 0))
        self.dashpanel=Frame(self.statspage,bg=self.whitecolor)
        self.dashpanel.grid(row=0,column=0,sticky=NW)
        Label(self.dashpanel, bg=self.whitecolor, image=self.lightgreybg1).grid(row=0, column=0, columnspan=2,
                                                                              pady=(10, 0))
        Label(self.dashpanel, bg=self.whitecolor, image=self.lightgreybg2).grid(row=0, column=2,pady=(10, 0),padx=(10,0))
        Label(self.dashpanel, bg=self.whitecolor, image=self.lightgreybg1).grid(row=1, column=1, columnspan=2,
                                                                              pady=(10, 10),padx=(10,0))
        Label(self.dashpanel, bg=self.whitecolor, image=self.lightgreybg2).grid(row=1, column=0,pady=(10, 10))
        self.continue_btn=Button(self.dashpanel,text=' Tickets>> ',font=self.font4,bg=self.bluecolor,
                                 fg=self.greencolor,border=0,cursor='hand2',command=lambda: self.cmx(0))
        self.continue_btn.grid(row=2, column=2,sticky=NE)

        self.pieframe=Frame(self.dashpanel,bg=self.lightgreycolor)
        self.pieframe.grid(row=0, column=2,pady=(10, 0),padx=(10,0))
        self.pieframe2=Frame(self.dashpanel,bg=self.lightgreycolor)
        self.pieframe2.grid(row=1, column=0,pady=(10, 0),padx=(10,0))
        self.barframe=Frame(self.dashpanel,bg=self.lightgreycolor)
        self.barframe.grid(row=0, column=0,columnspan=2,pady=(10, 10),padx=(10,0))
        self.barframe2=Frame(self.dashpanel,bg=self.lightgreycolor)
        self.barframe2.grid(row=1, column=1,columnspan=2,pady=(10, 10),padx=(10,0))
        self.plotall()




        # TICKETS PAGE
        self.tickets_page = Frame(self.dashpage, bg=self.whitecolor)
        # self.tickets_page.grid(row=2, column=0, sticky=NW,columnspan=2)
        Button(self.tickets_page, image=self.back_img, border=0, cursor='hand2',
               bg=self.whitecolor,command=lambda: self.cmx(1)).grid(row=0, column=0, sticky=W, pady=(25, 10), padx=(30, 0))
        Label(self.tickets_page, text="ALL TICKETS", font=self.font7, bg=self.whitecolor,
              fg=self.bluecolor).grid(row=0, column=0, sticky=NW, pady=(20, 10), padx=(70, 0))
        self.treeframe = Frame(self.tickets_page, bg=self.whitecolor, width=780, height=270)
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=self.font5,
                        rowheight=30)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", borderwidth=1, background=self.bluecolor,
                        foreground=self.whitecolor, relief='flat',
                        font=self.font5)  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        self.treescrolly = Scrollbar(self.treeframe)
        self.treescrolly.pack(side=RIGHT, fill=Y)
        self.treescrollx = Scrollbar(self.treeframe, orient='horizontal')
        self.treescrollx.pack(side=BOTTOM, fill=X)
        self.ticketstree = ttk.Treeview(self.treeframe, height=13, yscrollcommand=self.treescrolly.set,
                                        xscrollcommand=self.treescrollx.set,
                                        style="mystyle.Treeview", selectmode='browse')
        self.ticketstree.pack(fill=X)
        self.treeframe.pack_propagate(0)
        self.treescrolly.config(command=self.ticketstree.yview)
        self.treescrollx.config(command=self.ticketstree.xview)
        self.load_treeview_data()
        self.treeframe.grid(row=1, column=0, sticky=NW, padx=(30, 20), columnspan=2)




        # TRAIN MANAGEMENT PAGE
        self.trainspage=Frame(self.master,bg=self.whitecolor)
        # self.trainspage.grid(row=0,column=1,sticky=NSEW)
        Label(self.trainspage,bg=self.whitecolor,text='MANAGE TRAINS',font=self.font1,
              fg=self.bluecolor).grid(row=0,column=0,sticky=NW,padx=(20),pady=(0,30))
        self.traintop=Frame(self.trainspage,bg=self.whitecolor)
        self.traintop.grid(row=1,column=0,columnspan=2,sticky=NW,pady=(0,40))
        self.newtrain=Button(self.traintop,text='ADD NEW TRAIN',bg=self.whitecolor,fg=self.bluecolor,border=0,
                             command=self.newtrain_action,cursor='hand2',font=self.font4)
        self.newtrain.grid(row=1,column=0,padx=(26,0),sticky=NW)
        self.trf1=Frame(self.traintop,bg=self.whitecolor,width=134,height=3)
        self.trf1.grid(row=2,column=0,padx=(26,0),sticky=NW)
        self.viewtrain=Button(self.traintop,text='VIEW TRAINS',padx=10,bg=self.lightgreycolor,fg=self.bluecolor,border=0,
                              command=self.viewtrain_action,cursor='hand2',font=self.font4)
        self.viewtrain.grid(row=1,column=1,padx=(0,550),sticky=NW)
        self.trf2=Frame(self.traintop,bg=self.bluecolor,width=124,height=3)
        self.trf2.grid(row=2,column=1,padx=(0,0),sticky=NW)
        ttk.Separator(self.traintop,orient='horizontal').grid(row=3,column=0,columnspan=2,padx=26,sticky=EW)



        # ADD NEW TRAIN PAGE
        self.newtrainfrm = Frame(self.trainspage, bg=self.whitecolor)
        self.newtrainfrm.grid(row=2, column=0, sticky=NW, padx=26, columnspan=2)
        Label(self.newtrainfrm,text='TRAIN NAME: ',bg=self.whitecolor,fg=self.bluecolor,font=self.font4).grid(row=0,column=0,pady=(25,0),sticky=NW)
        self.trainname=Entry(self.newtrainfrm,bg=self.whitecolor,width=30,fg=self.darkgreencolor,border=0,font=self.font4)
        self.trainname.grid(row=0,column=1,pady=(25,0),sticky=SW)
        # ttk.Separator(self.newtrainfrm,orient='horizontal').grid(row=1,column=1,sticky=EW)
        Frame(self.newtrainfrm,bg=self.bluecolor,width=272,height=2).grid(row=1,column=1,sticky=NW)
        Label(self.newtrainfrm,text='FIRST CLASS CAPACITY: ',bg=self.whitecolor,fg=self.bluecolor,font=self.font4).grid(row=2,column=0,pady=(25,0), sticky=NW)
        self.fc_capacity=Spinbox(self.newtrainfrm,from_=10,to=100,bg=self.whitecolor,fg=self.bluecolor,font=self.font4,border=0,
                          state='readonly',repeatinterval=50,width=5)
        self.fc_capacity.grid(row=2,column=1,pady=(25,0),sticky=SW)
        Frame(self.newtrainfrm, bg=self.bluecolor, width=60, height=2).grid(row=3, column=1, sticky=NW)
        Label(self.newtrainfrm,text='SECOND CLASS CAPACITY: ',bg=self.whitecolor,fg=self.bluecolor,font=self.font4).grid(row=4,column=0,pady=(25,0), sticky=NW)
        self.bc_capacity=Spinbox(self.newtrainfrm,from_=10,to=100,bg=self.whitecolor,fg=self.bluecolor,font=self.font4,border=0,
                          repeatinterval=50,state='readonly',width=5)
        self.bc_capacity.grid(row=4,column=1,pady=(25,0),sticky=SW)
        Frame(self.newtrainfrm, bg=self.bluecolor, width=60, height=2).grid(row=5, column=1, sticky=NW)
        Label(self.newtrainfrm,text='REGULAR COACH CAPACITY: ',bg=self.whitecolor,fg=self.bluecolor,font=self.font4).grid(row=6,column=0,pady=(25,0), sticky=NW)
        self.rc_capacity=Spinbox(self.newtrainfrm,from_=10,to=100,bg=self.whitecolor,fg=self.bluecolor,font=self.font4,border=0,
                          repeatinterval=50,width=5,state='readonly',cursor='hand2')
        self.rc_capacity.grid(row=6,column=1,pady=(25,0),sticky=SW)
        Frame(self.newtrainfrm, bg=self.bluecolor, width=60, height=2).grid(row=7, column=1, sticky=NW)
        self.addtrainbtn=Button(self.newtrainfrm,text='S U B M I T',pady=3,padx=5,bg=self.greencolor,font=self.font4,
                                fg=self.whitecolor,command=self.add_train_action,border=0,cursor='hand2')
        self.addtrainbtn.grid(row=8,column=1,sticky=NE)


        # VIEW LIST OF TRAINS PAGE
        self.viewtrainpage=Frame(self.trainspage, bg=self.whitecolor)
        self.viewtrainpage.grid(row=2,column=0, sticky=NW, padx=26, columnspan=3)
        self.viewtrainfrm = Frame(self.viewtrainpage, bg=self.whitecolor, width=774, height=200)
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
        self.load_trains_tree()
        # self.newtrainfrm.grid_forget()
        self.viewtrainfrm.grid(row=0,column=0, sticky=NW, columnspan=3)
        self.edittrainbtn=Button(self.viewtrainpage,text='E D I T',padx=5,bg=self.greencolor,font=self.font4,
                                fg=self.whitecolor,command=self.editbtn_action,border=0,cursor='hand2')
        self.edittrainbtn.grid(row=1,column=2,sticky=NE,pady=20)
        self.deletetrainbtn=Button(self.viewtrainpage,text='D I S A B L E',padx=5,bg=self.redcolor,font=self.font4,
                                command=self.disable_train,fg=self.whitecolor,border=0,cursor='hand2')
        self.deletetrainbtn.grid(row=1,column=1,sticky=NE,padx=(0,80),pady=20,columnspan=2)

        # EDIT TRAIN DETAILS SEGMENT
        self.edittrainfrm=Frame(self.trainspage,bg=self.whitecolor)
        # self.edittrainfrm.grid(row=2,column=0, sticky=NW, padx=26, columnspan=3)
        Label(self.edittrainfrm, text='TRAIN NAME: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=0,column=0,pady=(25,0),sticky=NW)
        self.edittrainname = Entry(self.edittrainfrm, bg=self.whitecolor, width=30, fg=self.darkgreencolor, border=0,
                               font=self.font4)
        self.edittrainname.grid(row=0, column=1, pady=(25, 0), sticky=SW)
        Frame(self.edittrainfrm, bg=self.bluecolor, width=272, height=2).grid(row=1, column=1, sticky=NW)
        Label(self.edittrainfrm, text='FIRST CLASS CAPACITY: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=2, column=0, pady=(25, 0), sticky=NW)
        self.editfc_capacity = Spinbox(self.edittrainfrm, from_=10, to=100, bg=self.whitecolor, fg=self.bluecolor,
                                   font=self.font4, border=0,state='readonly',
                                   repeatinterval=50, width=5)
        self.editfc_capacity.grid(row=2, column=1, pady=(25, 0), sticky=SW)
        Frame(self.edittrainfrm, bg=self.bluecolor, width=60, height=2).grid(row=3, column=1, sticky=NW)
        Label(self.edittrainfrm, text='SECOND CLASS CAPACITY: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=4, column=0, pady=(25, 0), sticky=NW)
        self.editbc_capacity = Spinbox(self.edittrainfrm, from_=10, to=100, bg=self.whitecolor, fg=self.bluecolor,
                                   font=self.font4, border=0,state='readonly',
                                   repeatinterval=50, width=5)
        self.editbc_capacity.grid(row=4, column=1, pady=(25, 0), sticky=SW)
        Frame(self.edittrainfrm, bg=self.bluecolor, width=60, height=2).grid(row=5, column=1, sticky=NW)
        Label(self.edittrainfrm, text='REGULAR COACH CAPACITY: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=6, column=0, pady=(25, 0), sticky=NW)
        self.editrc_capacity = Spinbox(self.edittrainfrm, from_=10, to=100, bg=self.whitecolor, fg=self.bluecolor,
                                   font=self.font4, border=0,state='readonly',
                                   repeatinterval=50, width=5, cursor='hand2')
        self.editrc_capacity.grid(row=6, column=1, pady=(25, 0), sticky=SW)
        Frame(self.edittrainfrm, bg=self.bluecolor, width=60, height=2).grid(row=7, column=1, sticky=NW)
        items=['active','out of service']
        self.statevar.set(items[0])
        self.statemenu = Menubutton(self.edittrainfrm, text=items[0].upper(),border=0,font=self.font2,fg=self.whitecolor,
                                    cursor='hand2', bg=self.greencolor)
        self.statemenu.grid(row=8, column=0,sticky=NW,pady=(25, 0))

        self.statemenu.menu = Menu(self.statemenu, tearoff=0)
        self.statemenu['menu'] = self.statemenu.menu
        for i in range(len(items)):
            self.statemenu.menu.add_radiobutton(label=items[i],value=items[i], variable=self.statevar,
                                               command=lambda: self.statemenu_action(self.statevar.get()),font=self.font2)
        self.back_editbtn = Button(self.edittrainfrm, text='R E T U R N', padx=5, bg=self.redcolor,
                                  font=self.font4,command=self.viewtrain_action,
                                  fg=self.whitecolor, border=0, cursor='hand2')
        self.back_editbtn.grid(row=9, column=1, sticky=NW,pady=15)
        self.save_editbtn = Button(self.edittrainfrm, text='S A V E', padx=5, bg=self.greencolor,
                                  font=self.font4,command=self.save_edit_action,
                                  fg=self.whitecolor, border=0, cursor='hand2')
        self.save_editbtn.grid(row=9, column=1, sticky=NE,pady=15)



        # SCHEDULE MANAGEMENT PAGE
        self.schedulepage = Frame(self.master, bg=self.whitecolor)
        # self.schedulepage.grid(row=0,column=1,sticky=NSEW)
        Label(self.schedulepage, bg=self.whitecolor, text='MANAGE SCHEDULES', font=self.font1,
              fg=self.bluecolor).grid(row=0, column=0, sticky=NW, padx=(20), pady=(0, 30))
        self.scheduletop = Frame(self.schedulepage, bg=self.whitecolor)
        self.scheduletop.grid(row=1, column=0, columnspan=2, sticky=NW, pady=(0, 40))
        self.newschedule = Button(self.scheduletop, text='NEW SCHEDULE', padx=3, bg=self.lightgreycolor, fg=self.bluecolor, border=0,
                               command=self.newschedule_action, cursor='hand2', font=self.font4)
        self.newschedule.grid(row=1, column=0, padx=(26, 0), sticky=NW)
        self.shf1 = Frame(self.scheduletop, bg=self.bluecolor, width=134, height=3)
        self.shf1.grid(row=2, column=0, padx=(26, 0), sticky=NW)
        self.viewschedule = Button(self.scheduletop, text='VIEW SCHEDULES', padx=3, bg=self.whitecolor, fg=self.bluecolor,
                                border=0,
                                command=self.viewschedule_action, cursor='hand2', font=self.font4)
        self.viewschedule.grid(row=1, column=1, padx=(0, 530), sticky=NW)
        self.shf2 = Frame(self.scheduletop, bg=self.whitecolor, width=144, height=3)
        self.shf2.grid(row=2, column=1, padx=(0, 0), sticky=NW)
        ttk.Separator(self.scheduletop, orient='horizontal').grid(row=3, column=0, columnspan=2, padx=26, sticky=EW)

        # VIEW LIST OF SCHEDULES PAGE
        self.viewschedulepage = Frame(self.schedulepage, bg=self.whitecolor)
        # self.viewschedulepage.grid(row=2, column=0, sticky=NW, padx=26, columnspan=3)
        self.viewschedulefrm = Frame(self.viewschedulepage, bg=self.whitecolor, width=774, height=300)
        self.scrolly1 = Scrollbar(self.viewschedulefrm)
        self.scrolly1.pack(side=RIGHT, fill=Y)
        self.scrollx1 = Scrollbar(self.viewschedulefrm, orient='horizontal')
        self.scrollx1.pack(side=BOTTOM, fill=X)
        self.schedulestree = ttk.Treeview(self.viewschedulefrm, height=15, yscrollcommand=self.scrolly1.set,
                                       xscrollcommand=self.scrollx1.set,
                                       style="mystyle.Treeview", selectmode='browse')
        self.schedulestree.pack(fill=X)
        self.viewschedulefrm.pack_propagate(0)
        self.scrolly1.config(command=self.schedulestree.yview)
        self.scrollx1.config(command=self.schedulestree.xview)
        self.load_schedule_tree()
        # self.newschedulefrm.grid_forget()
        self.viewschedulefrm.grid(row=0, column=0, sticky=NW, columnspan=3)
        self.editschedulebtn = Button(self.viewschedulepage, text='E D I T', padx=5, bg=self.greencolor, font=self.font4,
                                   fg=self.whitecolor, command=self.editbtn_action, border=0, cursor='hand2')
        # self.editschedulebtn.grid(row=1, column=2, sticky=NE, pady=20)
        self.deleteschedulebtn = Button(self.viewschedulepage, text='E N D', padx=5, bg=self.redcolor,
                                     font=self.font4,
                                     command=self.disable_train, fg=self.whitecolor, border=0, cursor='hand2')
        # self.deleteschedulebtn.grid(row=1, column=1, sticky=NE, padx=(0, 80), pady=20, columnspan=2)


        # NEW SCHEDULE SEGMENT
        self.newschedulefrm = Frame(self.schedulepage, bg=self.whitecolor)
        self.newschedulefrm.grid(row=2, column=0, sticky=NW, padx=26, columnspan=2)
        Label(self.newschedulefrm, text='SOURCE: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=0,column=0,pady=(0,0),sticky=NW)
        self.source=Menubutton(self.newschedulefrm, text=self.sourcelist[0].upper(),border=0,font=self.font6,fg=self.whitecolor,
                                    cursor='hand2', bg=self.greencolor)
        self.source.grid(row=0, column=1,sticky=NW,pady=(0, 0))

        self.source.menu = Menu(self.source, tearoff=0)
        self.source['menu'] = self.source.menu
        for i in range(len(self.sourcelist)):
            self.source.menu.add_radiobutton(label=self.sourcelist[i],value=self.sourcelist[i], variable=self.sourcevar,
                                             command=lambda: self.source_action(self.sourcevar.get()),font=self.font2)
        self.sourcevar.set(self.sourcelist[0])
        Label(self.newschedulefrm, text='DESTINATION: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=0,column=2,pady=(0,0),padx=(10,0),sticky=NW)
        self.destination=Menubutton(self.newschedulefrm, text=self.destlist[0].upper(),border=0,font=self.font6,fg=self.whitecolor,
                                    cursor='hand2', bg=self.greencolor)
        self.destination.grid(row=0, column=3,sticky=NW,pady=(0, 0))

        self.destination.menu = Menu(self.destination, tearoff=0)
        self.destination['menu'] = self.destination.menu
        self.destvar.set(self.destlist[0])

        for i in range(len(self.destlist)):
            self.destination.menu.add_radiobutton(label=self.destlist[i],value=self.destlist[i], variable=self.destvar,
                                                  command=lambda: self.destination_action(self.destvar.get()),font=self.font2)

        self.addlocation = Button(self.newschedulefrm, text=' NEW LOCATION', bg=self.greencolor,font=self.font6,
                                  image=self.addimg,compound=LEFT, fg=self.whitecolor, border=0, cursor='hand2',
                                  command=self.addlocation_action)
        self.addlocation.grid(row=2,column=1,sticky=NW,pady=(15,0))

        Label(self.newschedulefrm, text='TRAIN NAME: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=3, column=0, pady=(15, 0), sticky=NW)
        self.trainmenu = Menubutton(self.newschedulefrm, text=self.trainlst[0].upper(), border=0, font=self.font6,
                                      fg=self.whitecolor,cursor='hand2', bg=self.greencolor)
        self.trainmenu.grid(row=3, column=1, sticky=NW, pady=(15, 0))

        self.trainmenu.menu = Menu(self.trainmenu, tearoff=0)
        self.trainmenu['menu'] = self.trainmenu.menu
        self.trainvar.set(self.trainlst[0])
        for i in range(len(self.trainlst)):
            self.trainmenu.menu.add_radiobutton(label=self.trainlst[i], value=self.trainlst[i], variable=self.trainvar,
                                                  command=lambda : self.trainmenu_action(self.trainvar.get()),font=self.font2)

        Label(self.newschedulefrm, text='START DATE: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=4,column=0,pady=(20,0),sticky=NW)
        self.startdate = DateEntry(self.newschedulefrm, selectmode='day', mindate=self.date, maxdate=self.maxdate,
                                    cursor='hand2', font=self.font2,
                                    year=dt.date.today().year)
        self.startdate['state'] = 'readonly'
        self.startdate.grid(row=4, column=1, pady=(20, 0), sticky=NW)

        Label(self.newschedulefrm, text='END DATE: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=4,column=2,padx=10,pady=(20,0),sticky=NW)

        self.enddate = DateEntry(self.newschedulefrm, selectmode='day', mindate=self.date+relativedelta(years=0,months=0,days=1), maxdate=self.maxdate,
                                    cursor='hand2', font=self.font2,
                                    year=dt.date.today().year)
        self.enddate['state'] = 'readonly'
        self.enddate.grid(row=4, column=3, pady=(20, 0), sticky=NW,columnspan=2)
        Label(self.newschedulefrm, text='TIME: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=5,column=0,pady=(20,0),sticky=NW)
        Label(self.newschedulefrm, text='hour: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=5,column=1,pady=(20,0),sticky=NW)
        self.hour = Spinbox(self.newschedulefrm, from_=0, to=24, bg=self.lightgreycolor, fg=self.greencolor,
                                   font=self.font4, border=0,
                                   state='readonly', repeatinterval=50, width=3)
        self.hour.grid(row=5, column=1, pady=(20, 0),padx=(50,0), sticky=NW)
        Label(self.newschedulefrm, text='minute: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=5,column=1,padx=(100,0),pady=(20,0),sticky=NW)
        self.minute = Spinbox(self.newschedulefrm, from_=0, to=59, bg=self.lightgreycolor, fg=self.greencolor,
                                   font=self.font4, border=0,
                                   state='readonly', repeatinterval=50, width=3)
        self.minute.grid(row=5, column=1, pady=(20, 0),padx=(160,0), sticky=NW)

        Label(self.newschedulefrm, text='F. CLASS PRICE: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=6,column=0,pady=(20,0),sticky=NW)
        self.fc_price=Spinbox(self.newschedulefrm, from_=100, to=10000, bg=self.lightgreycolor, fg=self.greencolor,
                                   font=self.font4, border=0,increment=10,
                                   state='readonly', repeatinterval=10, width=10)
        self.fc_price.grid(row=6, column=1, pady=(20, 0), sticky=NW)
        Label(self.newschedulefrm, text='B. CLASS PRICE: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=7,column=0,pady=(20,0),sticky=NW)
        self.bc_price=Spinbox(self.newschedulefrm, from_=100, to=10000, bg=self.lightgreycolor, fg=self.greencolor,
                                   font=self.font4, border=0,increment=10,
                                   state='readonly', repeatinterval=10, width=10)
        self.bc_price.grid(row=7, column=1, pady=(20, 0), sticky=NW)
        Label(self.newschedulefrm, text='R. COACH PRICE: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=8,column=0,pady=(20,0),sticky=NW)
        self.rc_price=Spinbox(self.newschedulefrm, from_=100, to=10000, bg=self.lightgreycolor, fg=self.greencolor,
                                   font=self.font4, border=0,increment=10,
                                   state='readonly', repeatinterval=10, width=10)
        self.rc_price.grid(row=8, column=1, pady=(20, 0), sticky=NW)
        self.schedule_submit = Button(self.newschedulefrm, text='S U B M I T',padx=30, bg=self.greencolor,font=self.font2,
                                      command=self.submit_schedule,fg=self.whitecolor, border=0, cursor='hand2')
        self.schedule_submit.grid(row=9,column=3,sticky=NE,pady=(25,0),columnspan=2,padx=(0,0))



        # ADD ADMIN PAGE
        self.adminpage = Frame(self.master, bg=self.whitecolor)
        # self.adminpage.grid(row=0, column=1, sticky=NSEW)
        self.admintop=Frame(self.adminpage,bg=self.whitecolor)
        self.admintop.grid(row=0,column=0,sticky=NW)
        Label(self.admintop, bg=self.whitecolor, text='ADD NEW ADMIN', font=self.font1,
              fg=self.bluecolor).grid(row=0, column=0, sticky=NW, padx=(20,470), pady=(0, 30))
        ttk.Separator(self.admintop, orient='horizontal').grid(row=1, column=0, padx=26, sticky=EW)

        self.signup_frm = Frame(self.adminpage, bg=self.whitecolor)
        self.signup_frm.grid(row=1, column=0, padx=25, sticky=NW)

        Label(self.signup_frm, text="F I R S T  N A M E", font=self.font2, bg=self.whitecolor,
              fg=self.bluecolor).grid(row=1, column=0, padx=(0, 10), sticky=NW,pady=(25, 0))

        self.f_name = Entry(self.signup_frm, bg=self.lightgreycolor, width=17, border=0, font=self.font2,
                            fg=self.bluecolor)
        self.f_name.grid(row=2, column=0, padx=(0, 10),pady=(5, 0),sticky=NW)
        Label(self.signup_frm, text="M I D D L E  N A M E", font=self.font2, bg=self.whitecolor,
              fg=self.bluecolor).grid(row=1, column=1, padx=(0, 10), sticky=NW,pady=(25, 0))

        self.m_name = Entry(self.signup_frm, bg=self.lightgreycolor, width=17, border=0, font=self.font2,
                            fg=self.bluecolor)
        self.m_name.grid(row=2, column=1, padx=(0, 10),pady=(5, 0))
        Label(self.signup_frm, text="L A S T  N A M E", font=self.font2, bg=self.whitecolor,
              fg=self.bluecolor).grid(row=1, column=2, sticky=NW,pady=(25,0))

        self.l_name = Entry(self.signup_frm, bg=self.lightgreycolor, width=17, border=0, font=self.font2,
                            fg=self.bluecolor)
        self.l_name.grid(row=2, column=2,pady=(5, 0),sticky=NW)
        Label(self.signup_frm, text="E M A I L  A D D R E S S", font=self.font2, bg=self.whitecolor,
              fg=self.bluecolor).grid(row=3, pady=(20, 0), column=0, columnspan=2,sticky=W)
        self.email = Entry(self.signup_frm, bg=self.lightgreycolor, width=30, border=0, font=self.font2,
                           fg=self.bluecolor)
        self.email.grid(row=4, column=0, columnspan=2,pady=(5, 0), sticky=NW)

        menuitems = ['MALE', 'FEMALE', 'OTHER']
        self.gender = Menubutton(self.signup_frm, text=menuitems[0], compound=RIGHT, image=self.down,
                                 border=0, font=self.font2, fg=self.bluecolor, cursor='hand2', bg=self.lightgreycolor)
        self.gender.grid(row=3, column=2, sticky=SW,rowspan=2, padx=5)

        self.gender.menu = Menu(self.gender, tearoff=0)
        self.gender['menu'] = self.gender.menu
        for i in range(len(menuitems)):
            self.gender.menu.add_radiobutton(label=menuitems[i], value=menuitems[i], variable=self.gendervar,
                                             command=lambda: self.gender_btn_action(self.gendervar.get()),
                                             font=self.font2)
        Label(self.signup_frm, text="P H O N E  N U M B E R", font=self.font2, bg=self.whitecolor,
              fg=self.bluecolor).grid(
            row=5, pady=(20, 0), column=0, columnspan=2,sticky=W)
        self.phone = Entry(self.signup_frm, bg=self.lightgreycolor, width=30, border=0, font=self.font2,
                           fg=self.bluecolor)
        self.phone.grid(row=6, column=0, columnspan=2,pady=(5, 0), sticky=NW)
        Label(self.signup_frm, text="U S E R N A M E (cannot be changed later)", font=self.font2,
              bg=self.whitecolor, fg=self.bluecolor).grid(pady=(20, 0),
                                                          row=7, column=0, columnspan=2, sticky=W)
        self.username_ent = Entry(self.signup_frm, bg=self.lightgreycolor, width=30, border=0, font=self.font2,
                                  fg=self.bluecolor)
        self.username_ent.grid(row=8, column=0, columnspan=2,pady=(5, 0), sticky=NW)
        Label(self.signup_frm, text="P A S S W O R D", font=self.font2, bg=self.whitecolor, fg=self.bluecolor).grid(
            row=9, column=0, sticky=NW, columnspan=2,pady=(20, 0))
        self.password_ent = Entry(self.signup_frm, bg=self.lightgreycolor, show='•', width=26, border=0, font=self.font2,
                                  fg=self.bluecolor)
        self.password_ent.grid(row=10, column=0, columnspan=2,pady=(5, 0), sticky=NW)
        self.toggle_btn2 = Button(self.signup_frm, image=self.toggle_btn_img, border=0, cursor='hand2',
                                  bg=self.lightgreycolor,
                                  command=lambda: self.toggle_password(self.password_ent, self.toggle_btn2))
        self.toggle_btn2.grid(row=10, column=1, padx=(64, 0), sticky=NW,pady=(5, 0))
        Button(self.signup_frm, text='S U B M I T', font=self.font2, fg=self.bluecolor, padx=33, border=0,
               cursor='hand2',
               bg=self.greencolor, command=self.signup_action).grid(row=11, column=2, padx=(5, 0), sticky=NW,pady=(10, 0))

    def cmx(self,n):
        self.statspage.grid_forget()
        self.tickets_page.grid_forget()
        if n==0:
            self.tickets_page.grid(row=2, column=0, sticky=NW, columnspan=2)
        else:
            self.statspage.grid(row=2, column=0, sticky=NW, columnspan=2, padx=(20, 0))

    def plotall(self):
        pie=fn.plot_pie()
        chart = FigureCanvasTkAgg(pie, master=self.pieframe)
        chart.draw()
        chart.get_tk_widget().grid(row=0, column=0)

        pie2=fn.plot_pie2()
        chart = FigureCanvasTkAgg(pie2, master=self.pieframe2)
        chart.draw()
        chart.get_tk_widget().grid(row=0, column=0)

        bar=fn.plot_barchart()
        chart = FigureCanvasTkAgg(bar, master=self.barframe)
        chart.draw()
        chart.get_tk_widget().grid(row=0, column=0)

        bar2=fn.plot_barchart()
        chart = FigureCanvasTkAgg(bar2, master=self.barframe2)
        chart.draw()
        chart.get_tk_widget().grid(row=0, column=0)


    def load_treeview_data(self):
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=self.font5, rowheight=30)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", borderwidth=1, background=self.bluecolor,
                        foreground=self.whitecolor, relief='flat',
                        font=self.font5)  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        header=('username',"ticket number","seat number","train number","Passenger name","departure date",
                                     "departure time","seat class","source","destination")
        self.ticketstree['columns']=(header)
        self.ticketstree.column("#0", width=0, stretch=NO)
        for i in header:
            self.ticketstree.column(i,anchor=W, width=70,minwidth=140)
        self.ticketstree.column("source",anchor=W, width=100,minwidth=200)
        self.ticketstree.column("destination",anchor=W, width=100,minwidth=200)
        self.ticketstree.column("Passenger name",anchor=W, width=100,minwidth=200)

        self.ticketstree.heading("#0", text="", anchor=W)
        for i in header:
            self.ticketstree.heading(i, text=i.upper(),anchor=W)
        data=fn.get_all_tickets()
        counter = 0
        for record in data:
            self.ticketstree.insert(parent='', index='end', iid=counter, values=(record))
            counter += 1

    def toggle_password(self,widget,toggle_btn):
        if widget.cget('show') == '':
            widget.config(show='•')
            toggle_btn.config(image=self.toggle_btn_img)
        else:
            widget.config(show='')
            toggle_btn.config(image=self.toggle_btn_img2)

    def signup_action(self):
        fname=self.f_name.get().lower()
        mname=self.m_name.get().lower()
        lname=self.l_name.get().lower()
        user=self.username_ent.get().lower()
        gend=self.gend.lower()
        type=1
        mail=self.email.get().lower()
        phone=self.phone.get().lower()
        password=self.password_ent.get()
        data=[(user,lname,mname,fname,gend,mail,phone,password,type)]
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
                messagebox.showinfo('SUCCESS','Admin added successfully')
                self.reset()

        else:
            messagebox.showerror('ERROR','ALL FIELDS ARE REQUIRED')

    def reset(self):
        self.f_name.delete(0,END)
        self.m_name.delete(0,END)
        self.l_name.delete(0,END)
        self.username_ent.delete(0,END)
        self.email.delete(0,END)
        self.phone.delete(0,END)
        self.password_ent.delete(0,END)


    def addlocation_action(self):
        top=Toplevel(self.master)
        top.configure(bg=self.whitecolor)
        top.geometry('300x110+533+284')
        top.resizable(False,False)
        Label(top, text='Enter new location: ', bg=self.whitecolor, fg=self.bluecolor,
              font=self.font4).grid(row=0, column=0, pady=10)
        ent=Entry(top,bg=self.lightgreycolor,fg=self.bluecolor,font=self.font4,width=33,border=0)
        ent.grid(row=1,column=0)
        save = Button(top, text='SAVE',padx=30, bg=self.greencolor,font=self.font4, border=0, cursor='hand2',
                                      command=lambda : self.newlocation(ent.get(),top),fg=self.whitecolor)
        save.grid(row=2,column=0)

    def get_time(self,h,m):
        if h<10:
            hh=f'0{h}'
        else:
            hh=f'{h}'
        if m<10:
            mm=f'0{m}'
        else:
            mm=f'{m}'
        return f'{hh}:{mm}:00'


    def submit_schedule(self):
        source=self.sourcevar.get()
        dest=self.destvar.get()
        train=self.trainvar.get()
        startdate=self.startdate.get_date()
        enddate=self.enddate.get_date()
        hour=int(self.hour.get())
        minute=int(self.minute.get())
        fc=int(self.fc_price.get())
        bc=int(self.bc_price.get())
        rc = int(self.rc_price.get())
        time=self.get_time(hour,minute)
        data=[fn.generate_schedule_num(),fn.get_trainid(train),source,dest,startdate,enddate,time,fc,bc,rc]
        print(data)
        shed=fn.validate_schedule(source,dest,time,startdate,enddate)
        if shed:
            messagebox.showerror("ERROR",f'Conflict of dates in schdule: {shed}')
        else:
            fn.register_schedule(data)
            messagebox.showinfo("SUCCESS",'Schedule created successfully')


    def newlocation(self,location,top):
        if location.strip():
            location = location.lower()
            self.sourcelist.append(location)
            self.destlist.append(location)
            self.destination.config(text=location.upper())
            self.destination.menu.add_radiobutton(label=location,value=location, variable=self.destvar,font=self.font2,
                                                  command=lambda: self.destination_action(self.destvar.get()))
            self.destvar.set(location)
            self.source.menu.add_radiobutton(label=location,value=location, variable=self.sourcevar,font=self.font2,
                                                  command=lambda: self.source_action(self.sourcevar.get()))
            top.destroy()

    def source_action(self,source):
        self.source.config(text=source.upper())
        if source in self.destlist:
            self.destlist.remove(source)
            dest=self.destlist
            self.destination.config(text=dest[0].upper())
            self.destination.menu = Menu(self.destination, tearoff=0)
            self.destination['menu'] = self.destination.menu
            for i in range(len(dest)):
                self.destination.menu.add_radiobutton(label=dest[i],value=dest[i], variable=self.destvar,font=self.font2,
                                                      command=lambda: self.destination_action(self.destvar.get()))
            self.destvar.set(dest[0])
            self.destlist.append(source)

    def destination_action(self,dest):
        self.destination.config(text=dest.upper())

    def trainmenu_action(self,train):
        self.trainmenu.config(text=train.upper())

    def newschedule_action(self):
        self.viewschedule.config(bg=self.whitecolor)
        self.newschedule.config(bg=self.lightgreycolor)
        self.shf1.config(bg=self.bluecolor)
        self.shf2.config(bg=self.whitecolor)
        self.viewschedulepage.grid_forget()
        self.newschedulefrm.grid(row=2, column=0, sticky=NW, padx=26, columnspan=3)

    def viewschedule_action(self):
        self.viewschedule.config(bg=self.lightgreycolor)
        self.newschedule.config(bg=self.whitecolor)
        self.shf1.config(bg=self.whitecolor)
        self.shf2.config(bg=self.bluecolor)
        self.newschedulefrm.grid_forget()
        self.viewschedulepage.grid(row=2, column=0, sticky=NW, padx=26, columnspan=3)


    def load_schedule_tree(self):
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=self.font4,
                        rowheight=30)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", borderwidth=1, background=self.bluecolor,
                        foreground=self.whitecolor, relief='flat',
                        font=self.font4)  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        header = ('schedule num','train num','source','destination','start date','end date','time',
                  'f.c. price','b.c. price','r.c. price')
        self.schedulestree['columns'] = (header)
        self.schedulestree.column("#0", width=0, stretch=NO)
        for i in header:
            self.schedulestree.column(i, anchor=W, width=130, minwidth=130)
        self.schedulestree.column('source',anchor=W, width=130, minwidth=240)
        self.schedulestree.column('destination',anchor=W, width=130, minwidth=240)

        self.schedulestree.heading("#0", text="", anchor=W)
        for i in header:
            self.schedulestree.heading(i, text=i.upper(), anchor=W)
        data = fn.get_all_schedules()
        counter = 0
        for record in data:
            self.schedulestree.insert(parent='', index='end', iid=counter, values=(record))
            counter += 1


    def save_edit_action(self):
        tid=self.trainid
        name=self.edittrainname.get()
        fc=int(self.editfc_capacity.get())
        bc=int(self.editbc_capacity.get())
        rc=int(self.editrc_capacity.get())
        status=self.statevar.get()
        val=fn.validate_train(name)
        if name.strip()!='':
            if val and val[0] != self.trainid:
                messagebox.showerror("ERROR",'TRAIN ALREADY EXISTS')
            else:
                fn.edit_train(tid,name,fc,bc,rc,status)
                messagebox.showinfo("SUCCESS","TRAIN DETAILS UPDATED SUCCESSFULLY")
                self.clear_treeview()
                self.load_trains_tree()
                self.viewtrain_action()
        else:
            messagebox.showerror("ERROR","PLEASE FILL ALL DETAILS")

    def add_train_action(self):
        name=self.trainname.get()
        fc=int(self.fc_capacity.get())
        bc=int(self.bc_capacity.get())
        rc=int(self.rc_capacity.get())
        if name.strip()!='':
            if fn.validate_train(name):
                messagebox.showerror("ERROR",'TRAIN ALREADY EXISTS')
            else:
                fn.add_new_train(name,fc,bc,rc)
                messagebox.showinfo("SUCCESS","TRAIN ADDED SUCCESSFULLY")
                self.trainlst.append(name)
                self.trainmenu.menu.add_radiobutton(label=name, value=name,
                                                    variable=self.trainvar,
                                                    command=lambda: self.trainmenu_action(self.trainvar.get()),
                                                    font=self.font2)
                self.trainname.delete(0,END)
                self.clear_treeview()
                self.load_trains_tree()
        else:
            messagebox.showerror("ERROR","TRAIN NAME IS REQUIRED")

    def disable_train(self):
        selected = self.trainstree.focus()
        values = self.trainstree.item(selected, 'values')
        if values:
            fn.disable_train(values[0])
            self.clear_treeview()
            self.load_trains_tree()

    def editbtn_action(self):
        selected = self.trainstree.focus()
        values = self.trainstree.item(selected, 'values')
        if values:
            self.trainid=values[0]
            self.edittrainname.delete(0,END)
            self.editfc_capacity.delete(0,END)
            self.editbc_capacity.delete(0,END)
            self.editrc_capacity.delete(0,END)
            self.edittrainname.insert(0,values[1])
            self.editfc_capacity.insert(0,values[2])
            self.editbc_capacity.insert(0,values[3])
            self.editrc_capacity.insert(0,values[4])
            self.statevar.set(values[5])
            self.statemenu_action(values[5])
            self.viewtrainpage.grid_forget()
            self.edittrainfrm.grid(row=2, column=0, sticky=NW, padx=26, columnspan=3)

    def statemenu_action(self,state):
        if state=='active':
            self.statemenu.config(text=state.upper(),bg=self.greencolor)
        elif state=='out of service':
            self.statemenu.config(text=state.upper(),bg=self.redcolor)

    def newtrain_action(self):
        self.newtrain.config(bg=self.lightgreycolor)
        self.trf1.config(bg=self.bluecolor)
        self.viewtrain.config(bg=self.whitecolor)
        self.trf2.config(bg=self.whitecolor)
        self.viewtrainpage.grid_forget()
        self.edittrainfrm.grid_forget()
        self.newtrainfrm.grid(row=2, column=0, sticky=NW, padx=26, columnspan=2)
    def viewtrain_action(self):
        self.newtrain.config(bg=self.whitecolor)
        self.trf1.config(bg=self.whitecolor)
        self.viewtrain.config(bg=self.lightgreycolor)
        self.trf2.config(bg=self.bluecolor)
        self.newtrainfrm.grid_forget()
        self.edittrainfrm.grid_forget()
        self.viewtrainpage.grid(row=2, column=0, sticky=NW, padx=26, columnspan=2)

    def clear_treeview(self):
        for i in self.trainstree.get_children():
            self.trainstree.delete(i)

    def load_trains_tree(self):
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=self.font5,
                        rowheight=30)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", borderwidth=1, background=self.bluecolor,
                        foreground=self.whitecolor, relief='flat',
                        font=self.font4)  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        header = ("Train number", "Train name", "F.C. capacity", "B.C. capacity", "R.C. capacity","status")
        self.trainstree['columns'] = (header)
        self.trainstree.column("#0", width=0, stretch=NO)
        for i in header:
            self.trainstree.column(i, anchor=W, width=120, minwidth=130)

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
            self.pages[i].grid_forget()
            self.navbtns[i].config(fg=self.whitecolor, image=self.navimg[i])
            self.fn[i].config(bg=self.bluecolor)
            self.selected[i] = False
        self.pages[n].grid(row=0, column=1, sticky=NSEW)
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

    def gender_btn_action(self,gend):
        self.gender.config(text=gend)
        self.gend=gend.lower()

    def close_all(self):
        if messagebox.askokcancel("QUIT","Are you sure you want to quit?"):
            self.master.master.destroy()

    def logout_action(self):
        self.master.destroy()
        self.master.master.deiconify()
# root=Tk()
# root.resizable(0, 0)
# root.configure(bg='white')
# root.geometry('1100x670+133+10')
# root.title('TRAIN PLUS+')
# root.iconbitmap('hyperloop.ico')
# apk = AdminPage(root)
# apk.mainloop()