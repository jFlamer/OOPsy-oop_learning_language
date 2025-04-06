from anytree import Node, RenderTree
from colorama import Fore, Style, init

# Zainicjuj kolor w terminalu (dla Windows też działa)
init()

def build_tree(ctx, name=None):
    node_name = name if name else type(ctx).__name__.replace("Context", "")
    node = Node(node_name)
    for i in range(ctx.getChildCount()):
        child = ctx.getChild(i)
        if hasattr(child, 'getChildCount') and child.getChildCount() > 0:
            child_node = build_tree(child)
        else:
            child_node = Node(str(child), parent=node)
        child_node.parent = node
    return node

def print_pretty_tree(ctx):
    tree = build_tree(ctx)
    # print(Fore.MAGENTA + "🌸 Pretty printed syntax tree:\n" + Style.RESET_ALL)
    for pre, fill, node in RenderTree(tree):
        print(Fore.LIGHTMAGENTA_EX + f"{pre}{node.name}" + Style.RESET_ALL)