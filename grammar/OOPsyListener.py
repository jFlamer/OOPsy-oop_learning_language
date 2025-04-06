# Generated from OOPsy.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .OOPsyParser import OOPsyParser
else:
    from OOPsyParser import OOPsyParser

# This class defines a complete listener for a parse tree produced by OOPsyParser.
class OOPsyListener(ParseTreeListener):

    # Enter a parse tree produced by OOPsyParser#program.
    def enterProgram(self, ctx:OOPsyParser.ProgramContext):
        pass

    # Exit a parse tree produced by OOPsyParser#program.
    def exitProgram(self, ctx:OOPsyParser.ProgramContext):
        pass


    # Enter a parse tree produced by OOPsyParser#statement.
    def enterStatement(self, ctx:OOPsyParser.StatementContext):
        pass

    # Exit a parse tree produced by OOPsyParser#statement.
    def exitStatement(self, ctx:OOPsyParser.StatementContext):
        pass


    # Enter a parse tree produced by OOPsyParser#classDecl.
    def enterClassDecl(self, ctx:OOPsyParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by OOPsyParser#classDecl.
    def exitClassDecl(self, ctx:OOPsyParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by OOPsyParser#methodDecl.
    def enterMethodDecl(self, ctx:OOPsyParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by OOPsyParser#methodDecl.
    def exitMethodDecl(self, ctx:OOPsyParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by OOPsyParser#attributeDecl.
    def enterAttributeDecl(self, ctx:OOPsyParser.AttributeDeclContext):
        pass

    # Exit a parse tree produced by OOPsyParser#attributeDecl.
    def exitAttributeDecl(self, ctx:OOPsyParser.AttributeDeclContext):
        pass


    # Enter a parse tree produced by OOPsyParser#assignment.
    def enterAssignment(self, ctx:OOPsyParser.AssignmentContext):
        pass

    # Exit a parse tree produced by OOPsyParser#assignment.
    def exitAssignment(self, ctx:OOPsyParser.AssignmentContext):
        pass


    # Enter a parse tree produced by OOPsyParser#returnStatement.
    def enterReturnStatement(self, ctx:OOPsyParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by OOPsyParser#returnStatement.
    def exitReturnStatement(self, ctx:OOPsyParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by OOPsyParser#expressionStatement.
    def enterExpressionStatement(self, ctx:OOPsyParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by OOPsyParser#expressionStatement.
    def exitExpressionStatement(self, ctx:OOPsyParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by OOPsyParser#printStatement.
    def enterPrintStatement(self, ctx:OOPsyParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by OOPsyParser#printStatement.
    def exitPrintStatement(self, ctx:OOPsyParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by OOPsyParser#ifStatement.
    def enterIfStatement(self, ctx:OOPsyParser.IfStatementContext):
        pass

    # Exit a parse tree produced by OOPsyParser#ifStatement.
    def exitIfStatement(self, ctx:OOPsyParser.IfStatementContext):
        pass


    # Enter a parse tree produced by OOPsyParser#loopStatement.
    def enterLoopStatement(self, ctx:OOPsyParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by OOPsyParser#loopStatement.
    def exitLoopStatement(self, ctx:OOPsyParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by OOPsyParser#block.
    def enterBlock(self, ctx:OOPsyParser.BlockContext):
        pass

    # Exit a parse tree produced by OOPsyParser#block.
    def exitBlock(self, ctx:OOPsyParser.BlockContext):
        pass


    # Enter a parse tree produced by OOPsyParser#paramList.
    def enterParamList(self, ctx:OOPsyParser.ParamListContext):
        pass

    # Exit a parse tree produced by OOPsyParser#paramList.
    def exitParamList(self, ctx:OOPsyParser.ParamListContext):
        pass


    # Enter a parse tree produced by OOPsyParser#expression.
    def enterExpression(self, ctx:OOPsyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by OOPsyParser#expression.
    def exitExpression(self, ctx:OOPsyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by OOPsyParser#methodCall.
    def enterMethodCall(self, ctx:OOPsyParser.MethodCallContext):
        pass

    # Exit a parse tree produced by OOPsyParser#methodCall.
    def exitMethodCall(self, ctx:OOPsyParser.MethodCallContext):
        pass


    # Enter a parse tree produced by OOPsyParser#argumentList.
    def enterArgumentList(self, ctx:OOPsyParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by OOPsyParser#argumentList.
    def exitArgumentList(self, ctx:OOPsyParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by OOPsyParser#typeName.
    def enterTypeName(self, ctx:OOPsyParser.TypeNameContext):
        pass

    # Exit a parse tree produced by OOPsyParser#typeName.
    def exitTypeName(self, ctx:OOPsyParser.TypeNameContext):
        pass



del OOPsyParser