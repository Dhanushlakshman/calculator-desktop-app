import tkinter as tk

def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def on_button_click(button_text):
    current_text = entry.get()
    new_text = current_text + str(button_text)
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def on_clear_click():
    entry.delete(0, tk.END)

def on_equal_click():
    expression = entry.get()
    result = calculate_expression(expression)
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for the expression
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons
button_texts = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', 'C', '=', '/'
]

row_val = 1
col_val = 0

for text in button_texts:
    if text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, command=on_clear_click)
    elif text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, command=on_equal_click)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, command=lambda txt=text: on_button_click(txt))
    
    button.grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main event loop
root.mainloop()
