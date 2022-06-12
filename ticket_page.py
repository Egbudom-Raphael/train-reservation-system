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

        self.img0 = ImageTk.PhotoImage(file="white_logout.png")
        self.b0 = Button(root, image=self.img0, borderwidth=0, highlightthickness=0, command=self.logout_button,
                         relief="flat")
        self.b0.place(x=1120, y=27, width=80, height=22)

        ### Raily Logo ###

        self.img8 = PhotoImage(file=f"Img_logo.png")
        b1 = Button(root, image=self.img8, borderwidth=0, highlightthickness=0, command=btn_clicked(), relief="flat")
        b1.place(x=100, y=35, width=120, height=40)


        ### TICKETS HEADER BUTTON ###

        self.img_ticket_header = PhotoImage(file=f"home_header.png")
        b1 = Button(root, image=self.img_ticket_header, borderwidth=0, highlightthickness=0, command=btn_clicked,
                    relief="flat")

        b1.place(x=460, y=35, width=65, height=40)

        ### Train class sub heading###
        canvas.create_text(608, 130, text="Ticket", fill="#110445", anchor="w",
                           font=("Poppins Bold", int(18.0)))
        #
        # canvas.create_text(610, 150, text="ID ", fill="#110445", anchor="w",
        #                    font=("Poppins Medium", int(13.0)))




        # For Total
        self.Total_bg = ImageTk.PhotoImage(file="total box.png")
        Total_bg_canvas = canvas.create_image(586, 518, image=self.Total_bg)


        # this for the Price and Seat Output
        # self.lbl_seat = (root,total )


        # For Ticketing
        self.Total_bg = ImageTk.PhotoImage(file="ticket_paper.png")
        Total_bg_canvas = canvas.create_image(640, 280, image=self.Total_bg)

        # Seat Full Name Text
        canvas.create_text(515, 235, text="Full Name  ", fill="#110445", anchor="w",
                            font=("Poppins Medium", int(10.0)))

        self.fullname_lbl = Label(root, text="Otali Samuel", bg="#ffffff",
                                        font=("Poppins Medium", int(10.0)), fg="#110445")
        self.fullname_lbl.place(x=680, y=220)

        # Seat Placement Text
        canvas.create_text(515, 263, text="Seat Placement  ", fill="#110445", anchor="w",
                           font=("Poppins Medium", int(10.0)))

        self.seatPlacement_lbl = Label(root, text="Business/A1", bg="#ffffff",
                                  font=("Poppins Medium", int(10.0)), fg="#110445")
        self.seatPlacement_lbl.place(x=680, y=248)

        # Seat Booking Code Text
        canvas.create_text(555, 300, text="Booking Code  ", fill="#110445", anchor="w",
                           font=("Poppins Medium", int(10.0)))

        self.BookingCode_lbl = Label(root, text="B000001", bg="#ffffff",
                                  font=("Poppins Medium", int(10.0)), fg="#110445")
        self.BookingCode_lbl.place(x=660, y=286)


        ### Train class sub heading###
        canvas.create_text(568, 435, text="Train Journey", fill="#110445", anchor="w",
                           font=("Poppins SemiBold", int(16.0)))

        # For Train Journey
        self.TrainJourney_bg = ImageTk.PhotoImage(file="greybg_train_journey.png")
        canvas.create_image(640, 560, image=self.TrainJourney_bg)

        self.destinationLine_bg = ImageTk.PhotoImage(file="destination line.png")
        canvas.create_image(575, 545, image=self.destinationLine_bg)

        # Departure Time & Date

        self.departure_time_lbl = Label(root, text="13:00", bg="#ECECEC",
                                      font=("Poppins Medium", int(13.0)), fg="#110445")
        self.departure_time_lbl.place(x=493, y=479)

        self.departure_date_lbl = Label(root, text="Wed 21", bg="#ECECEC",
                                       font=("Poppins Medium", int(10.0)), fg="#A9A9A9")
        self.departure_date_lbl.place(x=493, y=505)


        self.departure_location_lbl = Label(root, text="Military City", bg="#ECECEC",
                                        font=("Poppins Medium", int(13.0)), fg="#110445")
        self.departure_location_lbl.place(x=684, y=479)

        self.departure_station_lbl = Label(root, text="Military Station", bg="#ECECEC",
                                            font=("Poppins Medium", int(10.0)), fg="#A9A9A9")
        self.departure_station_lbl.place(x=684, y=505)




        # Arrival Time & Date

        self.arrival_time_lbl = Label(root, text="18:00", bg="#ECECEC",
                                       font=("Poppins Medium", int(13.0)), fg="#110445")
        self.arrival_time_lbl.place(x=493, y=580)

        self.arrival_date_lbl = Label(root, text="Wed 21", bg="#ECECEC",
                                       font=("Poppins Medium", int(10.0)), fg="#A9A9A9")
        self.arrival_date_lbl.place(x=493, y=605)

        self.arrival_location_lbl = Label(root, text="Abuja", bg="#ECECEC",
                                            font=("Poppins Medium", int(13.0)), fg="#110445")
        self.arrival_location_lbl.place(x=684, y=580)

        self.arrival_station_lbl = Label(root, text="Abuja Station", bg="#ECECEC",
                                           font=("Poppins Medium", int(10.0)), fg="#A9A9A9")
        self.arrival_station_lbl.place(x=684, y=605)




        # Total Price
        canvas.create_text(950, 570, text="Total Price", fill="#7A7A7A", anchor="w",
                           font=("Poppins Medium", int(10.0)))

        ### Done button ###

        self.img_next = PhotoImage(file=f"done_button.png")
        b1 = Button(root, image=self.img_next, borderwidth=0, highlightthickness=0, command=btn_clicked,
                    relief="flat")
        b1.place(x=970, y=600, width=169, height=56)


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
background_img = PhotoImage(file=f"ticket_whitebg.png")
background = canvas.create_image(640, 360.0, image=background_img)
canvas.place(x=0, y=0)
root.resizable(False, False)
root.title("Seat Page")
app = Application(root)
app.mainloop()
