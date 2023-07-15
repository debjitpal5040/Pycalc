"""This is a simple calculator made using Tkinter."""
from tkinter import Entry, StringVar, Tk

from tkmacosx import Button  # only for mac

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

# all units are in pixels

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
    height=25,
    width=75,
    bd=15,
    text="CA",
    highlightthickness=1,
    fg="black",
    bg="red",
    font=("arial", 20, "bold"),
    command=clear,
).grid(row=3, column=0)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="mod",
    highlightthickness=1,
    fg="black",
    bg="pink",
    font=("arial", 20, "bold"),
    command=lambda: press("%"),
).grid(row=3, column=1)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="(",
    highlightthickness=1,
    fg="black",
    bg="powder blue",
    font=("arial", 20, "bold"),
    command=lambda: press("("),
).grid(row=3, column=2)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text=")",
    highlightthickness=1,
    fg="black",
    bg="powder blue",
    font=("arial", 20, "bold"),
    command=lambda: press(")"),
).grid(row=3, column=3)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="7",
    highlightthickness=1,
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(7),
).grid(row=4, column=0)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="8",
    highlightthickness=1,
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(8),
).grid(row=4, column=1)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="9",
    highlightthickness=1,
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(9),
).grid(row=4, column=2)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="÷",
    highlightthickness=1,
    fg="black",
    bg="yellow",
    font=("arial", 20, "bold"),
    command=lambda: press("/"),
).grid(row=4, column=3)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="4",
    highlightthickness=1,
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(4),
).grid(row=5, column=0)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="5",
    highlightthickness=1,
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(5),
).grid(row=5, column=1)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="6",
    highlightthickness=1,
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(6),
).grid(row=5, column=2)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="x",
    highlightthickness=1,
    fg="black",
    bg="yellow",
    font=("arial", 20, "bold"),
    command=lambda: press("*"),
).grid(row=5, column=3)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="1",
    highlightthickness=1,
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(1),
).grid(row=6, column=0)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="2",
    highlightthickness=1,
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(2),
).grid(row=6, column=1)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="3",
    highlightthickness=1,
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(3),
).grid(row=6, column=2)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="-",
    highlightthickness=1,
    fg="black",
    bg="yellow",
    font=("arial", 20, "bold"),
    command=lambda: press("-"),
).grid(row=6, column=3)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="0",
    highlightthickness=1,
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press(0),
).grid(row=7, column=0)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text=".",
    highlightthickness=1,
    fg="black",
    bg="orange",
    font=("arial", 20, "bold"),
    command=lambda: press("."),
).grid(row=7, column=1)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="=",
    highlightthickness=1,
    fg="black",
    bg="green",
    font=("arial", 20, "bold"),
    command=equalpress,
).grid(row=7, column=2)

Button(
    gui,
    height=25,
    width=75,
    bd=15,
    text="+",
    highlightthickness=1,
    fg="black",
    bg="yellow",
    font=("arial", 20, "bold"),
    command=lambda: press("+"),
).grid(row=7, column=3)

gui.mainloop()
