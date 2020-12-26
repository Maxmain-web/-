#v 1.1
from tkinter import *
from datetime import datetime

root = Tk()

root['bg'] = '#d6def7'
root.title('Осталось до нового года')
#root.iconbitmap(r'D:/code/python/work/othcet.ico')
root.geometry('250x250')

root.resizable(width=False, height=False)

title = Label(root, text='До Нового Года\nосталось:', bg='#d6def7', font='Times 25', fg="#071d34")
title.pack()

current_datetime = datetime.now()
res = 31 - current_datetime.day

title = Label(root, text=res, bg='#d6def7', font='Times 50', fg="red")
title.pack()
title = Label(root, text="Дней", bg='#d6def7', font='Times 30', fg="red")
title.pack()

root.mainloop()