from antlr4 import *
from grammar.OOPsyLexer import OOPsyLexer
from grammar.OOPsyParser import OOPsyParser
from tree_printer import print_pretty_tree
from interpreter import Interpreter


def main():
    # Wczytaj kod z pliku
    with open("program.oopsy", "rb") as f:
        content = f.read()
        print("Raw bytes:", content)

    with open("program.oopsy", encoding="utf-8") as f:
        print("Text:\n", f.read())
    input_stream = FileStream("program.oopsy", encoding='utf-8')

    # Tokenizacja
    lexer = OOPsyLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Parsowanie
    parser = OOPsyParser(token_stream)

    # Uruchomienie reguły startowej: program
    tree = parser.program()

    # Wypisanie drzewa składniowego (tekstowa reprezentacja)
    print(tree.toStringTree(recog=parser))

    print("🦄 Pretty Printed Parser Parser Tree")
    print_pretty_tree(tree)

    print("Interpreter output:")
    interpreter = Interpreter()
    interpreter.visit(tree)


if __name__ == "__main__":
    main()