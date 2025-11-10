"""
Create a simple calculator GUI using Tkinter with the following features:
Buttons for 0-9 digits.
Buttons for +, -, ×, ÷.
Button for =.
"""
import tkinter as tk
from tkinter import messagebox
import ast

def safe_eval(expr):
    """
    Safely evaluate a numeric expression containing only literals and
    arithmetic operators (+, -, *, /, %, **, unary + and -).
    """
    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                return left / right
            if isinstance(node.op, ast.Mod):
                return left % right
            if isinstance(node.op, ast.Pow):
                return left ** right
            raise ValueError("Unsupported binary operator")
        if isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            if isinstance(node.op, ast.UAdd):
                return +operand
            if isinstance(node.op, ast.USub):
                return -operand
            raise ValueError("Unsupported unary operator")
        if isinstance(node, ast.Num):  # Python <3.8
            return node.n
        if isinstance(node, ast.Constant):  # Python 3.8+
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Unsupported constant type")
        raise ValueError("Unsupported expression")

    parsed = ast.parse(expr, mode='eval')
    return _eval(parsed)

class Calculator:
    """Calculator(master)

    A simple Tkinter-based calculator widget class that constructs a basic GUI and
    handles button-driven arithmetic input and evaluation.

    This class builds a 4-column grid of buttons and a single-line entry display.
    It supports the decimal digits 0-9, the basic binary operators + and -, and the
    multiplication and division symbols × and ÷ (mapped to Python's '*' and '/').
    The '=' button evaluates the current expression using a provided safe_eval
    function; the 'C' button clears the current expression.

    Parameters
    ----------
    master : tkinter.Tk or tkinter.Frame
        The parent Tkinter container in which the calculator widgets will be
        created. The caller is responsible for providing an appropriate Tk/Toplevel
        or Frame instance.

    Class Attributes
    ----------------
    BUTTON_FONT : tuple
        Default font specifier used for calculator buttons (('arial', 18)).
    BUTTON_PADX : int
        Horizontal padding for each button (default 20).
    BUTTON_PADY : int
        Vertical padding for each button (default 20).

    Instance Attributes
    -------------------
    master : tkinter widget
        The parent container passed to the constructor.
    expression : str
        The textual arithmetic expression currently being edited/displayed.
    text_input : tkinter.StringVar
        Tkinter variable bound to the Entry widget, used for display/updates.
    entry : tkinter.Entry
        The text entry widget used to show the current expression/result.

    Public Methods
    --------------
    __init__(master)
        Create and lay out the Entry widget and calculator Buttons in a 4-column
        grid. Each button is bound to click_event via a lambda capturing the
        button label.

    click_event(key)
        Handle a button press. Behavior depends on key:
        - '=' : Replace '×' and '÷' with '*' and '/', evaluate the expression using
          safe_eval(expr), and update the display with the result. On evaluation
          errors, show an error dialog via messagebox.showerror and clear state.
        - 'C' : Clear the expression and display.
        - other : Append the key string to the expression and update the display.

    Notes
    -----
    - This class assumes the following names are available in the module scope:
      tk (tkinter), safe_eval (a function that evaluates arithmetic expressions
      safely), and messagebox (tkinter.messagebox). They are not provided by this
      class and must be imported/defined by the caller/module.
    # Comment: safe_eval MUST be safe and sandboxed; do not use eval on untrusted input.
    # Comment: The multiplication/division symbols are user-facing; they are mapped
    #          to Python operators before evaluation.
    # Comment: The GUI updates text_input and entry directly; this class is not
    #          thread-safe and should be used from the Tkinter main thread.
    # Comment: Layout uses a simple 4-column grid; button order is fixed and can be
    #          modified by changing the buttons list in __init__ if needed.

    Examples
    --------
    # Basic usage (module-level imports required):
    # import tkinter as tk
    # from your_module import Calculator, safe_eval
    #
    # root = tk.Tk()
    # calc = Calculator(root)
    # root.mainloop()
    """
    BUTTON_FONT = ('arial', 18)
    BUTTON_PADX = 20
    BUTTON_PADY = 20

    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        self.expression = ""
        self.text_input = tk.StringVar()
        self.entry = tk.Entry(master, font=('arial', 20, 'bold'), textvariable=self.text_input, bd=20, insertwidth=4, bg="powder blue", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '×',
            '0', '=', 'C', '÷'
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(master, text=button, padx=self.BUTTON_PADX, pady=self.BUTTON_PADY, font=self.BUTTON_FONT, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_event(self, key):
        if key == '=':
            try:
                expr = self.expression.replace('×', '*').replace('÷', '/')
                result = str(safe_eval(expr))
                self.text_input.set(result)
                self.expression = result
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.text_input.set("")
        elif key == 'C':
            self.expression = ""
            self.text_input.set("")
        else:
            self.expression += str(key)
            self.text_input.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

