from tkinter import *
import math
expr = ""

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")
def close_window():
    root.destroy()

if __name__ == "__main__":
    root = Tk()
    root.configure(bg="black")
    root.title("Simple Calculator")
    root.geometry("323x320")
    display = StringVar()
    entry = Entry(root, textvariable=display)
    entry.grid(columnspan=4,rowspan=2,ipadx=100,ipady=10)

    btn1 = Button(root, text='1', fg='black', bg='grey', command=lambda: press(1), height=1, width=7)
    btn1.grid(row=2, column=0,ipadx=10,ipady=15)
    btn2 = Button(root, text='2', fg='black', bg='grey', command=lambda: press(2), height=1, width=7)
    btn2.grid(row=2, column=1,ipadx=10,ipady=15)
    btn3 = Button(root, text='3', fg='black', bg='grey', command=lambda: press(3), height=1, width=7)
    btn3.grid(row=2, column=2,ipadx=10,ipady=15)
    btn4 = Button(root, text='4', fg='black', bg='grey', command=lambda: press(4), height=1, width=7)
    btn4.grid(row=3, column=0,ipadx=10,ipady=15)
    btn5 = Button(root, text='5', fg='black', bg='grey', command=lambda: press(5), height=1, width=7)
    btn5.grid(row=3, column=1,ipadx=10,ipady=15)
    btn6 = Button(root, text='6', fg='black', bg='grey', command=lambda: press(6), height=1, width=7)
    btn6.grid(row=3, column=2,ipadx=10,ipady=15)
    btn7 = Button(root, text='7', fg='black', bg='grey', command=lambda: press(7), height=1, width=7)
    btn7.grid(row=4, column=0,ipadx=10,ipady=15)
    btn8 = Button(root, text='8', fg='black', bg='grey', command=lambda: press(8), height=1, width=7)
    btn8.grid(row=4, column=1,ipadx=10,ipady=15)
    btn9 = Button(root, text='9', fg='black', bg='grey', command=lambda: press(9), height=1, width=7)
    btn9.grid(row=4, column=2,ipadx=10,ipady=15)
    btn0 = Button(root, text='0', fg='black', bg='grey', command=lambda: press(0), height=1, width=7)
    btn0.grid(row=5, column=0,ipadx=10,ipady=15)

    minus = Button(root, text='-', fg='black', bg='grey', command=lambda: press('-'), height=1, width=7)
    minus.grid(row=3, column=3,ipadx=10,ipady=15)
    mult = Button(root, text='*', fg='black', bg='grey', command=lambda: press('*'), height=1, width=7)
    mult.grid(row=2, column=3,ipadx=10,ipady=15)
    plus = Button(root, text='+', fg='black', bg='grey', command=lambda: press('+'), height=1, width=7)
    plus.grid(row=4, column=3,rowspan=2,ipadx=10,ipady=43)
    div = Button(root, text='/', fg='black', bg='grey', command=lambda: press('/'), height=1, width=7)
    div.grid(row=6, column=1,ipadx=10,ipady=15)

    eq = Button(root, text='=', fg='black', bg='grey', command=equal, height=1, width=7)
    eq.grid(row=5, column=2,ipadx=10,ipady=15)
    clr = Button(root, text='Clear', fg='black', bg='grey', command=clear, height=1, width=7)
    clr.grid(row=5, column=1,ipadx=10,ipady=15)

    dot = Button(root, text='.', fg='black', bg='grey', command=lambda: press('.'), height=1, width=7)
    dot.grid(row=6, column=0,ipadx=10,ipady=15)
    ext = Button(root, text='EXIT', fg='black', bg='grey', command=close_window, height=1, width=7)
    ext.grid(row=6, column=2,columnspan=2,ipadx=50,ipady=15)

    root.mainloop()