import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label
label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# label.pack()

label["text"] = "New Text"
label.config(text="New Text")
# label.place(x=100, y=200)
label.grid(column=0, row=0)
label.config(padx=50, pady=50)


# Button
def button_clicked():
    label.config(text=entry.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
entry = tkinter.Entry(width=10)
# entry.pack()
entry.grid(column=3, row=2)

window.mainloop()
