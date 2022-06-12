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

        self.img8 = PhotoImage(file=f"railly logo green.png")
        b1 = Button(root, image=self.img8, borderwidth=0, highlightthickness=0, command=btn_clicked(), relief="flat")
        b1.place(x=93, y=35, width=105, height=40)

        self.dashboardButton = PhotoImage(file=f"side_dashboard button.png")
        dashboardButton = Button(root, image=self.dashboardButton, borderwidth=0, highlightthickness=0, command=btn_clicked,
                               relief="flat")
        dashboardButton.place(x=80, y=200, width=130, height=30)



        ### Train class sub heading###
        canvas.create_text(330, 84, text="Hi,", fill="#110445", anchor="w",
                           font=("Poppins Bold", int(24.0)))
        canvas.create_text(375, 84, text=" Admin", fill="#00F18C", anchor="w",
                           font=("Poppins Bold", int(24.0)))





        # this for the Price and Seat Output
        # self.lbl_seat = (root,total )


        # For top part
        self.dashboardDetails_bg = ImageTk.PhotoImage(file="dashboard details.png")
        canvas.create_image(695, 190, image=self.dashboardDetails_bg)

        self.Total_user_lbl = Label(root, text="03", bg="#110445",
                                       font=("Poppins bold", int(32.0)), fg="#00F18C")
        self.Total_user_lbl .place(x=470, y=160)

        self.Total_train_lbl = Label(root, text="04", bg="#110445",
                                    font=("Poppins bold", int(32.0)), fg="#00F18C")
        self.Total_train_lbl.place(x=700, y=160)

        self.Total_available_lbl = Label(root, text="03", bg="#110445",
                                     font=("Poppins bold", int(32.0)), fg="#00F18C")
        self.Total_available_lbl.place(x=970, y=160)

        #for lower part

        self.customer_list= ImageTk.PhotoImage(file="admin grey dashbooard.png")
        canvas.create_image(790, 500, image=self.customer_list)

        self.customer_id1 = Label(root, text="RA0001", bg="#ECECEC",
                                         font=("Poppins Regular", int(10.0)), fg="#110445")
        self.customer_id1 .place(x=395, y=370)

        self.customer_fullname1 = Label(root, text="Otali Samuel", bg="#ECECEC",
                                  font=("Poppins Regular", int(10.0)), fg="#110445")
        self.customer_fullname1.place(x=590, y=370)

        # self.customer_status1 = Label(root, text="Otali Samuel", bg="#ECECEC",
        #                                 font=("Poppins Regular", int(10.0)), fg="#110445")
        # self.customer_status1.place(x=590, y=370)

        self.customer_trips1 = Label(root, text="10", bg="#ECECEC",
                                  font=("Poppins Regular", int(10.0)), fg="#110445")
        self.customer_trips1.place(x=985, y=370)

        self.edit_button = PhotoImage(file=f"edit button.png")
        edit_button = Button(root, image=self.edit_button, borderwidth=0, highlightthickness=0, command=btn_clicked,
                    relief="flat")
        edit_button.place(x=1073, y=367, width=65, height=25)

        self.delete_button = PhotoImage(file=f"delete button.png")
        delete_button= Button(root, image=self.delete_button, borderwidth=0, highlightthickness=0, command=btn_clicked,
                    relief="flat")
        delete_button.place(x=1160, y=367, width=65, height=25)


        # # Seat Full Name Text
        # canvas.create_text(515, 235, text="Full Name  ", fill="#110445", anchor="w",
        #                     font=("Poppins Medium", int(10.0)))
        #
        # self.fullname_lbl = Label(root, text="Otali Samuel", bg="#ffffff",
        #                                 font=("Poppins Medium", int(10.0)), fg="#110445")
        # self.fullname_lbl.place(x=680, y=220)
        #
        # # Seat Placement Text
        # canvas.create_text(515, 263, text="Seat Placement  ", fill="#110445", anchor="w",
        #                    font=("Poppins Medium", int(10.0)))
        #
        # self.seatPlacement_lbl = Label(root, text="Business/A1", bg="#ffffff",
        #                           font=("Poppins Medium", int(10.0)), fg="#110445")
        # self.seatPlacement_lbl.place(x=680, y=248)
        #
        # # Seat Booking Code Text
        # canvas.create_text(555, 300, text="Booking Code  ", fill="#110445", anchor="w",
        #                    font=("Poppins Medium", int(10.0)))
        #
        # self.BookingCode_lbl = Label(root, text="B000001", bg="#ffffff",
        #                           font=("Poppins Medium", int(10.0)), fg="#110445")
        # self.BookingCode_lbl.place(x=660, y=286)





def destination():
    entry0 = [""]




def btn_clicked():
    print("Button Clicked")


root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, height=720, width=1280, bd=0, highlightthickness=0, relief="ridge", bg="#110445")
background_img = PhotoImage(file=f"admin_white bg.png")
background = canvas.create_image(800, 360.0, image=background_img)
canvas.place(x=0, y=0)
root.resizable(False, False)
root.title("Seat Page")
app = Application(root)
app.mainloop()
