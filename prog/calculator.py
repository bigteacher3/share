import tkinter as tk

# Глобальні змінні
current_value = ""
last_result = 0
last_operator = None

def update_display(text):
    display.delete(0, tk.END)
    display.insert(0, text)

def on_number_click(n):
    global current_value
    current_value += n
    update_display(current_value)

def on_operator_click(op):
    global current_value, last_result, last_operator

    if current_value:
        if last_operator:
            last_result = compute(last_result, float(current_value), last_operator)
        else:
            last_result = float(current_value)
        current_value = ""
    last_operator = op
    update_display(str(last_result))

def on_equals():
    global current_value, last_result, last_operator
    if current_value and last_operator:
        last_result = compute(last_result, float(current_value), last_operator)
        update_display(str(last_result))
        current_value = ""
        last_operator = None

def on_clear():
    global current_value, last_result, last_operator
    current_value = ""
    last_result = 0
    last_operator = None
    update_display("0")

def compute(a, b, op):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/": return a / b if b != 0 else 0
    return b

# Створення вікна
root = tk.Tk()
root.title("Калькулятор")
root.geometry("420x400")


display = tk.Entry(root, font=("Arial", 24), justify="right", bd=10, relief="ridge")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")
display.insert(0, "0")
# Кнопки
buttons = [
    ('7', on_number_click), ('8', on_number_click), ('9', on_number_click), ('/', on_operator_click),
    ('4', on_number_click), ('5', on_number_click), ('6', on_number_click), ('*', on_operator_click),
    ('1', on_number_click), ('2', on_number_click), ('3', on_number_click), ('-', on_operator_click),
    ('0', on_number_click), ('.', on_number_click), ('C', lambda _: on_clear()), ('+', on_operator_click),
    ('=', lambda _: on_equals())
]

row = 1
col = 0
for text, action in buttons:
    btn = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text, a=action: a(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1



root.mainloop()
