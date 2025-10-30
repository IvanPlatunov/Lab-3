from tkinter import *
from PIL import Image, ImageTk
from random import *
def generate():
    dec = str(int(txt.get(),16))
    alf = 'ABCDEF'
    key = ''
    for i in range(3):
        used = 0
        for j in range(5):
            r = randint(0,16)
            while str(r) == dec[0] or r == dec[1] or r == dec[2]:
                r = randint(0,16)
            flag = randint(0,1)
            if flag == 1 and not used:
                key += dec[i]
                used = 1
                continue
            if r < 10:
                key += str(r)
            else:
                key += alf[r-10-1]
        if used == 0:
            key = key[:-1]+dec[i]
        key+='-'
    key = key[:-1]
    key += ' '+dec[-2:]
    txt.delete(0, END)
    txt.insert(0, key)


window = Tk()
window.title('Keygen')
window.geometry('500x300')

im = Image.open("C:/Users/ivank/Downloads/Shadow Fiend.jpg")
bg = ImageTk.PhotoImage(im)
label1 = Label(image=bg)
label1.image = bg
label1.place(x=0, y=0,relwidth=1,relheight=1)
txt = Entry(window, width=30)
user_inp = txt.get()
btn = Button(window, text="Generate",command=generate)

btn.pack
txt.grid(column=1, row=0)
btn.grid(column=2,row=0)

window.mainloop()