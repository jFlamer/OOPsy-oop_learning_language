# Generated from OOPsy.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
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


    # Enter a parse tree produced by OOPsyParser#mainMethod.
    def enterMainMethod(self, ctx:OOPsyParser.MainMethodContext):
        pass

    # Exit a parse tree produced by OOPsyParser#mainMethod.
    def exitMainMethod(self, ctx:OOPsyParser.MainMethodContext):
        pass


    # Enter a parse tree produced by OOPsyParser#classDecl.
    def enterClassDecl(self, ctx:OOPsyParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by OOPsyParser#classDecl.
    def exitClassDecl(self, ctx:OOPsyParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by OOPsyParser#classElement.
    def enterClassElement(self, ctx:OOPsyParser.ClassElementContext):
        pass

    # Exit a parse tree produced by OOPsyParser#classElement.
    def exitClassElement(self, ctx:OOPsyParser.ClassElementContext):
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


    # Enter a parse tree produced by OOPsyParser#constructorDecl.
    def enterConstructorDecl(self, ctx:OOPsyParser.ConstructorDeclContext):
        pass

    # Exit a parse tree produced by OOPsyParser#constructorDecl.
    def exitConstructorDecl(self, ctx:OOPsyParser.ConstructorDeclContext):
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


    # Enter a parse tree produced by OOPsyParser#createStatement.
    def enterCreateStatement(self, ctx:OOPsyParser.CreateStatementContext):
        pass

    # Exit a parse tree produced by OOPsyParser#createStatement.
    def exitCreateStatement(self, ctx:OOPsyParser.CreateStatementContext):
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


    # Enter a parse tree produced by OOPsyParser#breakStatement.
    def enterBreakStatement(self, ctx:OOPsyParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by OOPsyParser#breakStatement.
    def exitBreakStatement(self, ctx:OOPsyParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by OOPsyParser#continueStatement.
    def enterContinueStatement(self, ctx:OOPsyParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by OOPsyParser#continueStatement.
    def exitContinueStatement(self, ctx:OOPsyParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by OOPsyParser#superCallStatement.
    def enterSuperCallStatement(self, ctx:OOPsyParser.SuperCallStatementContext):
        pass

    # Exit a parse tree produced by OOPsyParser#superCallStatement.
    def exitSuperCallStatement(self, ctx:OOPsyParser.SuperCallStatementContext):
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


    # Enter a parse tree produced by OOPsyParser#typedParam.
    def enterTypedParam(self, ctx:OOPsyParser.TypedParamContext):
        pass

    # Exit a parse tree produced by OOPsyParser#typedParam.
    def exitTypedParam(self, ctx:OOPsyParser.TypedParamContext):
        pass


    # Enter a parse tree produced by OOPsyParser#valueExpression.
    def enterValueExpression(self, ctx:OOPsyParser.ValueExpressionContext):
        pass

    # Exit a parse tree produced by OOPsyParser#valueExpression.
    def exitValueExpression(self, ctx:OOPsyParser.ValueExpressionContext):
        pass


    # Enter a parse tree produced by OOPsyParser#logicalExpression.
    def enterLogicalExpression(self, ctx:OOPsyParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by OOPsyParser#logicalExpression.
    def exitLogicalExpression(self, ctx:OOPsyParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by OOPsyParser#logicalTerm.
    def enterLogicalTerm(self, ctx:OOPsyParser.LogicalTermContext):
        pass

    # Exit a parse tree produced by OOPsyParser#logicalTerm.
    def exitLogicalTerm(self, ctx:OOPsyParser.LogicalTermContext):
        pass


    # Enter a parse tree produced by OOPsyParser#logicalFactor.
    def enterLogicalFactor(self, ctx:OOPsyParser.LogicalFactorContext):
        pass

    # Exit a parse tree produced by OOPsyParser#logicalFactor.
    def exitLogicalFactor(self, ctx:OOPsyParser.LogicalFactorContext):
        pass


    # Enter a parse tree produced by OOPsyParser#anyExpression.
    def enterAnyExpression(self, ctx:OOPsyParser.AnyExpressionContext):
        pass

    # Exit a parse tree produced by OOPsyParser#anyExpression.
    def exitAnyExpression(self, ctx:OOPsyParser.AnyExpressionContext):
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


    # Enter a parse tree produced by OOPsyParser#memberAccess.
    def enterMemberAccess(self, ctx:OOPsyParser.MemberAccessContext):
        pass

    # Exit a parse tree produced by OOPsyParser#memberAccess.
    def exitMemberAccess(self, ctx:OOPsyParser.MemberAccessContext):
        pass


    # Enter a parse tree produced by OOPsyParser#typeName.
    def enterTypeName(self, ctx:OOPsyParser.TypeNameContext):
        pass

    # Exit a parse tree produced by OOPsyParser#typeName.
    def exitTypeName(self, ctx:OOPsyParser.TypeNameContext):
        pass



del OOPsyParser