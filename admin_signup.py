from tkinter import *
from PIL import ImageTk



class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.create_widgets()
        self.place()

    def customerLogin_button(self):
        root.destroy()
        import customer_login
    def adminlogin_button(self):
        root.destroy()
        import Admin_login

    def create_widgets(self):
        background_img = PhotoImage(file = f"bg.png")
        background = canvas.create_image(
            850, 250,
            image=background_img)

        background_img = PhotoImage(file = f"railly logo.png")
        background = canvas.create_image(
            100, 50,
            image=background_img)



        self.entry0_img = PhotoImage(file = f"textBox1.png")
        entry0_bg = canvas.create_image(
            460, 299,
            image = self.entry0_img)

        entry0 = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0, font="Poppins 10")

        #### Username Entry ####
        entry0.place(
            x = 318, y = 282,
            width = 287,
            height = 36)

        #### Username Fullname ####
        self.entry4_img = PhotoImage(file = f"textBox1.png")
        entry4_bg = canvas.create_image(
            790, 299,
            image = self.entry4_img)

        entry4 = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0, font="Poppins 10")

        #### Username Entry ####
        entry4.place(
            x = 650, y = 282,
            width = 287,
            height = 36)



        #### Username Email ##### ###
        self.entry5_img = PhotoImage(file = f"textBox1.png")
        entry5_bg = canvas.create_image(
            790, 400,
            image = self.entry5_img)

        entry5 = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0, font="Poppins 10")


        entry5.place(
            x = 655, y = 384,
            width = 287,
            height = 36)





        #### Password white text box area ###
        #### Password Entry ####
        self.entry1_img = PhotoImage(file = f"textBox1.png")
        entry1_bg = canvas.create_image(
            460, 400,
            image = self.entry1_img)

        entry1 = Entry(
            bd = 0,
            bg = "#ffffff",show= "•",
            highlightthickness = 0, font="Poppins 10")

        entry1.place(
            x = 318, y = 383,
            width = 287,
            height = 36,
            )

        self.img0 = PhotoImage(file = f"signup.png")
        b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            #command = btn_clicked,
            relief = "flat")

        b0.place(
            x = 580, y = 478.37,
            width = 155,
            height = 37)

        canvas.create_text(
            350, 250,
            text = "Username",
            fill = "#00f18c",
            font = ("Poppins SemiBold", int(11.0)))

        canvas.create_text(
            350, 353,
            text = "Password",
            fill = "#00f18c",
            font = ("Poppins SemiBold", int(11.0)))



        canvas.create_text(
            675, 250,
            text = "Full name",
            fill = "#00f18c",
            font = ("Poppins SemiBold", int(11.0)))

        canvas.create_text(
            688, 353,
            text = "Email Address",
            fill = "#00f18c",
            font = ("Poppins SemiBold", int(11.0)))




        self.img1 = PhotoImage(file = f"customer small login.png")
        b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.customerLogin_button,
            relief = "flat")

        b1.place(
            x = 1088.37, y = 10,
            width = 140,
            height = 30)

        canvas.create_text(
            650, 180,
            text = "Admin Signup",
            fill = "#00f18c",
            font = ("Poppins ExtraBold", int(26.0)))


                 #Admin Login Button

        self.img3 = PhotoImage(file = f"Login small.png")
        b3 = Button(
            image = self.img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.adminlogin_button,
            relief = "flat")

        b3.place(
            x = 630, y = 540,
            width = 47,
            height = 17)

root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, height=720, width=1280, bd=0, highlightthickness=0, relief="ridge",bg="#110445")
canvas.place(x=0, y=0)
root.resizable(False, False)
app = Application(root)
app.mainloop()

root.resizable(False, False)
app.mainloop()
