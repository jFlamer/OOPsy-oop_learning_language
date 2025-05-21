# Generated from OOPsy.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .OOPsyParser import OOPsyParser
else:
    from OOPsyParser import OOPsyParser

# This class defines a complete generic visitor for a parse tree produced by OOPsyParser.

class OOPsyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OOPsyParser#program.
    def visitProgram(self, ctx:OOPsyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#statement.
    def visitStatement(self, ctx:OOPsyParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#mainMethod.
    def visitMainMethod(self, ctx:OOPsyParser.MainMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#classDecl.
    def visitClassDecl(self, ctx:OOPsyParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#classElement.
    def visitClassElement(self, ctx:OOPsyParser.ClassElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#methodDecl.
    def visitMethodDecl(self, ctx:OOPsyParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#attributeDecl.
    def visitAttributeDecl(self, ctx:OOPsyParser.AttributeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#constructorDecl.
    def visitConstructorDecl(self, ctx:OOPsyParser.ConstructorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#accessModifier.
    def visitAccessModifier(self, ctx:OOPsyParser.AccessModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#assignment.
    def visitAssignment(self, ctx:OOPsyParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#returnStatement.
    def visitReturnStatement(self, ctx:OOPsyParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#expressionStatement.
    def visitExpressionStatement(self, ctx:OOPsyParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#printStatement.
    def visitPrintStatement(self, ctx:OOPsyParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#createStatement.
    def visitCreateStatement(self, ctx:OOPsyParser.CreateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#ifStatement.
    def visitIfStatement(self, ctx:OOPsyParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#loopStatement.
    def visitLoopStatement(self, ctx:OOPsyParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#forStatement.
    def visitForStatement(self, ctx:OOPsyParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#breakStatement.
    def visitBreakStatement(self, ctx:OOPsyParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#continueStatement.
    def visitContinueStatement(self, ctx:OOPsyParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#superCallStatement.
    def visitSuperCallStatement(self, ctx:OOPsyParser.SuperCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#inputStatement.
    def visitInputStatement(self, ctx:OOPsyParser.InputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#commentStatement.
    def visitCommentStatement(self, ctx:OOPsyParser.CommentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#localVarDecl.
    def visitLocalVarDecl(self, ctx:OOPsyParser.LocalVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#block.
    def visitBlock(self, ctx:OOPsyParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#paramList.
    def visitParamList(self, ctx:OOPsyParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#typedParam.
    def visitTypedParam(self, ctx:OOPsyParser.TypedParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#valueExpression.
    def visitValueExpression(self, ctx:OOPsyParser.ValueExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#listLiteral.
    def visitListLiteral(self, ctx:OOPsyParser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#dictLiteral.
    def visitDictLiteral(self, ctx:OOPsyParser.DictLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#dictEntry.
    def visitDictEntry(self, ctx:OOPsyParser.DictEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#logicalExpression.
    def visitLogicalExpression(self, ctx:OOPsyParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#logicalTerm.
    def visitLogicalTerm(self, ctx:OOPsyParser.LogicalTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#logicalFactor.
    def visitLogicalFactor(self, ctx:OOPsyParser.LogicalFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#anyExpression.
    def visitAnyExpression(self, ctx:OOPsyParser.AnyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#methodCall.
    def visitMethodCall(self, ctx:OOPsyParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#inputCall.
    def visitInputCall(self, ctx:OOPsyParser.InputCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#argumentList.
    def visitArgumentList(self, ctx:OOPsyParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#memberAccess.
    def visitMemberAccess(self, ctx:OOPsyParser.MemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OOPsyParser#typeName.
    def visitTypeName(self, ctx:OOPsyParser.TypeNameContext):
        return self.visitChildren(ctx)



del OOPsyParser