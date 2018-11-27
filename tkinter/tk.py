from tkinter import *
clk = 0
clk_1 = 0
plusa = 0
plusb = 0

def btn_click():
    global clk
    global plusa
    clk += 1
    plusa += 1
    lba.config(text = "Button 1 clicked! {} ".format(plusa),bg = 'blue', fg = 'yellow')
    
def btn_click_1():
    global clk_1
    global plusb
    plusb +=1
    lba_1.config(text = "Button was clicked  {} times".format(plusb), bg = 'red', fg = 'black')
    clk_1 -= 1 
    
def ent_enter(event):
    global clk
    txt = ent.get()
    lbat.config(text = "Текст: " + txt,bg = 'red', fg = 'yellow')
                
# Cтворення вікна
root = Tk()
root.title('myWindow')
root.geometry('300x300+100+100')

# Поле Entry
ent = Entry(root)
ent.config(fg = "black", font = 'Courer_New 10')
ent.insert(0, 'ABCD')
ent.bind('<Return>', ent_enter)
ent.pack(side = TOP)

# Мітка Text here
lbat = Label(root)
lbat.config(text = 'Text here')
lbat.pack(side = TOP)

# Мітка Label
lba = Label(root)
lba.config(text = 'Мітка_1')
lba.pack(side = TOP)

# Мітка Label1
lba_1 = Label(root)
lba_1.config(text= 'Мітка_2')
lba_1.pack(side = BOTTOM)

# Кнопка Button
btn = Button(root, text = 'Нажми!', command = btn_click)
btn_1 = Button(root, text = 'Click me', command = btn_click_1)
btn.pack(side = LEFT)
btn_1.pack(side = RIGHT)
root.mainloop()
