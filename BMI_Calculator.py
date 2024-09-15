from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+500+100")
root.resizable(False,False)
root.configure(bg = "#f0f1f5")

def BMI():
    h = float(Height.get())
    w = float(Weight.get())
    m = h/100
    bmi = round(float(w/m**2),1)
    label1.config(text = bmi)

    if bmi<18.5:
        label2.config(text = "Underweight!")
        label3.config(text = "You have weight less than normal body! \n Doctors may suggest to gain weight!")

    elif bmi>=18.5 and bmi<24.9:
        label2.config(text = "Normal!")
        label3.config(text = "You have healthy body! Keep it up!")

    elif bmi>=24.9 and bmi<30:
        label2.config(text = "Overweight!")
        label3.config(text = "You have weight slightly more \n normal body! \n Doctors may advise to lose some weight for \n health reasons!")

    else:
        label2.config(text = "Obese!")
        label3.config(text = "Healt may be at risk if you do not lose weight!")

image_icon = PhotoImage(file = "icon.png")
root.iconphoto(False,image_icon)

top_frame = Frame(root,background = "#deded9",width = 470,height=80)
top_frame.place(x=0,y=0)

top = Label(top_frame,text = "BMI CALCULATOR",font = "Haventica 30 bold")
top.place(x=60,y=12)

Label(root,width = 72,height = 18,bg = "lightblue").pack(side=BOTTOM)

box = PhotoImage(file = "box.png")
Label(root,image = box).place(x=20,y=100)
Label(root,text = "Height (in cm)",font = "arial 18 bold").place(x=50,y=115)
Label(root,image = box).place(x=240,y=100)
Label(root,text = "Weight (in Kg)",font = "arial 18 bold").place(x=265,y=115)

scale = PhotoImage(file = "scale.png")
Label(root,image = scale,bg = "lightblue").place(x=20,y=310)


current_value = DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())

    size = int(float(get_current_value()))
    img = (Image.open("man.png"))
    resized_image = img.resize((50,10+size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image = photo2)
    secondimage.place(x=70,y=550-size)
    secondimage.image=photo2

style = ttk.Style()
style.configure("TScale",background = "white")
slider = ttk.Scale(root,from_=0,to=220,orient = 'horizontal',style = "TScale",command = slider_changed,variable = current_value)
slider.place(x=80,y=250)

current_value2 = DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

style2 = ttk.Style()
style2.configure("TScale",background = "white")
slider2 = ttk.Scale(root,from_=0,to=200,orient = 'horizontal',style = "TScale",command = slider_changed2,variable = current_value2)
slider2.place(x=300,y=250)









Height = StringVar()
Weight = StringVar()
height = Entry(root,textvariable = Height,width = 5,font = "arial 50",bg = "#fff",fg = "#000",justify = CENTER)
height.place(x=35,y=160)
Height.set(get_current_value())
weight = Entry(root,textvariable = Weight,width = 5,font = "arial 50",bg = "#fff",fg = "#000",justify = CENTER)
weight.place(x=255,y=160)
Weight.set(get_current_value2())


secondimage = Label(root,bg = "lightblue")
secondimage.place(x=70,y=530)


Button(root,text = "View Report",width = 15,height = 2,font = "arial 10 bold",bg = "#1f6e68",fg = "white",command = BMI).place(x=310,y=320)

label1 = Label(root,font = "arial 50 bold",bg = "lightblue",fg = "#fff")
label1.place(x=125,y=305)

label2 = Label(root,font = "arial 30 bold",bg = "lightblue",fg = "#3b3a3a")
label2.place(x=170,y=420)

label3 = Label(root,font = "arial 10 bold",bg = "lightblue")
label3.place(x=160,y=500)





root.mainloop()
