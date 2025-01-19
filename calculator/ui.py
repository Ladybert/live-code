import tkinter as tk
from calculator.logic import calculate

class CalculatorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Kalkulator")
        self.window.geometry("300x400")
        
        self.expression = ""
        self.create_widgets()
    
    def create_widgets(self):
        # Display untuk kalkulator
        self.display = tk.Entry(self.window, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        # Tombol-tombol kalkulator
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('%', 5, 3),
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.window, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Menyesuaikan ukuran tombol secara proporsional
        for i in range(6):
            self.window.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.window.grid_columnconfigure(j, weight=1)

    def on_button_click(self, button_text):
        if button_text == "=":
            # Hitung ekspresi
            result = calculate(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = str(result)
        elif button_text == "C":
            # Hapus ekspresi
            self.expression = ""
            self.display.delete(0, tk.END)
        else:
            # Tambah simbol atau angka ke ekspresi
            self.expression += button_text
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def run(self):
        self.window.mainloop()
