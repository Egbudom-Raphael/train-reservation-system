import tkinter
from tkinter import *
from PIL import ImageTk


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.create_widgets()
        self.place()


    def admin_login(self):
        print("button clicked")
    def Custom_login(self):
        root.destroy()
        import customer_login
    def adminSignup_button(self):
        root.destroy()
        import admin_signup

    def create_widgets(self):

        def toggle_password():
            if passwd_entry.cget('show') == '':
                passwd_entry.config(show='•')
                toggle_btn.config(text='Show Password')
            else:
                passwd_entry.config(show='')
                toggle_btn.config(text='Hide Password')


        # Test Login
        def test(self):
            if username.get() == "Admin".lower() and passwd_entry.get() == "12345":
                root.destroy()
                import customer_home
            else:
                passwd_entry.delete(0, END)
                wrong_details= tkinter.Label(root, text='Incorrect username or password', font="Poppins 9", fg='red', bg="#110445")
                wrong_details.place(x=560, y=210)


        self.background_img=PhotoImage(file=f"bg.png")
        background = canvas.create_image(
            850, 250,
            image=self.background_img)

        self.background_img = PhotoImage(file = f"railly logo.png")
        background = canvas.create_image(
            100, 56,
            image=self.background_img)

        #### Username TextBox ####
        self.username_img = PhotoImage(file = f"textBox1.png")
        username_bg = canvas.create_image(
            650, 299,
            image = self.username_img)

        username=Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0, font="Poppins 10")


        username.place(
            x = 506, y = 280,
            width = 295,
            height = 40)


        #### Password TextBox ####

        self.entry1_img = PhotoImage(file=f"textBox1.png")
        entry1_bg = canvas.create_image(650, 400, image=self.entry1_img)

        passwd_entry = Entry(
            bd = 0,
            bg = "#ffffff", show= "•",
            highlightthickness = 0,font="Poppins 10")


        passwd_entry.place(
            x = 506, y = 380,
            width = 295,
            height = 40,
            )

        ### Green Login Button ###
        self.loginButton = PhotoImage(file = f"loginButton.png")
        b0 = Button(
            image = self.loginButton,
            borderwidth = 0,
            highlightthickness=0,
            command=root.bind('<Return>', test),
            relief="flat")

        b0.place(
            x = 535, y = 478.37,
            width = 212,
            height = 50)

        canvas.create_text(
            530, 250,
            text = "Username",
            fill = "#00f18c",
            font = ("Poppins SemiBold", int(11.0)))

        canvas.create_text(
            530, 353,
            text = "Password",
            fill = "#00f18c",
            font = ("Poppins SemiBold", int(11.0)))

        #Customer Login Button
        self.img1 = PhotoImage(file = f"customer small login.png")
        b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command =  self.Custom_login ,
            relief = "solid")

        b1.place(
            x = 1088.37, y = 10,
            width = 140,
            height = 30)

        canvas.create_text(
            650, 180,
            text = "Admin Login",
            fill = "#00f18c",
            font = ("Poppins ExtraBold", int(26.0)))


        # # Admin Signup Button
        # self.img3 = PhotoImage(file = f"Signup small.png")
        # b3 = Button(
        #     image = self.img3,
        #     borderwidth = 0,
        #     highlightthickness = 0,
        #     #command = self.adminSignup_button,
        #     relief = "flat")
        #
        # b3.place(
        #     x = 610, y = 540,
        #     width = 47,
        #     height = 17)


        self.img_shield = PhotoImage(file = f"admin shield.png")
        b3 = Button(
            image = self.img_shield,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")

        b3.place(
            x = 770, y = 160,
            width = 34,
            height = 35)

        # Password Toggle
        toggle_btn = PhotoImage(file=f"eye toggle.png")
        show_pwd = Button(image=toggle_btn, borderwidth=0, highlightthickness=0, command=toggle_password, relief="flat")
        show_pwd.place(x=768, y=389)


root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, height=720, width=1280, bd=0, highlightthickness=0, relief="ridge",bg="#110445")
canvas.place(x=0, y=0)
root.resizable(False, False)
app = Application(root)
app.mainloop()

root.resizable(False, False)
app.mainloop()
