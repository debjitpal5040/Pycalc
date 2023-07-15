"""This is a simple calculator made with Python and Tkinter."""
from tkinter import Button, Entry, StringVar, Tk

expression = ""


def press(num):
    """This function is used to update the expression in the text entry box"""
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    """This function is used to evaluate the final expression"""
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except ValueError:
        equation.set("error")
        expression = ""


def clear():
    """This function is used to clear the text entry box"""
    global expression
    expression = ""
    equation.set("")


gui = Tk()
gui.configure()
gui.title("PyCalc")
equation = StringVar()

# all units are in cm

Entry(
    gui,
    bg="black",
    fg="white",
    selectbackground="red",
    selectforeground="blue",
    textvariable=equation,
    justify="right",
    font=("Ubuntu", 30),
    bd=10,
).grid(columnspan=4)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="CA",
    fg="black",
    bg="red",
    font=("arial", 20, "bold"),
    command=clear,
).grid(row=3, column=0)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="mod",
    fg="black",
    bg="pink",
    font=("arial", 20, "bold"),
    command=lambda: press("%"),
).grid(row=3, column=1)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="(",
    fg="black",
    bg="powder blue",
    font=("arial", 20, "bold"),
    command=lambda: press("("),
).grid(row=3, column=2)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    fg="black",
    text=")",
    bg="powder blue",
    font=("arial", 20, "bold"),
    command=lambda: press(")"),
).grid(row=3, column=3)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="7",
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(7),
).grid(row=4, column=0)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="8",
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(8),
).grid(row=4, column=1)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="9",
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(9),
).grid(row=4, column=2)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="÷",
    fg="black",
    bg="yellow",
    font=("arial", 20, "bold"),
    command=lambda: press("/"),
).grid(row=4, column=3)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="4",
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(4),
).grid(row=5, column=0)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="5",
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(5),
).grid(row=5, column=1)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="6",
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(6),
).grid(row=5, column=2)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="x",
    fg="black",
    bg="yellow",
    font=("arial", 20, "bold"),
    command=lambda: press("*"),
).grid(row=5, column=3)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="1",
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(1),
).grid(row=6, column=0)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="2",
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(2),
).grid(row=6, column=1)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="3",
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(3),
).grid(row=6, column=2)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="-",
    fg="black",
    bg="yellow",
    font=("arial", 20, "bold"),
    command=lambda: press("-"),
).grid(row=6, column=3)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="0",
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(0),
).grid(row=7, column=0)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text=".",
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press("."),
).grid(row=7, column=1)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="=",
    fg="black",
    bg="green",
    font=("arial", 20, "bold"),
    command=equalpress,
).grid(row=7, column=2)

Button(
    gui,
    height=2,
    width=6,
    bd=4,
    text="+",
    fg="black",
    bg="yellow",
    font=("arial", 20, "bold"),
    command=lambda: press("+"),
).grid(row=7, column=3)

gui.mainloop()
