# OOPsy-OOP Learning Language
## Authors 
Natalia Dybczak & Jagoda Flejmer 
## Contact 
ndybczak@student.agh.edu.pl

jflejmer@student.agh.edu.pl
## Goals 
Creating an educational programming language aimed at helping young learners grasp object-oriented programming in an intuitive and accessible way, along with a compiler that translates the code into Python.

## Implementation language
Python was chosen for its readability, simplicity, and widespread use in education. Python also offers robust support for building interpreters and compilers, including libraries for lexical and syntax analysis.

## Scanner & Parser implementation
The scanner and parser will be implemented using ANTLR 4, a powerful parser generator that supports multiple target languages, including Python.
ANTLR will be used to define the grammar of the language, from which it will automatically generate the lexer (scanner) and parser components. These components will then be integrated into the Python-based compiler.

## Tokens
---
### **Data Types & Literals**

| Name                          | Regex                          | Description |
|-------------------------------|--------------------------------|-------------|
| TYPE_INT                      | `int`                          | Keyword for integer type |
| TYPE_FLOAT                    | `float`                        | Keyword for floating-point type |
| TYPE_CHAR                     | `char`                         | Keyword for character type |
| TYPE_STRING                   | `string`                       | Keyword for string type |
| TYPE_BOOL                     | `bool`                         | Keyword for boolean type |
| BOOL_LITERAL_TRUE             | `true`                         | Boolean literal (true) |
| BOOL_LITERAL_FALSE            | `false`                        | Boolean literal (false) |
| INT_LITERAL                   | `[0-9]+`                       | Integer literal |
| FLOAT_LITERAL                 | `[0-9]+\.[0-9]+`               | Floating-point literal |
| CHAR_LITERAL                  | `'[^\\]'`                     | Character literal |
| STRING_LITERAL                | `".*?"`                        | String literal |

---

### **Operators**

| Name                          | Regex                          | Description |
|-------------------------------|--------------------------------|-------------|
| PLUS_OPERATOR                 | `\+`                           | Addition operator |
| MINUS_OPERATOR                | `-`                            | Subtraction operator |
| MULTIPLY_OPERATOR             | `\*`                           | Multiplication operator |
| DIVIDE_OPERATOR               | `/`                            | Division operator |
| MODULO_OPERATOR               | `%`                            | Modulo operator |
| INCREMENT_OPERATOR            | `\+\+`                         | Increment operator |
| DECREMENT_OPERATOR            | `--`                           | Decrement operator |
| ASSIGNMENT_OPERATOR           | `=`                            | Assignment operator |
| ADDITION_ASSIGNMENT_OPERATOR | `\+=`                          | Addition assignment |
| SUBTRACTION_ASSIGNMENT_OPERATOR | `-=`                        | Subtraction assignment |
| MULTIPLICATION_ASSIGNMENT_OPERATOR | `\*=`                  | Multiplication assignment |
| DIVISION_ASSIGNMENT_OPERATOR | `/=`                           | Division assignment |
| EQUAL_OPERATOR                | `==`                           | Equality check |
| UNEQUAL_OPERATOR              | `!=`                           | Inequality check |
| GREATER_OPERATOR              | `>`                            | Greater-than operator |
| LESSER_OPERATOR               | `<`                            | Less-than operator |
| GREATER_EQ_OPERATOR          | `>=`                           | Greater-or-equal operator |
| LESSER_EQ_OPERATOR           | `<=`                           | Less-or-equal operator |
| AND_OPERATOR                 | `&&`                           | Logical AND operator |
| OR_OPERATOR                  | `\|\|`                         | Logical OR operator |

---

### **Symbols & Separators**

| Name               | Regex          | Description |
|--------------------|----------------|-------------|
| LEFT_BRACKET       | `\[`          | Opening square bracket |
| RIGHT_BRACKET      | `\]`          | Closing square bracket |
| LEFT_PARENTHESIS   | `\(`          | Opening parenthesis |
| RIGHT_PARENTHESIS  | `\)`          | Closing parenthesis |
| LEFT_BRACE         | `{`            | Opening curly brace |
| RIGHT_BRACE        | `}`            | Closing curly brace |
| DOT_SEPARATOR      | `\.`          | Dot separator (e.g., for methods) |
| COMMA_SEPARATOR    | `,`            | Comma separator |
| COLON_SEPARATOR    | `:`            | Colon separator |
| SEMICOLON_SEPARATOR| `;`            | Semicolon end of statement |

---

### **Comments & Whitespace**

| Name            | Regex             | Description |
|------------------|-------------------|-------------|
| LINE_COMMENT     | `//.*`            | Single-line comment |
| BLOCK_COMMENT    | `/\*.*?\*/`       | Multi-line comment |
| WHITESPACE       | `[ \t\r\n]+`      | Whitespace (to be skipped) |

