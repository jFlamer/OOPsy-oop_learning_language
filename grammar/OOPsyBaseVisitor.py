from .OOPsyVisitor import OOPsyVisitor

class OOPsyBaseVisitor(OOPsyVisitor):
    def visitChildren(self, node):
        result = None
        for child in node.getChildren():
            result = child.accept(self)
        return result