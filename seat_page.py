from tkinter import *
from PIL import ImageTk


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.create_widgets()
        self.place()

    def logout_button(self):
        root.destroy()
        import customer_login

    def create_widgets(self):
        ### LOGOUT BUTTON ###

        self.img0 = ImageTk.PhotoImage(file="img0.png")
        self.b0 = Button(root, image=self.img0, borderwidth=0, highlightthickness=0, command=self.logout_button, relief="flat")
        self.b0.place(x=1120, y=27, width=80, height=22)

        ### Raily Logo ###

        self.img8 = PhotoImage(file=f"Img_logo.png")
        b1 = Button(root, image=self.img8, borderwidth=0, highlightthickness=0, command=btn_clicked(), relief="flat")
        b1.place(x=100, y=35, width=120, height=40)

        self.img9 = ImageTk.PhotoImage(file=f"train.png")
        img9_canvas = canvas.create_image(1010, 460, image=self.img9)


        ### TICKETS HEADER BUTTON ###

        self.img_ticket_header = PhotoImage(file=f"tickets_header.png")
        b1 = Button(root, image=self.img_ticket_header, borderwidth=0, highlightthickness=0, command=btn_clicked,
                    relief="flat")

        b1.place(x=540, y=27, width=65, height=40)


        ### Train class sub heading###
        canvas.create_text(230, 140, text="Select Seat", fill="#110445", anchor="w",
                           font=("Poppins SemiBold", int(15.0)))







        ### Next button ###


        self.img_next = PhotoImage(file=f"img4.png")
        b1 = Button(root, image=self.img_next, borderwidth=0, highlightthickness=0, command=btn_clicked(),
                    relief="flat")
        b1.place(x=503, y=600, width=169, height=56)

        # Train Seat Indicator
        self.indicator = ImageTk.PhotoImage(file="indicators.png")
        indicator_canvas = canvas.create_image(280, 186, image=self.indicator)

        # Train Seat Grey bg
        self.grey_bg = ImageTk.PhotoImage(file="base train bg.png")
        grey_bg_canvas = canvas.create_image(280, 410, image=self.grey_bg)
                #Seat Lettering
        canvas.create_text(166, 275, text="A               B                C               D", fill="#110445", anchor="w",
                           font=("Poppins Medium", int(13.0)))
                #Seat Numbering
        canvas.create_text(276, 438, text=" 1\n\n"
                                          "2\n\n"
                                          
                                          "3\n\n"
                                          "4\n\n"
                                          "5", fill="#110445", anchor="w",
                           font=("Poppins Medium", int(11.0)))
        # Seat buttons

        self.seat_total = Entry(font=("Poppins SemiBold", int(10.0)), bg='#EAEAEA', fg='#110445', relief='flat', justify='right')
        self.seat_total.place(x=600, y=495, width= 100)


        # Seating Column 3
        def seat_1a():
            print('Selected seat A1')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat A1")

        self.avail_1a = PhotoImage(file=f"available button.png")
        available_buttons1a = Button(root, image=self.avail_1a, borderwidth=0, highlightthickness=0, command=seat_1a,
                    relief="flat")
        available_buttons1a .place(x=160, y=316, width=28, height=28)

        def seat_1b():
            print('Selected seat B1')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat B1")

        self.avail_1b = PhotoImage(file=f"available button.png")
        available_buttons1b = Button(root, image=self.avail_1b, borderwidth=0, highlightthickness=0,
                                     command=seat_1b,
                                     relief="flat")
        available_buttons1b.place(x=230, y=316, width=28, height=28)

        def seat_1c():
            print('Selected seat C1')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat C1")

        self.avail_1c = PhotoImage(file=f"available button.png")
        available_buttons1c = Button(root, image=self.avail_1c, borderwidth=0, highlightthickness=0,
                                     command=seat_1c,
                                     relief="flat")
        available_buttons1c.place(x=305, y=316, width=28, height=28)

        def seat_1d():
            print('Selected seat D1')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat D1")

        self.avail_1d = PhotoImage(file=f"available button.png")
        available_buttons1d = Button(root, image=self.avail_1d, borderwidth=0, highlightthickness=0,
                                     command=seat_1d,
                                     relief="flat")
        available_buttons1d.place(x=375, y=316, width=28, height=28)

        # Seating Column 2

        def seat_2a():
            print('Selected seat A2')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat A2")

        self.avail_2a = PhotoImage(file=f"available button.png")
        available_buttons2a = Button(root, image=self.avail_2a, borderwidth=0, highlightthickness=0,
                                     command=seat_2a,
                                     relief="flat")
        available_buttons2a.place(x=160, y=370, width=28, height=28)



        def seat_2b():
            print('Selected seat B2')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat B2")

        self.avail_2b = PhotoImage(file=f"available button.png")
        available_buttons2b = Button(root, image=self.avail_2b, borderwidth=0, highlightthickness=0,
                                     command=seat_2b,
                                     relief="flat")
        available_buttons2b.place(x=230, y=370, width=28, height=28)

        def seat_2c():
            print('Selected seat C2')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat C2")

        self.avail_2c = PhotoImage(file=f"available button.png")
        available_buttons2c = Button(root, image=self.avail_2c, borderwidth=0, highlightthickness=0,
                                     command=seat_2c,
                                     relief="flat")
        available_buttons2c.place(x=305, y=370, width=28, height=28)

        def seat_2d():
            print('Selected seat D2')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat D2")

        self.avail_2d = PhotoImage(file=f"available button.png")
        available_buttons2d = Button(root, image=self.avail_2d, borderwidth=0, highlightthickness=0,
                                     command=seat_2d,
                                     relief="flat")
        available_buttons2d.place(x=375, y=370, width=28, height=28)

        # Seating Column 3

        def seat_3a():
            print('Selected seat A3')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat A3")

        self.avail_3a = PhotoImage(file=f"available button.png")
        available_buttons3a = Button(root, image=self.avail_3a, borderwidth=0, highlightthickness=0,
                                     command=seat_3a,
                                     relief="flat")
        available_buttons3a.place(x=160, y=420, width=28, height=28)

        def seat_3b():
            print('Selected seat B3')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat B3")

        self.avail_3b = PhotoImage(file=f"available button.png")
        available_buttons3b = Button(root, image=self.avail_3b, borderwidth=0, highlightthickness=0,
                                     command=seat_3b,
                                     relief="flat")
        available_buttons3b.place(x=230, y=420, width=28, height=28)

        def seat_3c():
            print('Selected seat C3')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Not Available")

        self.avail_3c = PhotoImage(file=f"indicator_unavailable.png")
        available_buttons3c = Button(root, image=self.avail_3c, borderwidth=0, highlightthickness=0,
                                     command=seat_3c,
                                     relief="flat")
        available_buttons3c.place(x=305, y=420, width=28, height=28)

        def seat_3d():
            print('Selected seat D3')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat D3")

        self.avail_3d = PhotoImage(file=f"available button.png")
        available_buttons3d = Button(root, image=self.avail_3d, borderwidth=0, highlightthickness=0,
                                     command=seat_3d,
                                     relief="flat")
        available_buttons3d.place(x=375, y=420, width=28, height=28)

        #Seating Column 4

        def seat_4a():
            print('Selected seat A4')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat A4")

        self.avail_4a = PhotoImage(file=f"available button.png")
        available_buttons4a = Button(root, image=self.avail_4a, borderwidth=0, highlightthickness=0,
                                     command=seat_4a,
                                     relief="flat")
        available_buttons4a.place(x=160, y=470, width=28, height=28)

        def seat_4b():
            print('Selected seat B4')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat B4")

        self.avail_4b = PhotoImage(file=f"available button.png")
        available_buttons4b = Button(root, image=self.avail_4b, borderwidth=0, highlightthickness=0,
                                     command=seat_4b,
                                     relief="flat")
        available_buttons4b.place(x=230, y=470, width=28, height=28)

        def seat_4c():
            print('Selected seat C4')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat C4")

        self.avail_4c = PhotoImage(file=f"available button.png")
        available_buttons4c = Button(root, image=self.avail_4c, borderwidth=0, highlightthickness=0,
                                     command=seat_4c,
                                     relief="flat")
        available_buttons4c.place(x=305, y=470, width=28, height=28)

        def seat_4d():
            print('Selected seat D4')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat D4")

        self.avail_4d = PhotoImage(file=f"available button.png")
        available_buttons4d = Button(root, image=self.avail_4d, borderwidth=0, highlightthickness=0,
                                     command=seat_4d,
                                     relief="flat")
        available_buttons4d.place(x=375, y=470, width=28, height=28)

        # Seating Column 5


        def seat_5a():
            print('Selected seat A5')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat A5")

        self.avail_5a = PhotoImage(file=f"available button.png")
        available_buttons5a = Button(root, image=self.avail_5a, borderwidth=0, highlightthickness=0,
                                     command=seat_5a,
                                     relief="flat")
        available_buttons5a.place(x=160, y=524, width=28, height=28)

        def seat_5b():
            print('Selected seat B5')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat B5")

        self.avail_5b = PhotoImage(file=f"available button.png")
        available_buttons5b = Button(root, image=self.avail_5b, borderwidth=0, highlightthickness=0,
                                     command=seat_5b,
                                     relief="flat")
        available_buttons5b.place(x=230, y=524, width=28, height=28)

        def seat_5c():
            print('Selected seat C5')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Seat C5")

        self.avail_5c = PhotoImage(file=f"available button.png")
        available_buttons5c = Button(root, image=self.avail_5c, borderwidth=0, highlightthickness=0,
                                     command=seat_5c,
                                     relief="flat")
        available_buttons5c.place(x=305, y=524, width=28, height=28)

        def seat_5d():
            print('Selected Seat Not Available')
            self.seat_total.delete(0, "end")
            self.seat_total.insert(0, "Not Available")

        self.avail_5d = PhotoImage(file=f"indicator_unavailable.png")
        available_buttons5d = Button(root, image=self.avail_5d, borderwidth=0, highlightthickness=0,
                                     command=seat_5d,
                                     relief="flat")
        available_buttons5d.place(x=375, y=524, width=28, height=28)













        #For Total
        self.Total_bg = ImageTk.PhotoImage(file="total box.png")
        Total_bg_canvas = canvas.create_image(586, 518, image=self.Total_bg)

        canvas.create_text(477, 510, text="Your Seat", fill="#7A7A7A", anchor="w",
                           font=("Poppins Medium", int(10.0)))

        #this for the Price and Seat Output
        #self.lbl_seat = (root,total )

        canvas.create_text(477, 550, text="Total Price", fill="#7A7A7A", anchor="w",
                           font=("Poppins Medium", int(10.0)))



def destination():
    entry0 = [""]


# entry1= [""]
# entry0= "home port"
# entry1= "Lagos Subway"

def btn_clicked():
    print("Button Clicked")


root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, height=720, width=1280, bd=0, highlightthickness=0, relief="ridge", bg="#110445")
background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(370, 360.0, image=background_img)
canvas.place(x=0, y=0)
root.resizable(False, False)
root.title("Seat Page")
app = Application(root)
app.mainloop()
