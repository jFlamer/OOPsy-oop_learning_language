# import tkinter as tk
# from tkinter import simpledialog, messagebox, Toplevel, Label, Entry, Button
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
#     return custom_input_dialog(prompt)
#
#
# def custom_input_dialog(prompt_text):
#     # Różowe niestandardowe okno wejścia
#     dialog = Toplevel(root)
#     dialog.title("Input")
#     dialog.configure(bg="#ffe0f0")
#     dialog.geometry("300x120")
#     dialog.resizable(False, False)
#
#     prompt = Label(dialog, text=prompt_text, bg="#ffe0f0", fg="#800040", font=("Courier New", 10))
#     prompt.pack(pady=(10, 5))
#
#     entry = Entry(dialog, bg="#fff0f5", fg="black", font=("Courier New", 10))
#     entry.pack(pady=5)
#
#     result = {"value": None}
#
#     def on_submit():
#         result["value"] = entry.get()
#         dialog.destroy()
#
#     submit_btn = Button(dialog, text="Submit", bg="#ffb6c1", command=on_submit)
#     submit_btn.pack(pady=(5, 10))
#
#     dialog.grab_set()
#     root.wait_window(dialog)
#     return result["value"]
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
# # Kolory i czcionki
# bg_color = "#ffe6f0"
# text_bg_color = "#fff0f5"
# output_bg_color = "#fcd6e6"
# button_color = "#ffb6c1"
# text_fg_color = "#800040"
# font_name = "Courier New"
#
# # Główne okno
# root = tk.Tk()
# root.title("OOPsy Retro IDE")
# root.configure(bg=bg_color)
# root.geometry("700x600")
# # root.iconbitmap("heart.ico")
#
# frame = tk.Frame(root, bg=bg_color)
# frame.pack(padx=10, pady=10)
#
# code_label = tk.Label(frame, text="Code Editor:", bg=bg_color, fg=text_fg_color, font=(font_name, 10, "bold"))
# code_label.pack(anchor='w')
#
# code_text = tk.Text(frame, height=20, width=70, bg=text_bg_color, fg="black", insertbackground="black", font=(font_name, 10))
# code_text.pack()
#
# run_button = tk.Button(frame, text="Run", command=run_code, bg=button_color, fg="black", activebackground="#ffa6c9", font=(font_name, 10, "bold"))
# run_button.pack(pady=5)
#
# output_label = tk.Label(frame, text="Output:", bg=bg_color, fg=text_fg_color, font=(font_name, 10, "bold"))
# output_label.pack(anchor='w')
#
# output_text = tk.Text(frame, height=10, width=70, state='disabled', bg=output_bg_color, fg="black", font=(font_name, 10))
# output_text.pack()
#
# root.mainloop()
