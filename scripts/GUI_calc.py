import tkinter as tk

def on_button_click(char):
    if char == '=':
        try:
            result = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif char == 'C':
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, char)

def create_button(text, row, col, width=4, height=2):
    button = tk.Button(root, text=text, command=lambda: on_button_click(text), width=width, height=height)
    button.grid(row=row, column=col)
    return button

# Set up the main application window
root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, font=("Arial", 16), justify="right")
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0), ('+', 4, 1), ('-', 4, 2),
    ('*', 5, 0), ('/', 5, 1), ('=', 5, 2),
    ('C', 6, 0)
]

for (text, row, col) in buttons:
    create_button(text, row, col)

root.mainloop()

