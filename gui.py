import tkinter as tk
from tkinter import simpledialog, messagebox

from antlr4 import *
from grammar.OOPsyLexer import OOPsyLexer
from grammar.OOPsyParser import OOPsyParser

from interpreter import Interpreter


def gui_print(*args):
    output_text.config(state='normal')
    output_text.insert(tk.END, " ".join(str(a) for a in args) + "\n")
    output_text.see(tk.END)
    output_text.config(state='disabled')


def gui_input(prompt=""):
    return simpledialog.askstring("Input", prompt)


def run_code():
    code = code_text.get("1.0", tk.END)
    output_text.config(state='normal')
    output_text.delete("1.0", tk.END)
    output_text.config(state='disabled')

    try:
        input_stream = InputStream(code)
        lexer = OOPsyLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = OOPsyParser(stream)
        tree = parser.program()

        interpreter = Interpreter(input_func=gui_input, print_func=gui_print)
        interpreter.visit(tree)
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("OOPsy")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

code_label = tk.Label(frame, text="Code Editor:")
code_label.pack(anchor='w')

code_text = tk.Text(frame, height=20, width=70)
code_text.pack()

run_button = tk.Button(frame, text="Run", command=run_code)
run_button.pack(pady=5)

output_label = tk.Label(frame, text="Output:")
output_label.pack(anchor='w')

output_text = tk.Text(frame, height=10, width=70, state='disabled', bg='#f0f0f0')
output_text.pack()

root.mainloop()