---

### **OOP Keywords**

| Name                      | Regex         | Description |
|---------------------------|---------------|-------------|
| CLASS_KEYWORD            | `class`       | Keyword to define a class |
| INHERITS_KEYWORD         | `inherits`    | Keyword to declare inheritance |
| HAS_ATTRIBUTE_KEYWORD    | `has`         | Keyword to declare attributes |
| METHOD_KEYWORD           | `method`      | Keyword to declare methods |
| CONSTRUCTOR_KEYWORD      | `constructor` | Keyword to define constructor |
| CREATE_KEYWORD           | `create`      | Keyword to instantiate objects |
| OF_STATEMENT             | `of`          | Used in constructs like `create X of Y` |
| SELF_KEYWORD             | `self`        | Reference to current object |
| ABSTRACT_CLASS           | `abstract`    | Declares a class as abstract |
| FINAL_CLASS              | `final`       | Declares a class as non-inheritable |
| OVERRIDE_METHOD          | `override`    | Indicates method override |
| SUPER_CALL               | `super`       | Call to parent class method |
| PUBLIC_MODIFIER          | `public`      | Public access modifier |
| PRIVATE_MODIFIER         | `private`     | Private access modifier |
| LIST_TYPE                | `list`        | Declares a list type |
| DICTIONARY_TYPE          | `dict`        | Declares a dictionary type |

---

### **Control Flow Keywords**

| Name                | Regex        | Description |
|---------------------|-------------|-------------|
| PRINT_KEYWORD       | `print`     | Keyword for printing values |
| IF_KEYWORD          | `if`        | Conditional keyword |
| ELSE_KEYWORD        | `else`      | Alternate branch keyword |
| REPEAT_KEYWORD      | `repeat`    | Loop keyword |
| UNTIL_KEYWORD       | `until`     | Loop exit condition keyword |
| INPUT_STATEMENT     | `input`     | Keyword to read user input |
| RETURN_STATEMENT    | `return`    | Keyword for returning from a function |
| BREAK_STATEMENT     | `break`     | Keyword to exit a loop early |
| CONTINUE_STATEMENT  | `continue`  | Keyword to skip to next loop iteration |
| PRINT_KEYWORD                | `print`                        | Keyword for printing values |
| IF_KEYWORD                   | `if`                           | Conditional keyword |
| ELSE_KEYWORD                 | `else`                         | Alternate branch keyword |
| REPEAT_KEYWORD               | `repeat`                       | Loop keyword |
| UNTIL_KEYWORD                | `until`                        | Loop exit condition keyword |
| INPUT_STATEMENT              | `input`                        | Keyword to read user input |
| SELF_KEYWORD                 | `self`                         | Reference to current object |
| ABSTRACT_CLASS               | `abstract`                     | Declares a class as abstract |
| FINAL_CLASS                  | `final`                        | Declares a class as non-inheritable |
| OVERRIDE_METHOD              | `override`                     | Indicates method override |
| SUPER_CALL                   | `super`                        | Call to parent class method |
| PUBLIC_MODIFIER              | `public`                       | Public access modifier |
| PRIVATE_MODIFIER             | `private`                      | Private access modifier |
| LIST_TYPE                    | `list`                         | Declares a list type |
| DICTIONARY_TYPE              | `dict`                         | Declares a dictionary type |
| RETURN_STATEMENT             | `return`                       | Keyword for returning from a function |
| BREAK_STATEMENT              | `break`                        | Keyword to exit a loop early |
| CONTINUE_STATEMENT          | `continue`                     | Keyword to skip to next loop iteration |

## Sample Code

```py
class Animal {
    has name: string;
    has age: int;

    method speak() {
        print("I am an animal.");
    }
}

class Dog inherits Animal {
    has breed: string;

    method speak() {
        print("Woof!");
    }

    method describe() {
        print(self.name);
        print(self.age);
        print(self.breed);
    }
}

method main() {
    create myDog of Dog;
    myDog.name = "Burek";
    myDog.age = 5;
    myDog.breed = "Labrador";

    if myDog.age > 3 {
        myDog.speak();
    } else {
        print("Too young to bark.");
    }

    repeat {
        print(myDog.name);
        myDog.age = myDog.age + 1;
    } until myDog.age > 6;

    return;
}

```
## Grammar
This project uses **ANTLR 4** for lexical and syntactic analysis.

The grammar is defined using two files:

- `OOPsyLexer.g4` – defines tokens (keywords, operators, literals, etc.)
- `OOPsy.g4` – defines parser rules (program structure, statements, expressions)

## TBA
1. Exceptions handling (semantic).
2. GUI
