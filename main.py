from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.title('Keygen')
window.geometry('500x300')


im = Image.open("C:/Users/ivank/Downloads/Shadow Fiend.jpg")
bg = ImageTk.PhotoImage(im)
label1 = Label(image=bg)
label1.image = bg
label1.place(x=0, y=0)
txt = Entry(window, width=15)
btn = Button(window, text="Generate")
txt.grid(column=1, row=0)
btn.grid(column=2,row=0)
window.mainloop()