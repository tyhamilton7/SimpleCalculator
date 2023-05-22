from tkinter import *

#create window
root = Tk()
root.title('MyCalculator')

#create entry space
e = Entry(root, width=35, borderwidth=10, bg = 'grey', fg = 'white')
e.grid(row=0, column=0, columnspan=5, padx=30, pady=10)

first_number = 0
op = None

def button_click(number):
    current = e.get()
    button_clear()
    e.insert(0, str(current) + str(number))

#operation functions
def button_clear():
    e.delete(0, END)

def button_op(given_op):
    global first_number
    first_number = e.get()
    global op
    op = given_op
    button_clear()

def button_equal():
    second_number = e.get()
    button_clear()

    match op:
        case "+":
            e.insert(0, int(first_number) + int(second_number))
        case "-":
            e.insert(0, int(first_number) - int(second_number))
        case "*":
            e.insert(0, int(first_number) * int(second_number))
        case "/":
            e.insert(0, int(first_number) / int(second_number))

#define number buttons
button_1 = Button(root, text="1", padx=40, pady=20, bg = 'grey', fg = 'white',command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg = 'grey', fg = 'white',command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg = 'grey', fg = 'white',command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg = 'grey', fg = 'white',command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg = 'grey', fg = 'white',command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg = 'grey', fg = 'white',command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg = 'grey', fg = 'white',command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg = 'grey', fg = 'white',command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg = 'grey', fg = 'white',command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg = 'grey', fg = 'white',command=lambda: button_click(0))
#define operator buttons
add_button = Button(root, text="+", padx=39, pady=20, bg = 'grey', fg = 'white', command=lambda: button_op("+"))
subtract_button = Button(root, text="-", padx=40, pady=20, bg = 'grey', fg = 'white', command=lambda: button_op("-"))
multiply_button = Button(root, text="*", padx=40, pady=20, bg = 'grey', fg = 'white', command=lambda: button_op("*"))
divide_button = Button(root, text="/", padx=40, pady=20, bg = 'grey', fg = 'white', command=lambda: button_op("/"))
clear_button = Button(root, text="CLEAR", padx=25, pady=20, bg = 'grey', fg = 'white', command=button_clear)
equal_button = Button(root, text="=", padx=40, pady=20, bg = 'grey', fg = 'white', command=button_equal)
#defining button placements
button_1.grid(row=3,column=0,columnspan=1)
button_2.grid(row=3,column=1,columnspan=1)
button_3.grid(row=3,column=2,columnspan=1)

button_4.grid(row=2,column=0,columnspan=1)
button_5.grid(row=2,column=1,columnspan=1)
button_6.grid(row=2,column=2,columnspan=1)

button_7.grid(row=1,column=0,columnspan=1)
button_8.grid(row=1,column=1,columnspan=1)
button_9.grid(row=1,column=2,columnspan=1)

button_0.grid(row=4,column=0,columnspan=1)

add_button.grid(row=1,column=3)
subtract_button.grid(row=2,column=3)
multiply_button.grid(row=3,column=3)
divide_button.grid(row=4, column=3)
clear_button.grid(row=4,column=2,columnspan=1)
equal_button.grid(row=4,column=1,columnspan=1)

root.mainloop()