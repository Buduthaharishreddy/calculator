import tkinter as tk
from tkinter import font as tkfont


class CalculatorUI(tk.Tk):
    """
    Electronic Calculator UI with pastel color palette.
    """

    def __init__(self, logic_callback):
        super().__init__()
        self.logic_callback = logic_callback
        self.title("Pastel Calculator")
        self.geometry("350x500")
        self.minsize(300, 450)
        self.configure(bg="#FDFD96")  # Main background

        self.current_expression = ""
        
        # UI Setup
        self._create_widgets()
        self._setup_layout()

    def _create_widgets(self):
        """Creates the display and buttons for the calculator."""
        display_font = tkfont.Font(family="Helvetica", size=30, weight="bold")
        # Display area (entry widget)
        self.display = tk.Entry(
            self,
            state="readonly",
            readonlybackground="#FFFFFF",
            fg="#4A4A4A",
            font=display_font,
            insertwidth=3,
            bd=0,
            justify="right"
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20)

        # Buttons
        button_font = tkfont.Font(family="Helvetica", size=15, weight="normal")
        
        # Color palette
        colors = {
            "digit": "#C7CEEA",       # Pastel Blue/Purple
            "operator": "#FFDAC1",    # Pastel Orange
            "special": "#B5EAD7",     # Pastel Green
            "text": "#4A4A4A"
        }

        # Button data (Label, Row, Col, ColumnSpan, Type)
        buttons = [
            ("C", 1, 0, 1, "special"), ("/", 1, 1, 1, "operator"), ("*", 1, 2, 1, "operator"), ("-", 1, 3, 1, "operator"),
            ("7", 2, 0, 1, "digit"), ("8", 2, 1, 1, "digit"), ("9", 2, 2, 1, "digit"), ("+", 2, 3, 1, "operator"),
            ("4", 3, 0, 1, "digit"), ("5", 3, 1, 1, "digit"), ("6", 3, 2, 1, "digit"), ("=", 3, 3, 2, "special"),
            ("1", 4, 0, 1, "digit"), ("2", 4, 1, 1, "digit"), ("3", 4, 2, 1, "digit"),
            ("0", 5, 0, 2, "digit"), (".", 5, 2, 1, "digit")
        ]

        for label, row, col, span, b_type in buttons:
            btn = tk.Button(
                self,
                text=label,
                bg=colors[b_type],
                fg=colors["text"],
                font=button_font,
                activebackground="#E0E0E0",
                relief="flat",
                command=lambda l=label: self.on_button_click(l)
            )
            btn.grid(row=row, column=col, columnspan=span, sticky="nsew", padx=3, pady=3)

    def _setup_layout(self):
        """Configures the grid weights for responsiveness."""
        # Grid weight configuration for responsiveness
        for i in range(4):
            self.columnconfigure(i, weight=1)
        
        self.rowconfigure(0, weight=2)  # Display area takes more space
        for i in range(1, 6):
            self.rowconfigure(i, weight=1)

    def on_button_click(self, label):
        if label == "C":
            self.current_expression = ""
            self.update_display("")
        elif label == "=":
            result = self.logic_callback(self.current_expression)
            self.update_display(result)
            self.current_expression = result if result != "Error" else ""
        else:
            # Prevent double operators if needed or basic string addition
            # Simple approach: append character
            self.current_expression += str(label)
            self.update_display(self.current_expression)

    def update_display(self, text):
        self.display.configure(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, text)
        self.display.configure(state="readonly")


if __name__ == "__main__":
    # Test UI independently
    app = CalculatorUI(lambda expr: f"Eval: {expr}")
    app.mainloop()
