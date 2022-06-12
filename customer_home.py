from tkinter import *
#from entry import Entry
from PIL import ImageTk

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.create_widgets()
        self.place()






    def create_widgets(self):

        # For Drop Down menu
        from_destinations = ["Lagos Subway", "Abuja Station", "Military Base City"]
        To_destinations = ["Main City", "Delta Alpha Station", "Maryland Station"]

        self.arrow = PhotoImage(file='drop down button.png')
        frm = Menubutton(root, image=self.arrow, relief="flat")
        frm.place(x=360, y=330)
        # 'From' Grey text bg image
        self.entry0_img = PhotoImage(file=f"img_textBox0.png")
        entry0_bg = canvas.create_image(310, 340, image=self.entry0_img)
        self.entry0 = Entry(bd=0, bg="#F1F1F1", highlightthickness=0, font="Poppins 10")
        self.entry0.place(x=140, y=330, width=200.0, height=30)

        # Drop down Menu
        frm.menu = Menu(frm, tearoff=0)
        frm["menu"] = frm.menu
        self.f = StringVar()
        for i in range(len(from_destinations)):
            frm.menu.add_radiobutton(label=from_destinations[i], variable=self.f, command= self.des_from, font="Poppins 10")

        # 'To' Grey BG Text image
        ## 'TO' TEXT ENTRY SECTION ##
        self.arrow2 = PhotoImage(file='drop down button.png')
        to = Menubutton(root, image=self.arrow2, relief="flat")
        to.place(x=360, y=410)

        self.entry1_img = PhotoImage(file=f"img_textBox1.png")
        entry1_bg = canvas.create_image(310, 420, image=self.entry1_img)
        self.entry1 = Entry(bd=0, bg="#F1F1F1", highlightthickness=0, font="Poppins 10")
        self.entry1.place(x=140, y=410, width=200.0, height=30)

        to.menu = Menu(to, tearoff=0)
        to["menu"] = to.menu
        self.t = StringVar()
        for i in range(len(To_destinations)):
            to.menu.add_radiobutton(label=To_destinations[i], variable=self.t, command=self.des_to, font="Poppins 10")



        def logout_button():
            root.destroy()
            import customer_login

        ### LOGOUT BUTTON ###

        self.img0 = ImageTk.PhotoImage(file="img0.png")
        img0_lbl = Label(root, image=self.img0)
        # img0_lbl.pack()
        self.b0 =Button(root, image=self.img0, borderwidth=0, highlightthickness=0, command=logout_button, relief="flat")

        self.b0.place(x=1120, y=27, width=80, height=22)

        self.img8 = PhotoImage(file=f"Img_logo.png")
        b1 = Button(root, image=self.img8, borderwidth=0, highlightthickness=0, command=btn_clicked(), relief="flat")
        b1.place(x=100, y=35, width=120, height=40)

        self.img9 = PhotoImage(file=f"train.png")

        ### Location switch button ###

        self.img_switch = PhotoImage(file=f"img1.png")
        b1 = Button(root, image=self.img_switch, borderwidth=0, highlightthickness=0, command=btn_clicked(), relief="flat")
        b1.place(x=420, y=345, width=51.5, height=52)

        ### Next button ###
        # def seat_page():
        #     root.destroy()
        #     import seat_page
        def action():
            a = self.f.get()
            b = self.t.get()
            if a in from_destinations and b in To_destinations:
                print("good")

            elif set_regular() == self.seat_indicator and set_business() == self.seat_indicator and set_first() == self.seat_indicator:
                root.destroy()
                import seat_page
            else:
                self.seat_indicator.delete(0,"end")


        self.img_next = PhotoImage(file=f"img4.png")
        b1 = Button(root, image=self.img_next, borderwidth=0, highlightthickness=0, command=action, relief="flat")
        b1.place(x=220, y=580, width=169, height=56)

        ### TICKETS HEADER BUTTON ###
        self.img_ticket_header = PhotoImage(file=f"tickets_header.png")
        b1 = Button(root, image=self.img_ticket_header, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")

        b1.place(x=540, y=27, width=65, height=40)

        ### Header Text'where do you want to go?'###
        canvas.create_text(100, 194,text="Where do you \n want to go?",
                           fill="#110445", anchor="w",
                           font=("Poppins Bold", int(27.0)))

        ### Train class sub heading###
        canvas.create_text(110, 480, text="Select a train class: ", fill="#110445", anchor="w", font=("Poppins Medium", int(12.0)))

        ### Regular Class Button ###
        def set_regular():
            self.seat_indicator.delete(0, "end")
            self.seat_indicator.insert(0, "Regular Class")

        self.img_regular = PhotoImage(file=f"regular.png")
        regular = Button(root, image=self.img_regular, text="", borderwidth=0, highlightthickness=0, command=set_regular, relief="flat")
        regular.place(x=140, y=500, width=103, height=46)
        self.seat_indicator = Entry(font=("Poppins SemiBold", int(9.0)), fg='#00F18C', relief='flat')
        self.seat_indicator.place(x=280, y=468)


        ### Business Class Button ###
        def set_business():
            self.seat_indicator.delete(0, "end")
            self.seat_indicator.insert(0, "Business Class")

        self.img_business = PhotoImage(file=f"business.png")
        b1 = Button(root, image=self.img_business, borderwidth=0, highlightthickness=0, command=set_business, relief="flat")
        b1.place(x=250, y=500, width=103, height=46)
        self.seat_indicator = Entry(font=("Poppins SemiBold", int(9.0)), fg='#00F18C', relief='flat')
        self.seat_indicator.place(x=280, y=468)

        ### First Class Button ###
        def set_first():
            self.seat_indicator.delete(0, "end")
            self.seat_indicator.insert(0, "First Class")

        self.img_first = PhotoImage(file=f"firstclass.png")
        b1 = Button(root, image=self.img_first, borderwidth=0, highlightthickness=0, command=set_first, relief="flat")
        b1.place(x=360, y=500, width=103, height=46)
        self.seat_indicator = Entry(font=("Poppins SemiBold", int(9.0)), fg='#00F18C', relief='flat')
        self.seat_indicator.place(x=280, y=468)

        self.img9 = ImageTk.PhotoImage(file=f"train.png")
        img9_canvas = canvas.create_image(1010, 460, image=self.img9)


    def des_from(self):
        destination_from = self.f.get()

        self.entry0.delete(0, END)
        self.entry0.insert(0, destination_from)

    def des_to(self):
        destination_to = self.t.get()

        self.entry1.delete(0, END)
        self.entry1.insert(0, destination_to)




def destination():
     entry0= [""]
    #entry1= [""]
    #entry0= "home port"
    #entry1= "Lagos Subway"

def btn_clicked():
    print("Button Clicked")




root = Tk()
root.geometry("1280x720")
canvas = Canvas( root, height=720, width=1280, bd=0, highlightthickness=0, relief="ridge", bg="#110445")
background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(370, 360.0, image=background_img)
canvas.place(x=0, y=0)
root.resizable(False, False)
app = Application(root)
app.mainloop()
