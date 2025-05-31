from antlr4 import *
from grammar.OOPsyLexer import OOPsyLexer
from grammar.OOPsyParser import OOPsyParser
from tree_printer import print_pretty_tree
from interpreter import Interpreter
from javaCompiler import JavaCompiler
from semantic_checker import SemanticChecker

def compile_oopsy_to_java(file_path: str, output_path: str):
    input_stream = FileStream(file_path, encoding="utf-8")
    lexer = OOPsyLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = OOPsyParser(token_stream)
    tree = parser.program()

    compiler = JavaCompiler()
    java_code = compiler.compile(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(java_code)
    print(f"Wygenerowano plik: {output_path}")

def main():
    # Wczytaj kod z pliku
    with open("algo.oopsy", "rb") as f:
        content = f.read()
        print("Raw bytes:", content)

    with open("algo.oopsy", encoding="utf-8") as f:
        print("Text:\n", f.read())
    input_stream = FileStream("algo.oopsy", encoding='utf-8')

    # Tokenizacja
    lexer = OOPsyLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Parsowanie
    parser = OOPsyParser(token_stream)

    # Uruchomienie reguły startowej: program
    tree = parser.program()

    try:
        checker = SemanticChecker()
        checker.visit(tree)
    except Exception as e:
        print(e)
        return

    # Wypisanie drzewa składniowego (tekstowa reprezentacja)
    print(tree.toStringTree(recog=parser))

    # print("🦄 Pretty Printed Parser Parser Tree")
    # print_pretty_tree(tree)

    print("Interpreter output:")
    interpreter = Interpreter()
    interpreter.visit(tree)

    compile_oopsy_to_java("algo.oopsy", "AlgoTestJava.java")


if __name__ == "__main__":
    main()