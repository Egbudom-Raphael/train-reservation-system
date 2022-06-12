from tkinter import *



def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#110445")
canvas = Canvas(
    window,
    bg = "#110445",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

background_img = PhotoImage(file = f"background2.png")
background = canvas.create_image(
    370, 360.0,
    image=background_img)
canvas.place(x = 0, y = 0)

### LOGOUT BUTTON ###
img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 1120, y = 27,
    width = 80,
    height = 22)


img8= PhotoImage(file=f"Img_logo.png")
b1 = Button(
    image= img8,
    borderwidth= 0,
    highlightthickness= 0 ,
    #command= btn_clicked(),
    relief= "flat")
b1.place(
    x = 100, y = 35,
    width = 120,
    height = 40)

img9= PhotoImage(file=f"train.png")


# ### Location switch button ###
#
# img_switch= PhotoImage(file=f"img1.png")
# b1 = Button(
#     image= img_switch,
#     borderwidth= 0,
#     highlightthickness= 0 ,
#     command= btn_clicked(),
#     relief= "flat")
# b1.place(
#     x = 420, y = 345,
#     width = 51.5,
#     height = 52)

### Next button ###
img_next= PhotoImage(file=f"img4.png")
b1 = Button(
    image= img_next,
    borderwidth= 0,
    highlightthickness= 0 ,
    command= btn_clicked(),
    activebackground="#110445",
    foreground="white",
    relief= "flat")
b1.place(
    x = 220, y = 580,
    width = 169,
    height = 56)



# ### "FROM" TEXT ENTRY SECTION ###
# entry0_img = PhotoImage(file = f"img_textBox0.png")
# entry0_bg = canvas.create_image(
#     310, 340,
#     image = entry0_img)
#
# entry0 = Entry(
#     bd = 0,
#     bg = "#F1F1F1",
#     highlightthickness = 0)
#
# entry0.place(
#     x = 140, y = 330,
#     width = 200.0,
#     height = 30)

# ### 'TO' TEXT ENTRY SECTION ###
#
# entry1_img = PhotoImage(file = f"img_textBox1.png")
# entry1_bg = canvas.create_image(
#     310, 420,
#     image = entry1_img)
#
# entry1 = Entry(
#     bd = 0,
#     bg = "#F1F1F1",
#     highlightthickness = 0)
#
# entry1.place(
#     x = 140, y = 410,
#     width = 200.0,
#     height = 30)

### TICKETS HEADER BUTTON ###
img_ticket_header = PhotoImage(file = f"tickets_header.png")
b1 = Button(
    image = img_ticket_header,
    borderwidth = 0,
    highlightthickness = 0,
    #command = btn_clicked,
    relief = "flat")

b1.place(
    x = 540, y = 27 ,
    width = 65,
    height = 40)


### Header Text'where do you want to go?'###
canvas.create_text(
   310, 165,
    text = "Select Seat",
    fill = "#110445",anchor= "w",
    font = ("Poppins SemiBold", int(13.0)))

### Available Indicator ###
img_availableIndicator= PhotoImage(file="indicator_available.png")
canvas.create_image(230,220,image=img_availableIndicator)

canvas.create_text(
   250, 223,
    text = "Available ",
    fill = "#110445",anchor= "w",
    font = ("Poppins Medium", int(12.0)))

############################
img_unavailableIndicator= PhotoImage(file="indicator_unavailable.png")
canvas.create_image(230,220,image=img_unavailableIndicator)

canvas.create_text(
   450, 223,
    text = "Unavailable",
    fill = "#110445",anchor= "w",
    font = ("Poppins Medium", int(12.0)))

img_unavailableIndicator= PhotoImage(file="indicator_unavailable.png")
canvas.create_image(430,220,image=img_unavailableIndicator)


# ### Train class sub heading###
# canvas.create_text(
#    110, 480,
#     text = "Select a train class: ",
#     fill = "#110445",anchor= "w",
#     font = ("Poppins Medium", int(12.0)))

# ### Regular Class Button ###
# img_regular = PhotoImage(file=f"regular.png")
# b1 = Button(
#     image= img_regular,
#     borderwidth= 0,
#     highlightthickness= 0 ,
#     command= btn_clicked(),
#     relief= "flat")
# b1.place(
#     x = 140, y = 500,
#     width = 103,
#     height = 46)

# ### Business Class Button ###
# img_business = PhotoImage(file=f"business.png")
# b1 = Button(
#     image= img_business,
#     borderwidth= 0,
#     highlightthickness= 0 ,
#     command= btn_clicked(),
#     relief= "flat")
# b1.place(
#     x = 250, y = 500,
#     width = 103,
#     height = 46)






window.resizable(False, False)
window.mainloop()
