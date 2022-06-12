from tkinter import *
from tkinter import font as f
from tkcalendar import *
import datetime as dt
from dateutil.relativedelta import relativedelta
from PIL import ImageTk, Image
import random
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image


class LandingPage(Frame):
    def __init__(self, master):
        super(LandingPage, self).__init__(master)
        self.master=master
        self.grid()

        self.font1=f.Font(family='Yu Gothic UI Semilight', size=30, weight='normal')
        self.font2 = f.Font(family='Yu Gothic UI Semilight', size=13, weight='normal')
        self.font3 = f.Font(family='Yu Gothic UI Light', size=18)
        self.font4 = f.Font(family='Yu Gothic UI Light', size=13)
        self.font5 = f.Font(family='Yu Gothic UI Light', size=11, weight='normal')

        self.blackcolor = '#080808'
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
        self.menuvar=StringVar()
        self.numvar=StringVar()
        self.childvar=StringVar()
        self.date = dt.datetime.now()
        self.maxdate=self.date+relativedelta(years=0,months=6,days=0)
        self.slide=0
        self.create_widgets()

    def create_widgets(self):
        self.logo = ImageTk.PhotoImage(Image.open("railly logo green.png"))
        self.logout = ImageTk.PhotoImage(Image.open("profile-user.png"))
        self.entrybg=ImageTk.PhotoImage(Image.open("img_textBox0.png"))
        self.entrybg2=ImageTk.PhotoImage(Image.open("img_textBox0.png").resize((343,69),))
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



        # NAVIGATION BAR SEGMENT
        self.navbar=Frame(self.master,bg=self.bluecolor,width=1000,height=200)
        self.navbar.grid(row=0,column=0,sticky=NW)

        # LOGO
        self.logo_btn = Button(self.navbar, image=self.logo,border=0,cursor='hand2',command=lambda: self.cmd(0),bg=self.bluecolor)
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
            self.mainmenu.menu.add_radiobutton(label=menuitems[i],value=menuitems[i], variable=self.menuvar,font=self.font2)

        # LANDING PAGE
        self.landing_page=Frame(self.master,)
        # BOOK FLIGHT PAGE
        self.bookpage=Frame(self.master,bg=self.whitecolor)
        # self.bookpage.grid(row=1,column=0,sticky=NW)
        
        # PAGE COUNTER AT THE TOP
        self.marker = Frame(self.bookpage,bg=self.whitecolor,width=80)
        self.marker.grid(row=0,column=0,sticky=N,columnspan=2,pady=10,padx=(50,0))
        self.where=Label(self.marker, image=self.cirle2, bg=self.whitecolor)
        self.where.grid(row=0, column=0,padx=5,sticky=NS)
        self.when=Label(self.marker, image=self.cirle, bg=self.whitecolor)
        self.when.grid(row=0, column=1,padx=5, sticky=NS)
        self.how=Label(self.marker, image=self.cirle, bg=self.whitecolor)
        self.how.grid(row=0, column=2,padx=5, sticky=NS)
        
        # RIGHT FLOAT PICTURE
        self.right_frm=Frame(self.bookpage,bg=self.whitecolor)
        self.right_frm.grid(row=1,column=1,padx=(112,120),sticky=NW)
        self.where_img=Label(self.right_frm, image=self.dest_img, bg=self.whitecolor)
        self.where_img.grid(row=0, column=0,sticky=N)

        
        # WHERE DO YOU WANT TO GO
        self.dest_frm=Frame(self.bookpage,bg=self.whitecolor)
        self.dest_frm.grid(row=1,column=0,padx=(100,0))
        Label(self.dest_frm,text='Where do you\nwant to go?',font=self.font1,bg=self.whitecolor,fg=self.bluecolor).grid(row=0,column=0,pady=20,sticky=NW)
        Label(self.dest_frm, image=self.entrybg, bg=self.whitecolor).grid(row=1, column=0,rowspan=2,sticky=NW,columnspan=2)
        Label(self.dest_frm, text='FROM', font=self.font2, bg=self.lightgreycolor,fg=self.bluecolor).grid(row=1, column=0, sticky=W,pady=(7,0),padx=27)
        self.fro=Label(self.dest_frm,text='Select Station',font=self.font2,bg=self.lightgreycolor,fg=self.darkgreencolor)
        self.fro.grid(row=2,column=0,sticky=NW,padx=27)
        self.fro_btn = Menubutton(self.dest_frm,cursor='hand2', image=self.down, relief="flat")
        self.fro_btn.grid(row=2, column=0,padx=(270,0),sticky=NW)
        Label(self.dest_frm, image=self.entrybg, bg=self.whitecolor).grid(row=3, column=0,rowspan=2,pady=15,sticky=NW,columnspan=2)
        Label(self.dest_frm, text='TO', font=self.font2, padx=20,bg=self.lightgreycolor,fg=self.bluecolor).grid(row=3, column=0, sticky=W,pady=(8,0),padx=9)
        self.to=Label(self.dest_frm,text='Select Station',font=self.font2,bg=self.lightgreycolor,fg=self.darkgreencolor)
        self.to.grid(row=4,column=0,sticky=NW,padx=27)
        self.to_btn = Menubutton(self.dest_frm,cursor='hand2', image=self.down, relief="flat")
        self.to_btn.grid(row=4, column=0,padx=(270,0),sticky=NW)
        Button(self.dest_frm, image=self.switch, border=0,cursor='hand2', bg=self.lightgreycolor).grid(row=2, column=1,rowspan=3,pady=(15,0),sticky=NW)
        self.dest_next=Button(self.dest_frm, image=self.next_img, border=0,cursor='hand2', bg=self.whitecolor,command=lambda: self.cmd(1))
        self.dest_next.grid(row=5, column=0,sticky=NW)
        

        # WHEN DO YOU WANT TO GO
        self.date_frm = Frame(self.bookpage, bg=self.whitecolor)
        # self.date_frm.grid(row=1, column=0, padx=(100, 0))
        Label(self.date_frm, text='When do you\nwant to go?', font=self.font1, bg=self.whitecolor,
              fg=self.bluecolor).grid(row=0, column=0, pady=20, sticky=NW)

        Label(self.date_frm, image=self.entrybg, bg=self.whitecolor).grid(row=1, column=0, rowspan=2, sticky=NW, columnspan=2)
        Label(self.date_frm, text='DATE', font=self.font2, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=1,column=0,sticky=W,pady=(7, 0),padx=27)
        self.lbl_date = Label(self.date_frm, text=f"{self.date:%A, %B %d, %Y}", bg=self.lightgreycolor, fg=self.darkgreencolor,
                              font=self.font2)
        # self.lbl_date.grid(row=2, column=0, sticky=NW, padx=27)
        self.selectdate = DateEntry(self.date_frm, selectmode='day',mindate=self.date,maxdate=self.maxdate, cursor='hand2', font=self.font2,
                             year=dt.date.today().year)
        self.selectdate['state'] = 'readonly'
        self.selectdate.grid(row=2, column=0,padx=(27,0),sticky=NW)

        self.to_lbl=Label(self.date_frm, text='TO', font=self.font2, bg=self.lightgreycolor,fg=self.bluecolor)
        # self.to_lbl.grid(row=2, column=0, sticky=NW, padx=(160,0))

        self.returndate = DateEntry(self.date_frm, selectmode='day',mindate=self.date,maxdate=self.maxdate, cursor='hand2', font=self.font2,
                             year=dt.date.today().year)
        self.returndate['state'] = 'readonly'
        # self.returndate.grid(row=2, column=0,padx=(190,0),sticky=NW)

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

        self.date_back=Button(self.date_frm,text='', image=self.backarrow, border=0, cursor='hand2',command=lambda: self.cmd(0),
               bg=self.whitecolor)
        self.date_back.grid(row=5, column=0,pady=3,padx=(0,5),sticky=NW)
        self.date_next=Button(self.date_frm, image=self.next_img, border=0, cursor='hand2',command=lambda: self.cmd(2),
               bg=self.whitecolor)
        self.date_next.grid(row=5, column=0,padx=60,sticky=NW)
        self.way=Button(self.date_frm, image=self.oneway_img, border=0,command=self.way_btn_action, cursor='hand2', bg=self.lightgreycolor)
        self.way.grid(row=2, column=1,rowspan=3,pady=(15, 0),sticky=NW)


        # HOW DO YOU WANT TO GO
        self.class_frm=Frame(self.bookpage, bg=self.whitecolor)
        # self.class_frm.grid(row=1, column=0, padx=(100, 0),sticky=NW)
        Label(self.class_frm, text='How do you\nwant to go?', font=self.font1, bg=self.whitecolor,
              fg=self.bluecolor).grid(row=0, column=0, pady=20,columnspan=2, sticky=NW)

        Label(self.class_frm, image=self.entrybg, bg=self.whitecolor).grid(row=1, column=0, rowspan=2, sticky=NW,
                                                                          columnspan=3)
        Label(self.class_frm, text='NO. OF PASSENGERS', font=self.font2, bg=self.lightgreycolor,
              fg=self.bluecolor).grid(row=1,column=0,sticky=NW,columnspan=2,pady=(7, 0),padx=(27,0))
        self.passnum = Label(self.class_frm, text='1 PERSON', font=self.font2, bg=self.lightgreycolor,
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
        self.class_lbl=Label(self.class_frm, text='FIRST CLASS (24 seater)', font=self.font2, bg=self.whitecolor,fg=self.greencolor)
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
               bg=self.whitecolor)#,command=self.show_passform
        self.class_next.grid(row=6, column=0,padx=60,sticky=NW)


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



        self.way_count=False
        self.page_count=1

    def travellerdata(self,n):
        self.entry = [[Entry() for row in range(6)] for col in range(n)]
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

                    elif row == 2:
                        self.entry[col][row] = Entry(self.pass_details, font=self.font5, bg=self.lightgreycolor,
                                           fg=self.darkgreencolor,
                                           border=0, width=35)


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

    def cmd(self,n):
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


    def way_btn_action(self):
        if self.way_count==False:
            self.to_lbl.grid(row=2, column=0, sticky=NW, padx=(160, 0))
            self.returndate.grid(row=2, column=0, padx=(190, 0), sticky=NW)
            self.return_time_btn.grid(row=4, column=0, padx=(120, 0), sticky=NW)
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
        
    
    def num_menu_action(self,num):
        self.passnum.config(text=f'{num} PERSONS')
        self.page_count = 1
        self.person_lbl.config(text=f'PERSON {self.page_count}')
        self.show_passform(int(num))
        self.class_btns_action('REGULAR COACH')

    def class_btns_action(self,n):
        if n=='REGULAR COACH':
            self.class_lbl.config(text=f'{n} (88 seater)')
            self.singleprice_lbl.config(text=f'{n}: N{self.regular_price}.00')
            self.sub_total_lbl.config(
                text=f'SUB TOTAL: {self.regular_price} x {self.numvar.get()} = N{self.regular_price*int(self.numvar.get())}.00')
        elif n=='BUSINESS CLASS':
            self.class_lbl.config(text=f'{n} (40 seater)')
            self.singleprice_lbl.config(text=f'{n}: N{self.business_price}.00')
            self.sub_total_lbl.config(
                text=f'SUB TOTAL: {self.business_price} x {self.numvar.get()} = N{self.business_price * int(self.numvar.get())}.00')
        elif n=='FIRST CLASS':
            self.class_lbl.config(text=f'{n} (24 seater)')
            self.singleprice_lbl.config(text=f'{n}: N{self.firstclass_price}.00')
            self.sub_total_lbl.config(
                text=f'SUB TOTAL: {self.firstclass_price} x {self.numvar.get()} = N{self.firstclass_price * int(self.numvar.get())}.00')









root=Tk()
root.resizable(0, 0)
root.configure(bg='#FFFFFF')
root.geometry('1000x600+183+60')
root.title('R A I L L Y')
# root.overrideredirect(1)
apk = LandingPage(root)
apk.mainloop()