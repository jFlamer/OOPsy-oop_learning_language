# import tkinter as tk
# from tkinter import simpledialog, messagebox
#
# from antlr4 import *
# from grammar.OOPsyLexer import OOPsyLexer
# from grammar.OOPsyParser import OOPsyParser
#
# from interpreter import Interpreter
#
#
# def gui_print(*args):
#     output_text.config(state='normal')
#     output_text.insert(tk.END, " ".join(str(a) for a in args) + "\n")
#     output_text.see(tk.END)
#     output_text.config(state='disabled')
#
#
# def gui_input(prompt=""):
#     return simpledialog.askstring("Input", prompt)
#
#
# def run_code():
#     code = code_text.get("1.0", tk.END)
#     output_text.config(state='normal')
#     output_text.delete("1.0", tk.END)
#     output_text.config(state='disabled')
#
#     try:
#         input_stream = InputStream(code)
#         lexer = OOPsyLexer(input_stream)
#         stream = CommonTokenStream(lexer)
#         parser = OOPsyParser(stream)
#         tree = parser.program()
#
#         interpreter = Interpreter(input_func=gui_input, print_func=gui_print)
#         interpreter.visit(tree)
#     except Exception as e:
#         messagebox.showerror("Error", str(e))
#
#
# # Kolory
# bg_color = "#ffe6f0"  # jasnoróżowe tło główne
# text_bg_color = "#fff0f5"  # tło edytora tekstu
# output_bg_color = "#fcd6e6"  # tło pola output
# button_color = "#ffb6c1"  # przycisk "Run"
# text_fg_color = "#800040"  # kolor tekstu (ciemniejszy róż/bordo)
#
# root = tk.Tk()
# root.title("OOPsy")
# root.configure(background=bg_color)
#
#
# frame = tk.Frame(root, bg=bg_color)
# frame.pack(padx=10, pady=10)
#
# code_label = tk.Label(frame, text="Code Editor:", background=bg_color, foreground=text_fg_color)
# code_label.pack(anchor='w')
#
# code_text = tk.Text(frame, height=20, width=70, background=text_bg_color, fg="black", insertbackground="black")
# code_text.pack()
#
# run_button = tk.Button(frame, text="Run", command=run_code, background=button_color, fg="black", activebackground="#ffa6c9")
# run_button.pack(pady=5)
#
# output_label = tk.Label(frame, text="Output:", background=bg_color, foreground=text_fg_color)
# output_label.pack(anchor='w')
#
# output_text = tk.Text(frame, height=10, width=70, state='disabled', bg=output_bg_color, fg="black")
# output_text.pack()
#
# root.mainloop()
#
#
#


import tkinter as tk
from tkinter import simpledialog, messagebox
from antlr4 import *

from grammar.OOPsyLexer import OOPsyLexer
from grammar.OOPsyParser import OOPsyParser

from interpreter import Interpreter
from javaCompiler import JavaCompiler


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

    java_text.config(state='normal')
    java_text.delete("1.0", tk.END)
    java_text.config(state='disabled')

    try:
        input_stream = InputStream(code)
        lexer = OOPsyLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = OOPsyParser(stream)
        tree = parser.program()

        #interpreter
        interpreter = Interpreter(input_func=gui_input, print_func=gui_print)
        interpreter.visit(tree)

        #kompilacja do Javy
        compiler = JavaCompiler()
        java_code = compiler.compile(tree)

        java_text.config(state='normal')
        java_text.insert(tk.END, java_code)
        java_text.config(state='disabled')

    except Exception as e:
        messagebox.showerror("Error", str(e))


# === Styl
bg_color = "#ffe6f0"
text_bg_color = "#fff0f5"
output_bg_color = "#fcd6e6"
button_color = "#ffb6c1"
text_fg_color = "#800040"

#start GUI
root = tk.Tk()
root.title("OOPsy")
root.configure(background=bg_color)

frame = tk.Frame(root, bg=bg_color)
frame.pack(padx=10, pady=10)

#Code editr
code_label = tk.Label(frame, text="Code Editor:", background=bg_color, foreground=text_fg_color)
code_label.pack(anchor='w')

code_text = tk.Text(frame, height=20, width=70, background=text_bg_color, fg="black", insertbackground="black")
code_text.pack()

run_button = tk.Button(frame, text="Run", command=run_code, background=button_color, fg="black",
                       activebackground="#ffa6c9")
run_button.pack(pady=5)

#Interpreter - okienko
output_label = tk.Label(frame, text="Interpreter Output:", background=bg_color, foreground=text_fg_color)
output_label.pack(anchor='w')

output_text = tk.Text(frame, height=10, width=70, state='disabled', bg=output_bg_color, fg="black")
output_text.pack()

#KOmpilator okienko
java_label = tk.Label(frame, text="Generated Java Code:", background=bg_color, foreground=text_fg_color)
java_label.pack(anchor='w')

java_text = tk.Text(frame, height=15, width=70, state='disabled', bg="#fbeff2", fg="black")
java_text.pack()

root.mainloop()
