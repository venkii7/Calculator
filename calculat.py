import tkinter as tk

# Function to update the input field
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry_input.get()))
            entry_input.set(result)
        except Exception as e:
            entry_input.set("Error")
    elif text == "C":
        entry_input.set("")
    else:
        entry_input.set(entry_input.get() + text)

# Setting up the main window
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("300x400")

# Entry widget to display inputs and results
entry_input = tk.StringVar()
entry = tk.Entry(root, textvar=entry_input, font="lucida 20 bold", bd=10, relief=tk.SUNKEN)
entry.pack(fill=tk.BOTH, ipadx=8)

# Creating buttons for the calculator
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 0, 0
for button in buttons:
    b = tk.Button(button_frame, text=button, font="lucida 15 bold", relief=tk.RAISED, bd=5)
    b.grid(row=row, column=col, padx=10, pady=10)
    b.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Main loop to run the application
root.mainloop()