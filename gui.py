import tkinter as tk
from tkinter import simpledialog, messagebox
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
import re


from grammar.OOPsyLexer import OOPsyLexer
from grammar.OOPsyParser import OOPsyParser

from interpreter import Interpreter
from javaCompiler import JavaCompiler
from semantic_checker import SemanticChecker


def gui_print(*args):
    output_text.config(state='normal')
    output_text.insert(tk.END, " ".join(str(a) for a in args) + "\n")
    output_text.see(tk.END)
    output_text.config(state='disabled')


def gui_input(prompt=""):
    return simpledialog.askstring("Input", prompt)

class GUIErrorListener(ErrorListener):
    def __init__(self):
        super(GUIErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Line {line}:{column} - {msg}"
        print(error_msg)  # <--- debug
        self.errors.append(error_msg)


def update_line_numbers(event=None):
    line_num.config(state='normal')
    line_num.delete("1.0", tk.END)

    current_lines = code_text.index('end-1c').split('.')[0]
    line_num.insert("1.0", "\n".join(str(i + 1) for i in range(int(current_lines))))
    line_num.config(state='disabled')


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

        error_listener = GUIErrorListener()

        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)


        stream = CommonTokenStream(lexer)
        parser = OOPsyParser(stream)


        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)


        tree = parser.program()

        checker = SemanticChecker()
        try:
            checker.visit(tree)
        except Exception as e:
            messagebox.showerror("Semantic Error", str(e))
            return

        if error_listener.errors:
            messagebox.showerror("Syntax Error", "\n".join(error_listener.errors))
            return

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

    # except Exception as e:
    #     line_info = ""
    #     if hasattr(e, "line") and hasattr(e, "column"):
    #         line_info = f"\nLine {e.line}, column {e.column}"
    #     elif hasattr(e, "ctx") and hasattr(e.ctx, "start"):
    #         token = e.ctx.start
    #         line_info = f"\nLine {token.line}, column {token.column}"
    #
    #     messagebox.showerror("Error", f"{str(e)}{line_info}")


def highlight_syntax(event=None):
    code = code_text.get("1.0", tk.END)

    for tag in ["keyword", "type", "string", "char", "number", "bool", "comment", "operator"]:
        code_text.tag_remove(tag, "1.0", tk.END)

    patterns = [
        (
        r'\b(class|main|inherits|has|method|constructor|create|of|print|if|else|repeat|until|for|in|do|input|self|abstract|final|override|super|public|private|return|break|continue)\b',
        "keyword"),
        (r'\b(int|float|string|char|bool|list|dict)\b', "type"),
        (r'\btrue\b|\bfalse\b', "bool"),
        (r'"([^"\\]|\\.)*"', "string"),
        (r"'([^'\\]|\\.)'", "char"),
        (r'\b\d+\.\d+\b|\b\d+\b', "number"),
        (r'//.*', "comment"),
        (r'/\*.*?\*/', "comment"),
        (r'==|!=|>=|<=|&&|\|\||[+\-*/%=<>&|]', "operator"),
    ]

    for pattern, tag in patterns:
        for match in re.finditer(pattern, code):
            start_idx = f"1.0+{match.start()}c"
            end_idx = f"1.0+{match.end()}c"
            code_text.tag_add(tag, start_idx, end_idx)



#Styl
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

# code_text = tk.Text(frame, height=20, width=70, background=text_bg_color, fg="black", insertbackground="black")
# code_text.pack()
#numerowanie linii

code_frame = tk.Frame(root, bg=bg_color)
code_frame.pack()

line_num = tk.Text(code_frame, width=4, padx=5, takefocus=0, border=0,
                       background="#ffe6f0", state='disabled', fg=text_fg_color)
line_num.pack(side='left', fill='y')

code_text = tk.Text(code_frame, height=20, width=66, background=text_bg_color,
                    fg="black", insertbackground="black", undo=True)
code_text.pack(side="left", fill="both", expand=True)

code_text.bind("<KeyRelease>", update_line_numbers)
code_text.bind("<MouseWheel>", update_line_numbers)
code_text.bind("<Button-1>", update_line_numbers)
code_text.bind("<Return>", update_line_numbers)
code_text.bind("<BackSpace>", update_line_numbers)
code_text.bind("<Configure>", update_line_numbers)
code_text.bind("<KeyRelease>", highlight_syntax)


# Kolorowanie skladni

code_text.tag_config("keyword", foreground="#c71585")   # Medium Violet Red
code_text.tag_config("type", foreground="#ba55d3")      # Medium Orchid
code_text.tag_config("bool", foreground="#db7093")      # Pale Violet Red
code_text.tag_config("string", foreground="#da70d6")    # Orchid
code_text.tag_config("char", foreground="#dda0dd")      # Plum
code_text.tag_config("number", foreground="#ff69b4")    # Hot Pink
code_text.tag_config("comment", foreground="#d8bfd8")   # Thistle
code_text.tag_config("operator", foreground="#ee82ee")  # Violet


#aktualizacja
update_line_numbers()


scrollbar = tk.Scrollbar(code_frame, orient="vertical", command=lambda *args: (code_text.yview(*args), line_num.yview(*args)))
scrollbar.pack(side="right", fill="y")
code_text.configure(yscrollcommand=scrollbar.set)
line_num.configure(yscrollcommand=scrollbar.set)

run_button = tk.Button(frame, text="Run", command=run_code, background=button_color, fg="black",
                       activebackground="#ffa6c9")
run_button.pack(pady=5)

#Interpretera okienko
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
