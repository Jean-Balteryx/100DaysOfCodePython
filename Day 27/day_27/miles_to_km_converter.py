import tkinter

# Creates the window
window = tkinter.Tk()
# Adds the title
window.title("Mile to Km Converter")
# Adds 20 px padding
window.config(padx=20, pady=20)

# Creates the miles input and places it on the grid
miles_input = tkinter.Entry(text="0", width=8)
miles_input.grid(column=1, row=0)


# Creates the "Miles" label and places it on the grid
miles_input_label = tkinter.Label(text="Miles")
miles_input_label.grid(column=2, row=0)


# Creates the "is equal to" label and places it on the grid
equal = tkinter.Label(text="is equal to")
equal.grid(column=0, row=1)


# Creates the kilometers value label and places it on the grid
km_value = tkinter.Label(text="0")
km_value.grid(column=1, row=1)


# Creates the "Km" label and places it on the grid
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)


# Creates the function that will convert the input and display it
def convert():
    result = round(float(miles_input.get()) * 1.60934)
    km_value.config(text=result)


# Creates the "Calculate" button, binds the convert() function to it and places it on the grid
calculate = tkinter.Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)



window.mainloop()