import tkinter as tk
from tkinter import messagebox
import math
import random

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("500x700")
        self.root.config(bg="#f4f4f4")  # Light theme by default

        self.result = ""
        self.is_dark_theme = False  # Default to light theme
        self.font_size = 22  # Larger font size for better readability

        # Display area (with higher contrast for better accessibility)
        self.display = tk.Entry(self.root, text=self.result, font=("Arial", self.font_size), bd=10, relief="sunken", justify="right", bg="#ffffff", fg="#000000")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons and design
        self.create_buttons()

        # Bind keyboard events for accessibility
        self.root.bind("<Return>", lambda event: self.on_button_click("="))
        self.root.bind("<BackSpace>", lambda event: self.clear_display())
        self.root.bind("<Key>", self.handle_keyboard_input)

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('sqrt', 5, 3),
            ('log', 6, 0), ('ln', 6, 1), ('exp', 6, 2), ('pi', 6, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", self.font_size), width=5, height=2, command=lambda t=text: self.on_button_click(t), relief="solid", bg="#0078d4", fg="white")
            button.grid(row=row, column=column, padx=5, pady=5)

        # Clear button
        clear_button = tk.Button(self.root, text="C", font=("Arial", self.font_size), width=5, height=2, command=self.clear_display, relief="solid", bg="#cc0000", fg="white")
        clear_button.grid(row=7, column=0, columnspan=4, pady=10)

        # Theme switch and color change button
        self.theme_button = tk.Button(self.root, text="Switch Theme", font=("Arial", self.font_size), width=20, height=2, command=self.switch_theme, relief="solid", bg="#4CAF50", fg="white")
        self.theme_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        # Button for random color change
        self.random_color_button = tk.Button(self.root, text="Random Colors", font=("Arial", self.font_size), width=20, height=2, command=self.change_random_colors, relief="solid", bg="#FF9800", fg="white")
        self.random_color_button.grid(row=8, column=2, columnspan=2, padx=10, pady=10)

    def handle_keyboard_input(self, event):
        """Handle keyboard input for calculator."""
        key = event.char
        if key.isdigit() or key in "+-*/.":
            self.on_button_click(key)
        elif key == "=":
            self.on_button_click("=")
        elif key == "c" or key == "C":
            self.clear_display()

    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                result = eval(self.result, {"__builtins__": None}, {"sin": math.sin, "cos": math.cos, "tan": math.tan, 
                                                                 "sqrt": math.sqrt, "log": math.log10, "ln": math.log, 
                                                                 "exp": math.exp, "pi": math.pi, "e": math.e})
                self.result = str(result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.result)
            except Exception as e:
                messagebox.showerror("Error", f"Calculation error: {e}")
        else:
            self.result += str(button_text)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.result)

    def clear_display(self):
        self.result = ""
        self.display.delete(0, tk.END)

    def switch_theme(self):
        if self.is_dark_theme:
            self.root.config(bg="#f4f4f4")
            self.display.config(bg="#ffffff", fg="#000000")
            self.theme_button.config(bg="#555555")
            self.is_dark_theme = False
            self.update_button_colors("#000000", "#f4f4f4")
        else:
            self.root.config(bg="#1e1e1e")
            self.display.config(bg="#333333", fg="#ffffff")
            self.theme_button.config(bg="#4CAF50")
            self.is_dark_theme = True
            self.update_button_colors("#ffffff", "#333333")

    def update_button_colors(self, text_color, bg_color):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(fg=text_color, bg=bg_color)

    def change_random_colors(self):
        """Change background and button colors randomly."""
        random_colors = ['#0078d4', '#ff6347', '#32cd32', '#ff9800', '#8a2be2', '#f44336', '#4CAF50']
        random_button_bg = random.choice(random_colors)
        random_display_bg = random.choice(random_colors)
        random_button_fg = random.choice(['white', 'black'])

        self.root.config(bg=random_display_bg)
        self.display.config(bg=random_display_bg, fg=random_button_fg)
        self.update_button_colors(random_button_fg, random_button_bg)

# Create main window
root = tk.Tk()
calculator = ScientificCalculator(root)
root.mainloop()
