## 🔧 Tools

- **Source Language**: A simple, kid-friendly OOP language
- **Target Language**: Python
- **Toolchain**:
  - **ANTLR4**: Grammar parsing and AST generation
  - **Python**: Compiler / Translator logic
  - **PyCharm**: IDE for running generated Python code

---

## 🧒 Why a Kid-Friendly Language?

- Simplified OOP concepts (classes, inheritance, methods)
- Readable, natural syntax
- Hides complex Python features like `self`, `__init__`, etc.

---

## How we'll be using ANTLR4

1. **Design the Grammar**  
   Define your custom language grammar using ANTLR4 syntax.

   Example of a kid-friendly syntax:

   ```
   class Animal
       has name
       method speak
           print "The animal speaks"
   end

   class Dog inherits Animal
       method speak
           print "Woof!"
   end

   create myDog of Dog
   myDog.speak
   ```

2. **Generate Parser and Lexer**:
   ```bash
   antlr4 -Dlanguage=Python3 YourLang.g4
   ```

3. **Walk the AST** using visitor/listener in Python.

4. **Generate Python Code** based on your custom AST.

5. **Output Python File** to be used in PyCharm.

---

## 🧠 Design Considerations

- Kid-friendly syntax: minimal punctuation and symbols
- Error messages: friendly and educational
- Optional GUI to visualize class hierarchy and calls
- Modular development: start with basics, add features incrementally


