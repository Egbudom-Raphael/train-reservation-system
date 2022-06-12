import tkinter
from tkinter import *
from PIL import ImageTk




class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.create_widgets()
        self.place()

    def customerSignup_button(self):
        root.destroy()
        import Customer_signup

    def adminlogin_button(self):
        root.destroy()
        import Admin_login



    def create_widgets(self):
        try:
            def toggle_password():
                if passwd_entry.cget('show') == '':
                    passwd_entry.config(show='•')
                    toggle_btn.config(text='Show Password')
                else:
                    passwd_entry.config(show='')
                    toggle_btn.config(text='Hide Password')
        except TypeError:
            tkinter.messagebox.showerror('Error', 'No value input')
        except:
            pass

        def test():
            if username.get() == "Test".lower() and passwd_entry.get() == "12345":
                root.destroy()
                import customer_home
            else:
                passwd_entry.delete(0,END)
                wrong_details= tkinter.Label(root, text='Incorrect username or password', font="Poppins 9", fg='red', bg="#110445")
                wrong_details.place(x=550, y=210)


        background_img = PhotoImage(file = f"bg.png")
        background = canvas.create_image(
            850, 250,
            image=background_img)

        self.background_img = PhotoImage(file = f"railly logo.png")
        background = canvas.create_image(
            100, 56,
            image=self.background_img)


        #### Username TextBox ####
        self.username_img = PhotoImage(file = f"textBox1.png")
        entry6_bg = canvas.create_image(
            650, 299,
            image = self.username_img)

        username = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0, font="Poppins 10")


        username.place(
            x = 506, y = 280,
            width = 295,
            height = 40)

        #### Password TextBox ####

        self.password_img = PhotoImage(file = f"textBox1.png")
        entry7_bg = canvas.create_image(
            650, 400,
            image = self.password_img)

        passwd_entry = Entry(
            bd = 0,
            bg = "#ffffff",show= "•",
            highlightthickness = 0, font="Poppins 10")


        passwd_entry.place(
            x = 506, y = 380,
            width = 295,
            height = 40,
            )

        ### Green Login Button ###

        self.img0 = PhotoImage(file=f"loginButton.png")
        b0 = Button(
            image = self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=test,
            relief="flat")

        b0.place(
            x=535, y=478.37,
            width=217.2,
            height=50.2)

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

        #### For Admin Login button ####
        self.img1 = PhotoImage(file = f"admin login small.png")
        b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.adminlogin_button,
            relief = "flat")

        b1.place(
            x = 1088.37, y = 10,
            width = 120,
            height = 22)

        canvas.create_text(
            650, 180,
            text = "Customer Login",
            fill = "#ffffff",
            font = ("Poppins ExtraBold", int(26.0)))

        # Password Toggle
        toggle_btn= PhotoImage(file=f"eye toggle.png")
        show_pwd= Button(image= toggle_btn, borderwidth = 0, highlightthickness = 0,command = toggle_password, relief = "flat" )
        show_pwd.place(x= 768, y=389)

        # Customers Signup Button
        self.img3 = PhotoImage(file = f"Signup small.png")
        b3 = Button(image = self.img3, borderwidth=0, highlightthickness=0, command=self.customerSignup_button, relief="flat")

        b3.place(x=610, y=540, width=47, height=17)

        #root.bind('<Return>', test)



    # def testing(self):
    #     frame1.tkraise()



root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, height=720, width=1280, bd=0, highlightthickness=0, relief="ridge", bg="#110445")
canvas.place(x=0, y=0)
# frame1 = Frame(root, height= 720, width= 1280 , bg="white")
# frame1.place(relx=0, rely=0)
root.resizable(False, False)
app = Application(root)
app.mainloop()


root.resizable(False, False)
app.mainloop()
