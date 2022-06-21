import datetime
from tkinter import *
from tkinter import font as f
from tkcalendar import *
import datetime as dt
from dateutil.relativedelta import relativedelta
import time
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

        self.font1=f.Font(family='Yu Gothic UI Semilight', size=30, weight='normal')
        self.font2 = f.Font(family='Yu Gothic UI Semilight', size=13, weight='normal')
        self.font3 = f.Font(family='Yu Gothic UI Light', size=9)
        self.font4 = f.Font(family='Yu Gothic UI Light', size=13)
        self.font5 = f.Font(family='Yu Gothic UI Light', size=11, weight='normal')
        self.font6 = f.Font(family='Yu Gothic UI Light', size=13, weight='normal',underline=True)

        self.blackcolor = '#080808'
        self.redcolor = '#E50914'
        self.darkredcolor='#ED4B3A'
        self.bluecolor = "#110445"
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
        self.username='sugarpops'
        self.l_name='egbudom'
        self.f_name='raphael'
        self.m_name='chidindu'
        self.email='egbudomraphael@gmail.com'
        self.phone_num='08091516236'
        self.deficit=(10-len(self.username))*8.5
        self.regular_price=2000
        self.business_price=self.regular_price*2
        self.firstclass_price=self.regular_price*3
        self.source=fn.get_sources()
        # self.destination=['Obafemi Awolowo Station','Samuel Ladoke Akintola Station','Wole Soyinka Station',
        #                   'Babatunde Raji Fashola Station','Mobolaji Johnson Station']
        self.sourcevar=StringVar()
        self.destinationvar=StringVar()
        self.go_time=['8:00','10:00','12:00','14:00','16:30']
        self.return_time=['9:00','11:00','13:00','15:00','18:30']
        self.go_timevar=StringVar()
        self.return_timevar=StringVar()
        self.menuvar=StringVar()
        self.numvar=IntVar()
        self.classval='first class'
        self.classval2='fc'
        self.childvar=StringVar()
        self.gendervar=StringVar()
        self.gend='male'
        self.sourcedate=[]
        self.return_date=[]
        self.remembervar=BooleanVar()
        self.date = dt.datetime.now()
        self.maxdate=self.date+relativedelta(years=0,months=2,days=0)
        self.slide=0
        self.create_widgets()
        self.fill_card_data()
        # self.class_btns_action('FIRST CLASS')


    def create_widgets(self):
        self.logo = ImageTk.PhotoImage(Image.open("railly logo green.png"))
        self.logout = ImageTk.PhotoImage(Image.open("profile-user.png"))
        self.entrybg=ImageTk.PhotoImage(Image.open("img_textBox0.png"))
        self.entrybg2=ImageTk.PhotoImage(Image.open("img_textBox0.png").resize((343,69),))
        self.entryimg = ImageTk.PhotoImage(Image.open("textBox1.png").resize((250, 30)))
        self.entryimg2 = ImageTk.PhotoImage(Image.open("textBox1.png").resize((70, 30)))
        self.entryimg3 = ImageTk.PhotoImage(Image.open("textBox1.png").resize((300, 30)))
        self.entryimg4 = ImageTk.PhotoImage(Image.open("textBox1.png").resize((300, 30)))
        self.entryimg5 = ImageTk.PhotoImage(Image.open("textBox1.png").resize((200, 30)))
        self.down=ImageTk.PhotoImage(Image.open("drop down button.png"))
        self.switch = ImageTk.PhotoImage(Image.open("img1.png"))#.transpose(Image.ROTATE_90)
        self.next_img=ImageTk.PhotoImage(Image.open("img4.png"))
        self.cirle = ImageTk.PhotoImage(Image.open("circle.png").resize((12,12),))
        self.cirle1=ImageTk.PhotoImage(Image.open("circle.png"))
        self.cirle2 = ImageTk.PhotoImage(Image.open("circle2.png").resize((20,20),))
        self.dest_img = ImageTk.PhotoImage(Image.open("point2.png"))
        self.backarrow=ImageTk.PhotoImage(Image.open("backarrow.png").resize((50,50),))
        self.date_img = ImageTk.PhotoImage(Image.open("calendar.png"))
        self.regular=ImageTk.PhotoImage(Image.open("regular.png"))
        self.business=ImageTk.PhotoImage(Image.open("business.png"))
        self.firstclass=ImageTk.PhotoImage(Image.open("firstclass.png"))
        self.availble=ImageTk.PhotoImage(Image.open("available button.png").resize((23,23),))
        self.unavailable=ImageTk.PhotoImage(Image.open("indicator_unavailable.png"))
        self.selected=ImageTk.PhotoImage(Image.open("indicator_available.png"))
        self.oneway_img = ImageTk.PhotoImage(Image.open("img1.png").transpose(Image.ROTATE_90))
        self.return_img = ImageTk.PhotoImage(Image.open("backarrow.png").resize((50,50),).transpose(Image.ROTATE_180))
        self.premium = ImageTk.PhotoImage(Image.open("insurance.png"))
        self.forward=ImageTk.PhotoImage(Image.open("fast-forward.png").resize((32,32),))
        self.backward = ImageTk.PhotoImage(Image.open("fast-forward-1.png"))
        self.roundrect=ImageTk.PhotoImage(Image.open("greybg_train_journey.png").resize((343,120),))
        self.seatspace = ImageTk.PhotoImage(Image.open("base train bg.png").resize((340,180),))
        self.pic = ImageTk.PhotoImage(Image.open("high-speed-train.png"))
        self.captain = ImageTk.PhotoImage(Image.open("police (1).png").resize((64,64),))
        self.captain2 = ImageTk.PhotoImage(Image.open("police (2).png").resize((64,64),))
        self.premium2 = ImageTk.PhotoImage(Image.open("insurance.png").resize((64,64),))
        self.captain3 = ImageTk.PhotoImage(Image.open("police (4).png").resize((64,64),))
        self.relax = ImageTk.PhotoImage(Image.open("relax.png"))
        self.visacard=ImageTk.PhotoImage(Image.open("visa.png"))
        self.paypalcard=ImageTk.PhotoImage(Image.open("paypal.png"))
        self.americacard=ImageTk.PhotoImage(Image.open("american-express.png"))
        self.card=ImageTk.PhotoImage(Image.open("credit-card.png"))
        self.back_img=ImageTk.PhotoImage(Image.open("back-button2.png"))
        self.toggle_btn_img = ImageTk.PhotoImage(Image.open("view.png"))
        self.toggle_btn_img2 = ImageTk.PhotoImage(Image.open("hide.png"))
        self.login_btn = ImageTk.PhotoImage(Image.open("loginButton.png").resize((150,35)))




        # NAVIGATION BAR SEGMENT
        self.navbar=Frame(self.master,bg=self.bluecolor,width=1000,height=200)
        self.navbar.grid(row=0,column=0,sticky=NW)

        # LOGO
        self.logo_btn = Button(self.navbar, image=self.logo,border=0,cursor='hand2',command=lambda: self.page_switcher(0),bg=self.bluecolor)
        self.logo_btn.grid(row=0,column=0,pady=10,sticky=NW)
        self.username_display=Label(self.navbar,text=self.username.upper(),font=self.font2,bg=self.bluecolor,fg=self.greencolor)
        # self.username_display.grid(row=0,column=1,sticky=E,padx=(740+self.deficit,0))

        # MENU ITEMS
        menuitems=['PROFILE','TICKETS','LOGOUT']
        self.mainmenu = Menubutton(self.navbar, text=self.username.upper(),compound=RIGHT,image=self.logout,
                                   border=0,font=self.font2,fg=self.greencolor,cursor='hand2', bg=self.bluecolor)
        self.mainmenu.grid(row=0, column=2,padx=(730+self.deficit,21),sticky=E)

        self.mainmenu.menu = Menu(self.mainmenu, tearoff=0)
        self.mainmenu['menu'] = self.mainmenu.menu
        for i in range(len(menuitems)):
            self.mainmenu.menu.add_radiobutton(label=menuitems[i],value=menuitems[i], variable=self.menuvar,
                                               command=lambda: self.mainmenu_action(self.menuvar.get()),font=self.font2)

        # LANDING PAGE
        self.landing_page=Frame(self.master,bg=self.bluecolor)
        self.landing_page.grid(row=1,column=0,sticky=NW)
        Label(self.landing_page, image=self.captain, bg=self.bluecolor).grid(row=0,padx=(20,0), column=0,sticky=NW)
        Label(self.landing_page,text=f'WELCOME BACK {self.f_name.upper()}!',font=self.font1,bg=self.bluecolor,fg=self.greencolor).grid(row=0,column=1,columnspan=2,sticky=NW)
        text='In case you forgot, RAILLY our little app, has\n made train booking your LAGOS-IBADAN\n metro booking easy and user friendly...'
        Label(self.landing_page,text=text,font=self.font2,bg=self.bluecolor,fg=self.greencolor).grid(row=1,column=2,pady=(15,10),padx=(450,0),sticky=NE)
        Label(self.landing_page, image=self.captain2, bg=self.bluecolor).grid(row=1, column=3,pady=(15,10),sticky=NE)
        text2='Make quick transactions without having to put\n your card details everytime you wish to make\n payment, with our secure cloud data storage...'
        Label(self.landing_page, image=self.premium2, bg=self.bluecolor).grid(row=2,padx=(20,0), column=0,sticky=NW)
        Label(self.landing_page,text=text2,font=self.font2,bg=self.bluecolor,fg=self.greencolor).grid(row=2,column=1,sticky=NW,columnspan=2)
        text3='Our system is advanced enough to allow\n a single user to book a slots for family and/or\n friends, up to a whooping number of 6...'
        Label(self.landing_page,text=text3,font=self.font2,bg=self.bluecolor,fg=self.greencolor).grid(row=3,column=2,pady=(15,10),padx=(450,0),sticky=NE)
        Label(self.landing_page, image=self.captain3, bg=self.bluecolor).grid(row=3, column=3,pady=(15,10),sticky=NE)
        text4='Sit back, relax and watch RAILLY do its thing,\n thanks for using our app and have a great travel!'
        Label(self.landing_page, image=self.relax, bg=self.bluecolor).grid(row=4,padx=(20,0), column=0,sticky=NW,pady=(15,0))
        Label(self.landing_page,text=text4,font=self.font2,bg=self.bluecolor,fg=self.greencolor).grid(row=4,column=1,sticky=NW,pady=(15,0),columnspan=2)
        self.continue_btn=Button(self.landing_page,text='Click here to continue>>>',font=self.font6,bg=self.bluecolor,
                                 fg=self.greencolor,border=0,cursor='hand2',command=lambda: self.page_switcher(1))
        self.continue_btn.grid(row=5, column=2,padx=(450,0),sticky=NE)
        self.continue_btn.bind("<Enter>",self.on_enter)
        self.continue_btn.bind("<Leave>",self.on_leave)



        # BOOK FLIGHT PAGE
        self.book_page=Frame(self.master,bg=self.whitecolor)
        # self.book_page.grid(row=1,column=0,sticky=NW)
        
        # PAGE COUNTER AT THE TOP
        self.marker = Frame(self.book_page,bg=self.whitecolor,width=80)
        self.marker.grid(row=0,column=0,sticky=N,columnspan=2,pady=10,padx=(50,0))
        self.where=Label(self.marker, image=self.cirle2,cursor='hand2', bg=self.whitecolor)
        self.where.grid(row=0, column=0,padx=5,sticky=NS)
        self.when=Label(self.marker, image=self.cirle,cursor='hand2', bg=self.whitecolor)
        self.when.grid(row=0, column=1,padx=5, sticky=NS)
        self.how=Label(self.marker, image=self.cirle,cursor='hand2', bg=self.whitecolor)
        self.how.grid(row=0, column=2,padx=5, sticky=NS)
        
        # RIGHT FLOAT PICTURE
        self.right_frm=Frame(self.book_page,bg=self.whitecolor)
        self.right_frm.grid(row=1,column=1,padx=(112,120),sticky=NW)
        self.where_img=Label(self.right_frm, image=self.dest_img, bg=self.whitecolor)
        self.where_img.grid(row=0, column=0,sticky=N)

        
        # WHERE DO YOU WANT TO GO
        self.dest_frm=Frame(self.book_page,bg=self.whitecolor)
        self.dest_frm.grid(row=1,column=0,padx=(100,0))
        Label(self.dest_frm,text='Where do you\nwant to go?',font=self.font1,bg=self.whitecolor,fg=self.bluecolor).grid(row=0,column=0,pady=20,sticky=NW)
        Label(self.dest_frm, image=self.entrybg, bg=self.whitecolor).grid(row=1, column=0,rowspan=2,sticky=NW,columnspan=2)
        Label(self.dest_frm, text='FROM', font=self.font2, bg=self.lightgreycolor,fg=self.bluecolor).grid(row=1, column=0, sticky=W,pady=(7,0),padx=27)
        self.fro=Label(self.dest_frm,text='Select Station',font=self.font2,bg=self.lightgreycolor,fg=self.darkgreencolor)
        self.fro.grid(row=2,column=0,sticky=NW,padx=27)
        self.fro_btn = Menubutton(self.dest_frm,cursor='hand2', image=self.down, relief="flat")
        self.fro_btn.grid(row=2, column=1,sticky=NW)
        self.fro_btn.menu = Menu(self.fro_btn, tearoff=0)
        self.fro_btn['menu'] = self.fro_btn.menu
        for i in range(len(self.source)):
            self.fro_btn.menu.add_radiobutton(label=self.source[i], value=self.source[i], variable=self.sourcevar,
                                               command=lambda: self.from_action(self.sourcevar.get()),
                                               font=self.font2)
        Label(self.dest_frm, image=self.entrybg, bg=self.whitecolor).grid(row=3, column=0,rowspan=2,pady=15,sticky=NW,columnspan=2)
        Label(self.dest_frm, text='TO', font=self.font2, padx=20,bg=self.lightgreycolor,fg=self.bluecolor).grid(row=3, column=0, sticky=W,pady=(8,0),padx=9)
        self.to=Label(self.dest_frm,text='Select Station',font=self.font2,bg=self.lightgreycolor,fg=self.darkgreencolor)
        self.to.grid(row=4,column=0,sticky=NW,padx=27)
        self.to_btn = Menubutton(self.dest_frm,cursor='hand2', image=self.down, relief="flat")
        self.to_btn.grid(row=4, column=1,sticky=NW)
        self.dest_next=Button(self.dest_frm, image=self.next_img, border=0,cursor='hand2', bg=self.whitecolor,command=lambda: self.cmd(1))
        self.dest_next.grid(row=5, column=0,sticky=NW)
        

        # WHEN DO YOU WANT TO GO
        self.date_frm = Frame(self.book_page, bg=self.whitecolor)
        # self.date_frm.grid(row=1, column=0, padx=(100, 0))
        Label(self.date_frm, text='When do you\nwant to go?', font=self.font1, bg=self.whitecolor,
              fg=self.bluecolor).grid(row=0, column=0, pady=20, sticky=NW)

        Label(self.date_frm, image=self.entrybg, bg=self.whitecolor).grid(row=1, column=0, rowspan=2, sticky=NW, columnspan=2)
        Label(self.date_frm, text='DATE', font=self.font2, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=1,column=0,sticky=W,pady=(7, 0),padx=27)
        self.selectdate = DateEntry(self.date_frm, selectmode='day',mindate=self.date,maxdate=self.maxdate, cursor='hand2', font=self.font2,
                             year=dt.date.today().year)
        self.selectdate['state'] = 'readonly'
        self.selectdate.grid(row=2, column=0,padx=(27,0),sticky=NW)
        self.selectdate.bind("<<DateEntrySelected>>",lambda e: self.get_go_time(self.selectdate.get_date()))
        self.to_lbl=Label(self.date_frm, text='TO', font=self.font2, bg=self.lightgreycolor,fg=self.bluecolor)

        # self.to_lbl.grid(row=2, column=0, sticky=NW, padx=(160,0))

        self.returndate = DateEntry(self.date_frm, selectmode='day',mindate=self.date,maxdate=self.maxdate, cursor='hand2', font=self.font2,
                             year=dt.date.today().year)
        self.returndate['state'] = 'readonly'
        # self.returndate.grid(row=2, column=0,padx=(190,0),sticky=NW)
        self.returndate.bind("<<DateEntrySelected>>",lambda e: self.get_return_time(self.returndate.get_date()))

        Label(self.date_frm, image=self.entrybg, bg=self.whitecolor).grid(row=3, column=0, rowspan=2, pady=15,
                                                                          sticky=NW, columnspan=2)
        Label(self.date_frm, text='TIME', font=self.font2, padx=20, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=3, column=0,sticky=W,pady=(10, 0),padx=9)
        self.lbl_time = Label(self.date_frm, text='Select Time', font=self.font2, bg=self.lightgreycolor,
                        fg=self.darkgreencolor)
        # self.lbl_time.grid(row=4, column=0, sticky=NW, padx=27)
        self.go_time_btn = Menubutton(self.date_frm,text='GOING',font=self.font2,fg=self.bluecolor,bg=self.lightgreycolor,
                                      compound=RIGHT,cursor='hand2', image=self.down, relief="flat")
        self.go_time_btn.grid(row=4, column=0, padx=(27, 0), sticky=NW,pady=(0, 2))

        self.return_time_btn = Menubutton(self.date_frm, text='RETURN', font=self.font2, fg=self.bluecolor,
                                          bg=self.lightgreycolor,compound=RIGHT, cursor='hand2', image=self.down, relief="flat")
        # self.return_time_btn.grid(row=4, column=0, padx=(110, 0), sticky=NW)
        self.return_time_btn.menu = Menu(self.return_time_btn, tearoff=0)
        self.return_time_btn['menu'] = self.return_time_btn.menu

        self.date_back=Button(self.date_frm,text='', image=self.backarrow, border=0, cursor='hand2',command=lambda: self.cmd(0),
               bg=self.whitecolor)
        self.date_back.grid(row=5, column=0,pady=3,padx=(0,5),sticky=NW)
        self.date_next=Button(self.date_frm, image=self.next_img, border=0, cursor='hand2',command=lambda: self.cmd(2),
               bg=self.whitecolor)
        self.date_next.grid(row=5, column=0,padx=60,sticky=NW)
        self.way=Button(self.date_frm, image=self.oneway_img, border=0,command=self.way_btn_action, cursor='hand2', bg=self.lightgreycolor)
        # self.way.grid(row=2, column=1,rowspan=3,pady=(15, 0),sticky=NW)


        # HOW DO YOU WANT TO GO
        self.class_frm=Frame(self.book_page, bg=self.whitecolor)
        # self.class_frm.grid(row=1, column=0, padx=(100, 0),sticky=NW)
        Label(self.class_frm, text='How do you\nwant to go?', font=self.font1, bg=self.whitecolor,
              fg=self.bluecolor).grid(row=0, column=0, pady=20,columnspan=2, sticky=NW)

        Label(self.class_frm, image=self.entrybg, bg=self.whitecolor).grid(row=1, column=0, rowspan=2, sticky=NW,
                                                                          columnspan=3)
        Label(self.class_frm, text='NO. OF PASSENGERS', font=self.font2, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=1,column=0,sticky=NW,columnspan=2,pady=(7, 0),padx=(27,0))
        self.passnum = Label(self.class_frm, text='SELECT No OF PASSENGERS', font=self.font2, bg=self.lightgreycolor,
                         fg=self.darkgreencolor)
        self.passnum.grid(row=2, column=0, sticky=NW,columnspan=2, padx=(27,0))
        self.num_menu = Menubutton(self.class_frm,font=self.font5,fg=self.bluecolor,
                                     bg=self.lightgreycolor, cursor='hand2', image=self.down, relief="flat")
        self.num_menu.grid(row=2, column=1,columnspan=2, padx=(0, 0), sticky=NW)

        self.num_menu.menu = Menu(self.num_menu, tearoff=0)
        self.num_menu['menu'] = self.num_menu.menu
        self.num_of_people=[1,2,3,4,5,6]
        for i in range(len(self.num_of_people)):
            self.num_menu.menu.add_radiobutton(label=str(self.num_of_people[i])+' PERSONS', value=self.num_of_people[i], variable=self.numvar,
                                                   font=self.font2,command=lambda: self.num_menu_action(self.numvar.get()))

        Label(self.class_frm, text='CLASS:', font=self.font2, bg=self.whitecolor,
              fg=self.bluecolor).grid(row=4,column=0,sticky=NW, padx=(27,0),pady=(8,0))
        self.class_lbl=Label(self.class_frm, text='SELECT SEAT CLASS', font=self.font2, bg=self.whitecolor,fg=self.greencolor)
        self.class_lbl.grid(row=4,column=0,columnspan=2,sticky=NW, padx=(100,0),pady=(8,0))
        Button(self.class_frm, image=self.regular, border=0, cursor='hand2',bg=self.whitecolor,
               command=lambda: self.class_btns_action('REGULAR COACH')).grid(row=5, column=0,columnspan=3, pady=(3,15),padx=(27,0), sticky=NW)
        Button(self.class_frm, image=self.business, border=0, cursor='hand2',bg=self.whitecolor,
               command=lambda: self.class_btns_action('BUSINESS CLASS')).grid(row=5, column=0, pady=(3,15), padx=(135, 5), sticky=NW)
        Button(self.class_frm, image=self.firstclass, border=0, cursor='hand2',bg=self.whitecolor,
               command=lambda: self.class_btns_action('FIRST CLASS')).grid(row=5, column=0, pady=(3,15), padx=(245, 5), sticky=NW)
        self.class_back=Button(self.class_frm, image=self.backarrow, border=0, cursor='hand2',
               bg=self.whitecolor,command=lambda: self.cmd(1))
        self.class_back.grid(row=6, column=0, pady=3,padx=(0,5),sticky=NW)
        self.class_next=Button(self.class_frm, image=self.next_img, border=0, cursor='hand2',
               bg=self.whitecolor,command=lambda: self.page_switcher(2))
        self.class_next.grid(row=6, column=0,padx=60,sticky=NW)


        # PASSENGER NUMBER RIGHT SIDE PAGE
        self.pass_details=Frame(self.right_frm,bg=self.whitecolor)
        # self.pass_details.grid(row=0, column=0, sticky=NW)
        self.person_lbl=Label(self.pass_details, text=f'PERSON {self.num_of_people[0]}', font=self.font2, bg=self.whitecolor,
              fg=self.bluecolor)
        self.person_lbl.grid(row=0, column=0, sticky=NW)
        Label(self.pass_details, image=self.entrybg2, bg=self.whitecolor).grid(row=1, column=0, rowspan=2, sticky=NW)
        Label(self.pass_details, text='FULL NAME', font=self.font2, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=1, column=0, sticky=NW,pady=(4,0), padx=(25, 0))

        Label(self.pass_details, image=self.entrybg2, bg=self.whitecolor).grid(row=3, column=0, rowspan=2, sticky=NW)
        Label(self.pass_details, text='EMAIL', font=self.font2, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=3, column=0, sticky=NW, pady=(4, 0), padx=(25, 0))

        Label(self.pass_details, image=self.entrybg2, bg=self.whitecolor).grid(row=5, column=0, rowspan=2, sticky=NW)
        Label(self.pass_details, text='PHONE NUMBER', font=self.font2, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=5, column=0, sticky=NW, pady=(4, 0), padx=(25, 0))

        Button(self.pass_details, image=self.backward, border=0, cursor='hand2',bg=self.whitecolor,
               command=self.prev_form).grid(row=7, column=0, padx=50, sticky=NE)
        Button(self.pass_details, image=self.forward, border=0, cursor='hand2', bg=self.whitecolor,
               command=self.next_form).grid(row=7, column=0, padx=2, sticky=NE)

        self.pricepanel=Frame(self.right_frm,bg=self.whitecolor)
        # self.pricepanel.grid(row=1,column=0,sticky=NW)
        Label(self.pricepanel, image=self.roundrect, bg=self.whitecolor).grid(row=0, column=0, rowspan=3,columnspan=2, sticky=NW)
        Label(self.pricepanel, text='PRICE', font=self.font2, bg=self.lightergreycolor,
              fg=self.bluecolor).grid(row=0, column=0, sticky=NW, pady=(4, 0), padx=(25, 0))
        self.singleprice_lbl=Label(self.pricepanel, text=' ', font=self.font2, bg=self.lightergreycolor,
              fg=self.darkgreencolor)
        self.singleprice_lbl.grid(row=1, column=0,columnspan=2, sticky=NW, pady=(4, 0), padx=(25, 0))
        self.sub_total_lbl=Label(self.pricepanel, text=' ', font=self.font2, bg=self.lightergreycolor,
              fg=self.darkgreencolor)
        self.sub_total_lbl.grid(row=2, column=0,columnspan=2, sticky=NW, pady=(4, 0), padx=(25, 0))


        # PAYMENT PORTAL
        self.payment_page = Frame(self.master, bg=self.lightgreycolor)
        # self.payment_page.grid(row=1, column=0, sticky=NW)
        Button(self.payment_page,image=self.back_img,bg=self.lightgreycolor,cursor='hand2',border=0,command=lambda: self.page_switcher(1)).grid(row=0,column=0,pady=(5,0),padx=(40,0),sticky=W)
        Label(self.payment_page, text='PAYMENT PORTAL', font=self.font1, bg=self.lightgreycolor,fg=self.bluecolor).grid(row=0,column=0)
        self.payment_frm = Frame(self.payment_page, bg=self.lightgreycolor)
        self.payment_frm.grid(row=1, column=0,padx=100,pady=10, sticky=NW)
        Label(self.payment_frm, text='Card Number*', font=self.font2, bg=self.lightgreycolor,fg=self.bluecolor).grid(row=1,column=0,sticky=NW)
        Label(self.payment_frm, image=self.entryimg, bg=self.lightgreycolor).grid(row=2, column=0,sticky=NW)
        self.card_num=Entry(self.payment_frm,bg=self.whitecolor,fg=self.darkgreencolor,width=27,font=self.font2,border=0)
        self.card_num.grid(row=2,column=0,sticky=NW,padx=5,pady=5)
        Label(self.payment_frm, image=self.visacard, bg=self.lightgreycolor).grid(row=3, column=0,sticky=NW)
        Label(self.payment_frm, image=self.americacard, bg=self.lightgreycolor).grid(row=3, column=0,sticky=NW,padx=(40,0))
        Label(self.payment_frm, image=self.paypalcard, bg=self.lightgreycolor).grid(row=3, column=0,sticky=NW,padx=(80,0))

        Label(self.payment_frm, text='Expiry Month*', font=self.font2, bg=self.lightgreycolor,fg=self.bluecolor).grid(row=4,pady=(5,0),column=0,sticky=NW)
        Label(self.payment_frm, text='Expiry Year*', font=self.font2, bg=self.lightgreycolor,fg=self.bluecolor).grid(row=4,pady=(5,0),column=0,padx=(120,0),sticky=NW)
        Label(self.payment_frm, image=self.entryimg2, bg=self.lightgreycolor).grid(row=5, column=0,sticky=NW)
        Label(self.payment_frm, image=self.entryimg2, bg=self.lightgreycolor).grid(row=5, column=0,sticky=NW,padx=(120,0))
        self.exp_month=Entry(self.payment_frm,bg=self.whitecolor,fg=self.darkgreencolor,width=7,font=self.font2,border=0)
        self.exp_month.grid(row=5, column=0,sticky=NW,pady=5,padx=5)
        self.exp_year=Entry(self.payment_frm,bg=self.whitecolor,fg=self.darkgreencolor,width=7,font=self.font2,border=0)
        self.exp_year.grid(row=5,column=0,padx=(125,0),sticky=NW,pady=5)
        Label(self.payment_frm, text='Card Holder Name*', font=self.font2, bg=self.lightgreycolor,fg=self.bluecolor).grid(row=6,column=0,pady=(5,0),sticky=NW)
        Label(self.payment_frm, image=self.entryimg3, bg=self.lightgreycolor).grid(row=7, column=0,sticky=NW)
        self.card_holder=Entry(self.payment_frm,bg=self.whitecolor,fg=self.darkgreencolor,width=32,font=self.font2,border=0)
        self.card_holder.grid(row=7,column=0,sticky=NW,padx=5,pady=5)
        Label(self.payment_frm, text='Security code*', font=self.font2, bg=self.lightgreycolor,fg=self.bluecolor).grid(row=8,column=0,pady=(5,0),sticky=NW)
        Label(self.payment_frm, image=self.entryimg2, bg=self.lightgreycolor).grid(row=9, column=0,sticky=NW)
        self.sec_code=Entry(self.payment_frm,show='•',bg=self.whitecolor,fg=self.darkgreencolor,width=7,font=self.font2,border=0)
        self.sec_code.grid(row=9, column=0,sticky=NW,pady=5,padx=5)
        Label(self.payment_frm, image=self.card, bg=self.lightgreycolor).grid(row=9, column=0,sticky=NW,padx=(80,0))
        Label(self.payment_frm, text='3 digits on the back of your card*', font=self.font3, bg=self.lightgreycolor,fg=self.greycolor).grid(row=9,column=0,padx=(120,0),sticky=W)
        self.remember=Checkbutton(self.payment_frm,text='Remember card details for next purchase',bg=self.lightgreycolor,
                                  cursor='hand2',variable=self.remembervar,fg=self.darkgreencolor,font=self.font2)
        self.remember.grid(row=10,column=0,pady=(5,0),sticky=NW)
        self.remember.select()
        self.pay_btn=Button(self.payment_frm,text='Pay',font=self.font2,width=17,fg=self.whitecolor,bg=self.greencolor,
                            cursor='hand2',border=0,command=lambda : self.page_switcher(4))
        self.pay_btn.grid(row=11,column=0,pady=(5,0),padx=(170,0),sticky=W)
        Label(self.payment_page, image=self.premium, bg=self.lightgreycolor).grid(row=1, column=1,sticky=W,pady=(0,60),padx=(80,0))
        self.where.bind("<Button-1>", lambda e: self.cmd(0))
        self.when.bind("<Button-1>", lambda e: self.cmd(1))
        self.how.bind("<Button-1>", lambda e: self.cmd(2))

        # EDIT PROFILE PAGE
        self.edit_page = Frame(self.master, bg=self.lightgreycolor)
        # self.edit_page.grid(row=1, column=0, sticky=NW)
        self.edit_frm = Frame(self.edit_page, bg=self.lightgreycolor)
        self.edit_frm.grid(row=2, column=1, padx=5, sticky=W,pady=(30,0))
        Button(self.edit_page, image=self.back_img, border=0, cursor='hand2', command=lambda: self.page_switcher(1),
               bg=self.lightgreycolor).grid(row=1, column=0, sticky=NW, pady=15,padx=(20,0))
        Label(self.edit_page, text="EDIT PROFILE", font=self.font1, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=1, column=0, sticky=NW, columnspan=2, pady=(0, 10), padx=(60, 0))

        Label(self.edit_frm, text="F I R S T  N A M E", font=self.font2, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=1, column=0, padx=(0, 10), sticky=W)
        Label(self.edit_frm, image=self.entryimg5, bg=self.lightgreycolor).grid(row=2, column=0, padx=(0, 10), sticky=W)
        self.f_name_ent = Entry(self.edit_frm, bg=self.whitecolor, width=21, border=0, font=self.font2,
                            fg=self.darkgreencolor)
        self.f_name_ent.insert(0,self.f_name.title())
        self.f_name_ent.grid(row=2, column=0, padx=(0, 10))
        Label(self.edit_frm, text="M I D D L E  N A M E", font=self.font2, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=1, column=1, padx=(0, 10), sticky=W)
        Label(self.edit_frm, image=self.entryimg5, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=2, column=1, padx=(0, 10), sticky=W)
        self.m_name_ent = Entry(self.edit_frm, bg=self.whitecolor, width=21, border=0, font=self.font2,
                            fg=self.darkgreencolor)
        self.m_name_ent.insert(0, self.m_name.title())
        self.m_name_ent.grid(row=2, column=1, padx=(0, 10))
        Label(self.edit_frm, text="L A S T  N A M E", font=self.font2, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=1, column=2, sticky=W)
        Label(self.edit_frm, image=self.entryimg5, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=2, column=2, sticky=W)
        self.l_name_ent = Entry(self.edit_frm, bg=self.whitecolor, width=21, border=0, font=self.font2,
                            fg=self.darkgreencolor)
        self.l_name_ent.insert(0, self.l_name.title())
        self.l_name_ent.grid(row=2, column=2)
        Label(self.edit_frm, text="E M A I L  A D D R E S S", font=self.font2, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=3, pady=(5, 0), column=0, sticky=W)
        Label(self.edit_frm, image=self.entryimg4, bg=self.lightgreycolor).grid(row=4, column=0, columnspan=2, sticky=W)
        self.email_ent = Entry(self.edit_frm, bg=self.whitecolor, width=30, border=0, font=self.font2,
                           fg=self.darkgreencolor)
        self.email_ent.insert(0, self.email)
        self.email_ent.grid(row=4, column=0, columnspan=2, sticky=W, padx=(5, 0))

        menuitems = ['MALE', 'FEMALE', 'OTHER']
        self.gender = Menubutton(self.edit_frm, text=menuitems[0], compound=RIGHT, image=self.down,
                                 border=0, font=self.font2, fg=self.bluecolor, cursor='hand2', bg=self.whitecolor)
        self.gender.grid(row=4, column=2, sticky=NW, padx=5)

        self.gender.menu = Menu(self.gender, tearoff=0)
        self.gender['menu'] = self.gender.menu
        for i in range(len(menuitems)):
            self.gender.menu.add_radiobutton(label=menuitems[i], value=menuitems[i], variable=self.gendervar,
                                             command=lambda: self.gender_btn_action(self.gendervar.get()),
                                             font=self.font2)

        Label(self.edit_frm, text="P H O N E  N U M B E R", font=self.font2, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=5, pady=(5, 0), column=0, sticky=W)
        Label(self.edit_frm, image=self.entryimg4, bg=self.lightgreycolor).grid(row=6, column=0, columnspan=2, sticky=W)
        self.phone_ent = Entry(self.edit_frm, bg=self.whitecolor, width=30, border=0, font=self.font2,
                           fg=self.darkgreencolor)
        self.phone_ent.insert(0, self.phone_num)
        self.phone_ent.grid(row=6, column=0, columnspan=2, sticky=W, padx=(5, 0))
        Label(self.edit_frm, text="N E W  P A S S W O R D", font=self.font2, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(pady=(5, 0),
                                       row=7, column=0, columnspan=2, sticky=W)
        Label(self.edit_frm, image=self.entryimg4, bg=self.lightgreycolor).grid(row=8, column=0, columnspan=2, sticky=W)
        self.newpass_ent = Entry(self.edit_frm, bg=self.whitecolor, show='•', width=26, border=0, font=self.font2,
                                  fg=self.darkgreencolor)
        self.newpass_ent.grid(row=8, column=0, padx=(5, 0), columnspan=2, sticky=W)
        Label(self.edit_frm, text="O L D  P A S S W O R D", font=self.font2, bg=self.lightgreycolor, fg=self.bluecolor).grid(
            row=9, column=0, sticky=W, pady=(5, 0))
        Label(self.edit_frm, image=self.entryimg4, bg=self.lightgreycolor).grid(row=10, column=0, columnspan=2, sticky=W)
        self.toggle_btn = Button(self.edit_frm, image=self.toggle_btn_img, border=0, cursor='hand2',bg=self.whitecolor,
                                  command=lambda: self.toggle_password(self.newpass_ent, self.toggle_btn))
        self.toggle_btn.grid(row=8, column=1, padx=(60, 0), sticky=W)
        self.password_ent = Entry(self.edit_frm, bg=self.whitecolor, show='•', width=26, border=0, font=self.font2,
                                  fg=self.darkgreencolor)
        self.password_ent.grid(row=10, column=0, padx=(5, 0), columnspan=2, sticky=W)
        self.toggle_btn2 = Button(self.edit_frm, image=self.toggle_btn_img, border=0, cursor='hand2',
                                  bg=self.whitecolor,
                                  command=lambda: self.toggle_password(self.password_ent, self.toggle_btn2))
        self.toggle_btn2.grid(row=10, column=1, padx=(60, 0), sticky=W)
        Button(self.edit_frm, text='S U B M I T', font=self.font2, fg=self.whitecolor, padx=33, border=0,cursor='hand2',bg=self.greencolor,
               command=lambda: self.page_switcher(0)).grid(row=11, column=2, padx=(5, 0), sticky=W)
        Label(self.edit_page, image=self.premium, bg=self.lightgreycolor).grid(row=2, column=0,padx=30, sticky=W)


        self.seat_selection_page = Frame(self.master, bg=self.lightgreycolor)
        # self.seat_selection_page.grid(row=1, column=0, sticky=NW)
        Label(self.seat_selection_page, text="SELECT SEAT", font=self.font1, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=0, column=0, sticky=NW, pady=(10,0),padx=30)
        Label(self.seat_selection_page,image=self.availble,bg=self.lightgreycolor,fg=self.bluecolor).grid(row=1, column=1, sticky=NW, padx=(10,10))
        Label(self.seat_selection_page, text="AVAILABLE", font=self.font2, bg=self.lightgreycolor,
              fg=self.darkgreencolor).grid(row=1, column=1, sticky=NW, padx=(40,0))
        Label(self.seat_selection_page,image=self.selected,bg=self.lightgreycolor,fg=self.bluecolor).grid(row=1, column=2, sticky=NW, padx=10)
        Label(self.seat_selection_page, text="SELECTED", font=self.font2, bg=self.lightgreycolor,
              fg=self.greencolor).grid(row=1, column=2, sticky=NW, padx=(40,0))
        Label(self.seat_selection_page,image=self.unavailable,bg=self.lightgreycolor,state='disabled',fg=self.bluecolor).grid(row=1, column=3, sticky=NW, padx=10)
        Label(self.seat_selection_page, text="UNAVAILABLE", font=self.font2, bg=self.lightgreycolor,
              fg=self.darkredcolor).grid(row=1, column=3, sticky=NW, padx=(40,0))
        self.seat_class_lbl = Label(self.seat_selection_page, text='FIRST CLASS (24 SEATER)',font=self.font2, bg=self.lightgreycolor,fg=self.bluecolor)
        self.seat_class_lbl.grid(row=2, column=1,columnspan=2, sticky=NW, pady=(5,5),padx=(10))
        self.seat_frm=Frame(self.seat_selection_page, bg=self.lightgreycolor)
        self.seat_frm.grid(row=3, column=1,columnspan=3,rowspan=2,padx=10, sticky=NW)
        Button(self.seat_selection_page, text='P R O C E E D', font=self.font2, fg=self.whitecolor, padx=10, border=0,
               cursor='hand2',command=self.registerall, bg=self.greencolor).grid(row=5, column=3,pady=20, sticky=NE)

        self.saved = []
        self.way_count=False
        self.page_count=1
        self.completed=False

    def seat_placement(self,cls,num,z):
        count=1
        if num>=12:
            for x in range(1,13):
                for y in range(num//12):
                    if count in z:
                        b = Button(self.seat_frm, image=self.unavailable, border=0, bg=self.lightgreycolor,
                                   name='%s-%d' % (cls,count),
                                   cursor='hand2',state='disabled' ,command=lambda x=count: self.get_seat_num(cls,x))
                        # b.config(state='disabled')
                        b.grid(row=y, column=x, padx=5, pady=5)
                        count += 1
                    else:
                        b=Button(self.seat_frm,image=self.availble,border=0,bg=self.lightgreycolor,name='%s-%d' % (cls,count),
                                 cursor='hand2',command=lambda x=count:self.get_seat_num(cls,x))
                        b.grid(row=y,column=x,padx=5,pady=5)
                        count+=1
            for i in range(1,num%12+1):
                if count in z:
                    b = Button(self.seat_frm, image=self.unavailable, border=0, bg=self.lightgreycolor,
                               name='%s-%d' % (cls,count),
                               cursor='hand2', state='disabled', command=lambda x=count: self.get_seat_num(cls,x))
                    # b.config(state='disabled')
                    b.grid(row=y+1, column=i, padx=5, pady=5)
                    count += 1
                else:
                    b = Button(self.seat_frm, image=self.availble, border=0, bg=self.lightgreycolor, name='%s-%d' % (cls,count),
                               cursor='hand2', command=lambda x=count: self.get_seat_num(cls,x))
                    b.grid(row=y+1, column=i, padx=5, pady=5)
                    count += 1
        else:
            for i in range(1,num+1):
                if count in z:
                    b = Button(self.seat_frm, image=self.unavailable, border=0, bg=self.lightgreycolor,
                               name='%s-%d' % (cls,count),
                               cursor='hand2', state='disabled', command=lambda x=count: self.get_seat_num(cls,x))
                    # b.config(state='disabled')
                    b.grid(row=1, column=i, padx=5, pady=5)
                    count += 1
                else:
                    b = Button(self.seat_frm, image=self.availble, border=0, bg=self.lightgreycolor, name='%s-%d' % (cls,count),
                               cursor='hand2', command=lambda x=count: self.get_seat_num(cls,x))
                    b.grid(row=1, column=i, padx=5, pady=5)
                    count += 1



    def get_seat_num(self,cls,numb):
        for k,v in self.seat_frm.children.items():
            if k=='%s-%d'% (cls,numb):
                if v._name in self.saved:
                    v.config(image=self.availble)
                    self.saved.remove(v._name)
                    print(self.saved)
                else:
                    if len(self.saved) < self.numvar.get():
                        v.config(image=self.selected)
                        self.saved.append(v._name)
                        print(self.saved)
                    else:
                        messagebox.showerror('ERROR', 'max seats reached')

            # print(v._name)



    def travellerdata(self,n):
        self.entry = [[Entry() for row in range(3)] for col in range(n)]
        i=1
        for col in range(n):
            for row in range(3):
                if col==0:
                    if row==0:
                        self.entry[col][row] = Entry(self.pass_details, font=self.font5, bg=self.lightgreycolor,
                                           fg=self.darkgreencolor,
                                           border=0, width=35)
                        self.entry[col][row].insert(0, f'{self.l_name.upper()} {self.f_name.upper()} {self.m_name.upper()}')
                        self.entry[col][row].grid(row=i * 2, column=0, sticky=NW, padx=(26, 0))

                    elif row==1:
                        self.entry[col][row] = Entry(self.pass_details, font=self.font5, bg=self.lightgreycolor,
                                           fg=self.darkgreencolor,
                                           border=0, width=35)
                        self.entry[col][row].insert(0, self.email.upper())
                        self.entry[col][row].grid(row=i * 2, column=0, sticky=NW, padx=(26, 0))

                    elif row==2:
                        self.entry[col][row] = Entry(self.pass_details, font=self.font5, bg=self.lightgreycolor,
                                           fg=self.darkgreencolor,
                                           border=0, width=35)
                        self.entry[col][row].insert(0, self.phone_num)
                        self.entry[col][row].grid(row=i*2, column=0, sticky=NW, padx=(26, 0))

                    i+=1
                else:
                    if row == 0:
                        self.entry[col][row] = Entry(self.pass_details, font=self.font5, bg=self.lightgreycolor,
                                           fg=self.darkgreencolor,
                                           border=0, width=35)

                    elif row == 1:
                        self.entry[col][row] = Entry(self.pass_details, font=self.font5, bg=self.lightgreycolor,
                                           fg=self.darkgreencolor,
                                           border=0, width=35)
                        self.entry[col][row].insert(0, self.email.upper())

                    elif row == 2:
                        self.entry[col][row] = Entry(self.pass_details, font=self.font5, bg=self.lightgreycolor,
                                           fg=self.darkgreencolor,
                                           border=0, width=35)
                        self.entry[col][row].insert(0, self.phone_num)

    def get_pass_details(self):
        num=self.numvar.get()
        pass_data = [[],[],[]]
        for col in range(num):
            for row in range(3):
                pass_data[row].append(self.entry[col][row].get())
        return pass_data

    def validate_pass_details(self):
        data=self.get_pass_details()
        num = len(data[0])
        for col in range(3):
            for row in range(num):
                if '' in data[row][col]:
                    messagebox.showerror('ERROR','PLEASE FILL ALL PASSENGER INFO')
                    return False
                else:
                    return True

    def get_all_data(self,n):
        source=self.sourcevar.get()
        dest=self.destinationvar.get()
        date=self.selectdate.get_date()
        time=self.go_timevar.get()
        name=self.get_pass_details()
        p_name=name[0][n]
        p_mail=name[1][n]
        cls=self.classval
        num=self.numvar.get()
        seatnum=self.saved[n]
        username=self.username
        return [seatnum,source,dest,date,time,p_name,cls,username,p_mail]

    def registerall(self):
        for i in range(self.numvar.get()):
            data = self.get_all_data(i)
            tknum = fn.generate_ticket_num()
            seatnum = data[0]
            schedule_id = fn.get_schedule_id(data[1], data[2], data[3], data[4])
            fn.register_all(tknum, seatnum, schedule_id, data[5].lower(), data[3], data[4], data[6], data[7])
            try:
                fn.send_mail(tknum,seatnum,schedule_id,data[5],data[3],data[4],data[6],data[8])
            except:
                messagebox.showerror('error','error sending email')
        messagebox.showinfo('yay', 'booking successful')
        self.page_switcher(1)
        self.reset()


    def next_form(self):
        num=len(self.entry)
        if self.page_count<num:
            for col in range(num):
                for row in range(3):
                            self.entry[col][row].grid_forget()
            for i in range(3):
                self.entry[self.page_count][i].grid(row=(i+1) * 2, column=0, sticky=NW, padx=(26, 0))
                self.person_lbl.config(text=f'PERSON {self.page_count+1}')
            self.page_count += 1
        else:
            pass


    def prev_form(self):
        num = len(self.entry)
        if self.page_count > 1:
            self.page_count -= 1
            for col in range(num):
                for row in range(3):
                    self.entry[col][row].grid_forget()
            for i in range(3):
                self.entry[self.page_count-1][i].grid(row=(i + 1) * 2, column=0, sticky=NW, padx=(26, 0))
                self.person_lbl.config(text=f'PERSON {self.page_count}')

        else:
            pass

    def cmd_valid(self,n):
        pages=[self.dest_frm,self.date_frm,self.class_frm]
        images=[self.dest_img,self.date_img,self.premium]
        marker=[self.where,self.when,self.how]
        for i in range(len(pages)):
            pages[i].grid_forget()
            marker[i].config(image=self.cirle)
        # self.where_img.grid(row=0, column=0, sticky=NW)
        # self.pass_details.grid_forget()
        marker[n].config(image=self.cirle2)
        pages[n].grid(row=1, column=0, padx=(100, 0))
        self.where_img.config(image=images[n])
        # self.right_frm.grid_configure(padx=(112,120))
    def cmd(self,n):
        if n==0:
            self.cmd_valid(n)
        elif n==1:
            if not self.sourcevar.get():
                messagebox.showerror('PAUSE', 'KINDLY SELECT A SOURCE AND LOCATION')
                print(False)
            else:
                if self.to.cget('text') == self.fro.cget('text'):
                    messagebox.showerror('ERROR','INVALID DESTINATION/SOURCE')
                else:
                    self.get_go_time(self.selectdate.get_date())
                    self.cmd_valid(n)
        elif n==2:
            if not self.go_timevar.get():
                messagebox.showerror('PAUSE', 'KINDLY SELECT YOUR DESIRED TIME')
            else:
                self.cmd_valid(n)





    def way_btn_action(self):
        if self.way_count==False:
            self.to_lbl.grid(row=2, column=0, sticky=NW, padx=(160, 0))
            self.returndate.grid(row=2, column=0, padx=(190, 0), sticky=NW)
            self.return_time_btn.grid(row=4, column=0, padx=(130, 0), sticky=NW)
            self.way.config(image=self.return_img)
            self.way_count=True
        else:
            self.to_lbl.grid_forget()
            self.returndate.grid_forget()
            self.return_time_btn.grid_forget()
            self.way.config(image=self.oneway_img)
            self.way_count=False


    def show_passform(self,n):
        self.where_img.grid_forget()
        self.pass_details.grid(row=0, column=0, sticky=NW)
        self.pricepanel.grid(row=1,column=0,sticky=NW)
        self.right_frm.grid_configure(padx=(59,87))
        self.travellerdata(n)
        # print(self.get_pass_details())
        
    
    def num_menu_action(self,num):
        self.passnum.config(text=f'{num} PERSONS')
        self.page_count = 1
        self.person_lbl.config(text=f'PERSON {self.page_count}')
        self.show_passform(int(num))
        self.class_btns_action('REGULAR COACH')

    def class_btns_action(self,n):
        source = self.sourcevar.get()
        dest = self.destinationvar.get()
        date = self.selectdate.get_date()
        time = self.go_timevar.get()
        sid = fn.get_schedule_id(source, dest, date, time)
        seat=fn.get_num_of_seats(sid, n.lower())
        prices=fn.get_price(self.sourcevar.get(),self.destinationvar.get(),self.go_timevar.get())
        if n=='REGULAR COACH':
            self.class_lbl.config(text=f'{n} ({seat} seater)')
            self.seat_class_lbl.config(text=f'{n} ({seat} seater)')
            self.regular_price=prices[2]
            self.singleprice_lbl.config(text=f'{n}: N{self.regular_price}.00')
            self.sub_total_lbl.config(
                text=f'SUB TOTAL: {self.regular_price} x {self.numvar.get()} = N{self.regular_price*int(self.numvar.get())}.00')
            self.pay_btn.config(text=f'PAY N{self.regular_price*int(self.numvar.get())}.00')
            self.classval='regular coach'
            self.classval2='rc'
        elif n=='BUSINESS CLASS':
            self.class_lbl.config(text=f'{n} ({seat} seater)')
            self.seat_class_lbl.config(text=f'{n} ({seat} seater)')
            self.business_price=prices[1]
            self.singleprice_lbl.config(text=f'{n}: N{self.business_price}.00')
            self.sub_total_lbl.config(
                text=f'SUB TOTAL: {self.business_price} x {self.numvar.get()} = N{self.business_price * int(self.numvar.get())}.00')
            self.pay_btn.config(text=f'PAY N{self.business_price*int(self.numvar.get())}.00')
            self.classval='business class'
            self.classval2 = 'bc'
        elif n=='FIRST CLASS':
            self.class_lbl.config(text=f'{n} ({seat} seater)')
            self.seat_class_lbl.config(text=f'{n} ({seat} seater)')
            self.firstclass_price=prices[0]
            self.singleprice_lbl.config(text=f'{n}: N{self.firstclass_price}.00')
            self.sub_total_lbl.config(
                text=f'SUB TOTAL: {self.firstclass_price} x {self.numvar.get()} = N{self.firstclass_price * int(self.numvar.get())}.00')
            self.pay_btn.config(text=f'PAY N{self.firstclass_price*int(self.numvar.get())}.00')
            self.classval='first class'
            self.classval2 = 'fc'
        else:
            pass

    def page_switcher2(self,n):
        pages=[self.landing_page,self.book_page,self.payment_page,self.edit_page,self.seat_selection_page]
        colors=[self.bluecolor,self.whitecolor,self.lightgreycolor,self.lightgreycolor,self.lightgreycolor]
        for i in range(len(pages)):
            pages[i].grid_forget()
        pages[n].grid(row=1,column=0,sticky=NW)
        self.master.configure(bg=colors[n])
    def page_switcher(self,n):
        if n==2:
            if self.numvar.get():
                if '' in self.get_pass_details()[0]:
                    messagebox.showerror('WAIT', 'KINDLY FILL ALL PASSENGER DETAILS')
                else:
                    self.page_switcher2(n)
            else:
                messagebox.showerror('WAIT','KINDLY SELECT NUMBER OF PASSENGERS')
        elif n==4:
            if self.check_payment():
                if self.remembervar.get():
                    fn.store_card_details(self.check_payment(),self.username)
                else:
                    fn.forget_card_details(self.username)
                source = self.sourcevar.get()
                dest = self.destinationvar.get()
                date = self.selectdate.get_date()
                time = self.go_timevar.get()
                sid=fn.get_schedule_id(source,dest,date,time)
                messagebox.showinfo('SUCCESS','Payment successful')
                self.seat_placement(self.classval2, fn.get_num_of_seats(sid,self.classval), fn.get_seats(self.classval,sid))
                self.page_switcher2(n)
                self.completed=True
            else:
                messagebox.showerror('CHILL','PLS COMPLETE PAYMENT INFO')
        else:
            if self.completed:
                pass
            else:
                self.page_switcher2(n)

    def check_payment(self):
        if self.card_num.get() and self.exp_month.get() and self.exp_year.get() and self.card_holder.get() and self.sec_code.get():
            return [self.card_num.get(), self.exp_month.get(), self.exp_year.get(), self.card_holder.get(), self.sec_code.get()]

    def fill_card_data(self):
        data=fn.get_card_details(self.username)
        entries=[self.card_num, self.exp_month, self.exp_year, self.card_holder, self.sec_code]
        if data[0]:
            for i in range(len(data)):
                entries[i].insert(0,data[i])


    def mainmenu_action(self,item):
        if item=='PROFILE':
            self.page_switcher(3)
        elif item=='TICKETS':
            self.page_switcher(3)
        elif item== 'LOGOUT':
            if self.completed:
                messagebox.showwarning('HOLD UP','PLEASE COMPLETE BOOKING')
            else:
                self.master.destroy()


    def on_enter(self,event):
        self.continue_btn.config(fg=self.whitecolor)

    def on_leave(self,event):
        self.continue_btn.config(fg=self.greencolor)

    def toggle_password(self,widget,toggle_btn):
        if widget.cget('show') == '':
            widget.config(show='•')
            toggle_btn.config(image=self.toggle_btn_img)
        else:
            widget.config(show='')
            toggle_btn.config(image=self.toggle_btn_img2)

    def gender_btn_action(self,gend):
        self.gender.config(text=gend)
        self.gend=gend.lower()

    def from_action(self, station):
        self.go_time_btn.config(text='GOING')
        self.go_timevar.set('')
        self.fro.config(text=station)
        destination=fn.get_destinations(station)
        if station in destination:
            destination.remove(station)
            self.to_btn.menu = Menu(self.to_btn, tearoff=0)
            self.to_btn['menu'] = self.to_btn.menu
            for i in range(len(destination)):
                self.to_btn.menu.add_radiobutton(label=destination[i], value=destination[i],variable=self.destinationvar,
                                                 command=lambda: self.to_action(self.destinationvar.get()),
                                                 font=self.font2)
            destination.append(station)

        else:
            # destination.remove(station)
            if station==self.destinationvar.get():
                self.to_btn.config(text=destination[0])
                self.destinationvar.set(destination[0])
            self.to_btn.menu = Menu(self.to_btn, tearoff=0)
            self.to_btn['menu'] = self.to_btn.menu
            for i in range(len(destination)):
                self.to_btn.menu.add_radiobutton(label=destination[i], value=destination[i],
                                                 variable=self.destinationvar,
                                                 command=lambda: self.to_action(self.destinationvar.get()),
                                                 font=self.font2)

    def to_action(self,station):
        self.to.config(text=station)

    def get_go_time(self,date):
        source=self.fro.cget('text')
        dest=self.to.cget('text')
        self.returndate.config(mindate=date+relativedelta(years=0,months=0,days=1))
        self.returndate.set_date(date+relativedelta(years=0,months=0,days=1))
        times=fn.get_time(source,dest,str(date))
        self.get_return_time(date+relativedelta(years=0,months=0,days=1))
        self.go_time_btn.menu = Menu(self.go_time_btn, tearoff=0)
        self.go_time_btn['menu'] = self.go_time_btn.menu
        for i in range(len(times)):
            self.go_time_btn.menu.add_radiobutton(label=times[i], value=times[i],variable=self.go_timevar,font=self.font2,
                                                  command=lambda: self.go_time_btn.config(text=self.go_timevar.get()))
    def get_return_time(self,date):
        source=self.fro.cget('text')
        dest=self.to.cget('text')
        times=fn.get_time(dest,source,str(date))
        self.return_time_btn.menu = Menu(self.return_time_btn, tearoff=0)
        self.return_time_btn['menu'] = self.return_time_btn.menu
        for i in range(len(times)):
            self.return_time_btn.menu.add_radiobutton(label=times[i], value=times[i],font=self.font2,variable=self.return_timevar,
                                                  command=lambda: self.return_time_btn.config(text=self.return_timevar.get()),)

    def reset(self):
        self.to.config(text='Select Station')
        self.fro.config(text='Select Station')
        self.sourcevar.set('')
        self.destinationvar.set('')
        self.selectdate.set_date(datetime.datetime.today())
        self.go_time_btn.config(text='GOING')
        self.go_timevar.set('')
        self.passnum.config(text='SELECT No OF PASSENGERS')
        self.numvar.set(0)
        self.person_lbl.config(text='PERSON 1')
        self.page_count = 1
        self.class_lbl.config(text='SELECT SEAT CLASS')
        if not self.remembervar:
            self.card_num.delete(0,END)
            self.exp_month.delete(0,END)
            self.exp_year.delete(0,END)
            self.card_holder.delete(0,END)
            self.sec_code.delete(0,END)
        self.right_frm.grid_configure(padx=(112, 120))
        self.pass_details.grid_forget()
        self.pricepanel.grid_forget()
        self.where_img.grid(row=0, column=0, sticky=NW)
        self.seat_frm.destroy()
        self.seat_frm=Frame(self.seat_selection_page, bg=self.lightgreycolor)
        self.seat_frm.grid(row=3, column=1,columnspan=3,rowspan=2,padx=10, sticky=NW)
        self.saved=[]
        self.completed = False
        self.cmd(0)
        self.page_switcher(1)




root=Tk()
root.resizable(0, 0)
root.configure(bg='#110445')
root.geometry('1000x600+183+60')
root.title('R A I L L Y')
# root.overrideredirect(1)
apk = LandingPage(root)
apk.mainloop()