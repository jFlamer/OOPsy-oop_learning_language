# Generated from OOPsy.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,72,226,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,63,8,1,1,2,1,2,1,2,1,2,3,2,69,
        8,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,78,8,3,1,3,1,3,5,3,82,8,3,10,
        3,12,3,85,9,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,93,8,4,1,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,6,1,6,3,6,106,8,6,1,6,1,6,1,6,1,6,1,7,1,7,
        3,7,114,8,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,138,8,11,1,12,
        1,12,1,12,1,12,1,12,1,12,1,13,1,13,5,13,148,8,13,10,13,12,13,151,
        9,13,1,13,1,13,1,14,1,14,1,14,5,14,158,8,14,10,14,12,14,161,9,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,3,15,177,8,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,185,8,15,10,
        15,12,15,188,9,15,1,16,1,16,1,16,3,16,193,8,16,1,17,1,17,1,17,1,
        17,1,17,1,17,3,17,201,8,17,1,18,1,18,1,18,1,18,1,18,3,18,208,8,18,
        1,18,1,18,1,19,1,19,1,19,5,19,215,8,19,10,19,12,19,218,9,19,1,20,
        1,20,1,20,1,20,1,21,1,21,1,21,0,1,30,22,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,0,5,1,0,14,16,1,0,12,13,1,0,
        24,29,2,0,60,60,72,72,2,0,1,5,72,72,236,0,47,1,0,0,0,2,62,1,0,0,
        0,4,64,1,0,0,0,6,73,1,0,0,0,8,88,1,0,0,0,10,97,1,0,0,0,12,105,1,
        0,0,0,14,111,1,0,0,0,16,117,1,0,0,0,18,120,1,0,0,0,20,126,1,0,0,
        0,22,132,1,0,0,0,24,139,1,0,0,0,26,145,1,0,0,0,28,154,1,0,0,0,30,
        176,1,0,0,0,32,189,1,0,0,0,34,200,1,0,0,0,36,202,1,0,0,0,38,211,
        1,0,0,0,40,219,1,0,0,0,42,223,1,0,0,0,44,46,3,6,3,0,45,44,1,0,0,
        0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,
        1,0,0,0,50,51,3,4,2,0,51,52,5,0,0,1,52,1,1,0,0,0,53,63,3,8,4,0,54,
        63,3,10,5,0,55,63,3,12,6,0,56,63,3,22,11,0,57,63,3,24,12,0,58,63,
        3,14,7,0,59,63,3,18,9,0,60,63,3,16,8,0,61,63,3,20,10,0,62,53,1,0,
        0,0,62,54,1,0,0,0,62,55,1,0,0,0,62,56,1,0,0,0,62,57,1,0,0,0,62,58,
        1,0,0,0,62,59,1,0,0,0,62,60,1,0,0,0,62,61,1,0,0,0,63,3,1,0,0,0,64,
        65,5,49,0,0,65,66,5,46,0,0,66,68,5,34,0,0,67,69,3,28,14,0,68,67,
        1,0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,71,5,35,0,0,71,72,3,26,13,
        0,72,5,1,0,0,0,73,74,5,45,0,0,74,77,5,72,0,0,75,76,5,47,0,0,76,78,
        5,72,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,79,1,0,0,0,79,83,5,36,0,
        0,80,82,3,2,1,0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,
        1,0,0,0,84,86,1,0,0,0,85,83,1,0,0,0,86,87,5,37,0,0,87,7,1,0,0,0,
        88,89,5,49,0,0,89,90,5,72,0,0,90,92,5,34,0,0,91,93,3,28,14,0,92,
        91,1,0,0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,95,5,35,0,0,95,96,3,26,
        13,0,96,9,1,0,0,0,97,98,5,48,0,0,98,99,5,72,0,0,99,100,5,40,0,0,
        100,101,3,42,21,0,101,102,5,41,0,0,102,11,1,0,0,0,103,106,5,72,0,
        0,104,106,3,40,20,0,105,103,1,0,0,0,105,104,1,0,0,0,106,107,1,0,
        0,0,107,108,5,19,0,0,108,109,3,30,15,0,109,110,5,41,0,0,110,13,1,
        0,0,0,111,113,5,69,0,0,112,114,3,30,15,0,113,112,1,0,0,0,113,114,
        1,0,0,0,114,115,1,0,0,0,115,116,5,41,0,0,116,15,1,0,0,0,117,118,
        3,34,17,0,118,119,5,41,0,0,119,17,1,0,0,0,120,121,5,54,0,0,121,122,
        5,34,0,0,122,123,3,30,15,0,123,124,5,35,0,0,124,125,5,41,0,0,125,
        19,1,0,0,0,126,127,5,52,0,0,127,128,5,72,0,0,128,129,5,53,0,0,129,
        130,5,72,0,0,130,131,5,41,0,0,131,21,1,0,0,0,132,133,5,55,0,0,133,
        134,3,32,16,0,134,137,3,26,13,0,135,136,5,56,0,0,136,138,3,26,13,
        0,137,135,1,0,0,0,137,138,1,0,0,0,138,23,1,0,0,0,139,140,5,57,0,
        0,140,141,3,26,13,0,141,142,5,58,0,0,142,143,3,32,16,0,143,144,5,
        41,0,0,144,25,1,0,0,0,145,149,5,36,0,0,146,148,3,2,1,0,147,146,1,
        0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,152,1,
        0,0,0,151,149,1,0,0,0,152,153,5,37,0,0,153,27,1,0,0,0,154,159,5,
        72,0,0,155,156,5,39,0,0,156,158,5,72,0,0,157,155,1,0,0,0,158,161,
        1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,29,1,0,0,0,161,159,1,
        0,0,0,162,163,6,15,-1,0,163,177,5,72,0,0,164,177,5,8,0,0,165,177,
        5,9,0,0,166,177,5,11,0,0,167,177,5,10,0,0,168,177,5,6,0,0,169,177,
        5,7,0,0,170,177,3,36,18,0,171,177,3,40,20,0,172,173,5,34,0,0,173,
        174,3,30,15,0,174,175,5,35,0,0,175,177,1,0,0,0,176,162,1,0,0,0,176,
        164,1,0,0,0,176,165,1,0,0,0,176,166,1,0,0,0,176,167,1,0,0,0,176,
        168,1,0,0,0,176,169,1,0,0,0,176,170,1,0,0,0,176,171,1,0,0,0,176,
        172,1,0,0,0,177,186,1,0,0,0,178,179,10,12,0,0,179,180,7,0,0,0,180,
        185,3,30,15,13,181,182,10,11,0,0,182,183,7,1,0,0,183,185,3,30,15,
        12,184,178,1,0,0,0,184,181,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,
        0,186,187,1,0,0,0,187,31,1,0,0,0,188,186,1,0,0,0,189,192,3,30,15,
        0,190,191,7,2,0,0,191,193,3,30,15,0,192,190,1,0,0,0,192,193,1,0,
        0,0,193,33,1,0,0,0,194,201,3,30,15,0,195,196,5,54,0,0,196,197,5,
        34,0,0,197,198,3,30,15,0,198,199,5,35,0,0,199,201,1,0,0,0,200,194,
        1,0,0,0,200,195,1,0,0,0,201,35,1,0,0,0,202,203,5,72,0,0,203,204,
        5,38,0,0,204,205,5,72,0,0,205,207,5,34,0,0,206,208,3,38,19,0,207,
        206,1,0,0,0,207,208,1,0,0,0,208,209,1,0,0,0,209,210,5,35,0,0,210,
        37,1,0,0,0,211,216,3,30,15,0,212,213,5,39,0,0,213,215,3,30,15,0,
        214,212,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,
        217,39,1,0,0,0,218,216,1,0,0,0,219,220,7,3,0,0,220,221,5,38,0,0,
        221,222,5,72,0,0,222,41,1,0,0,0,223,224,7,4,0,0,224,43,1,0,0,0,18,
        47,62,68,77,83,92,105,113,137,149,159,176,184,186,192,200,207,216
    ]

class OOPsyParser ( Parser ):

    grammarFileName = "OOPsy.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'string'", "'char'", 
                     "'bool'", "'true'", "'false'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'++'", "'--'", "'='", "'+='", "'-='", "'*='", 
                     "'/='", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", 
                     "'&&'", "'||'", "'['", "']'", "'('", "')'", "'{'", 
                     "'}'", "'.'", "','", "':'", "';'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'class'", "'main'", "'inherits'", "'has'", 
                     "'method'", "'constructor'", "'end'", "'create'", "'of'", 
                     "'print'", "'if'", "'else'", "'repeat'", "'until'", 
                     "'input'", "'self'", "'abstract'", "'final'", "'override'", 
                     "'super'", "'public'", "'private'", "'list'", "'dict'", 
                     "'return'", "'break'", "'continue'" ]

    symbolicNames = [ "<INVALID>", "OOPSY_TYPE_INT", "OOPSY_TYPE_FLOAT", 
                      "OOPSY_TYPE_STRING", "OOPSY_TYPE_CHAR", "OOPSY_TYPE_BOOL", 
                      "BOOL_LITERAL_TRUE", "BOOL_LITERAL_FALSE", "INT_LITERAL", 
                      "FLOAT_LITERAL", "CHAR_LITERAL", "STRING_LITERAL", 
                      "PLUS_OPERATOR", "MINUS_OPERATOR", "MULTIPLY_OPERATOR", 
                      "DIVIDE_OPERATOR", "MODULO_OPERATOR", "INCREMENT_OPERATOR", 
                      "DECREMENT_OPERATOR", "ASSIGNMENT_OPERATOR", "ADDITION_ASSIGNMENT_OPERATOR", 
                      "SUBTRACTION_ASSIGNMENT_OPERATOR", "MULTIPLICATION_ASSIGNMENT_OPERATOR", 
                      "DIVISION_ASSIGNMENT_OPERATOR", "EQUAL_OPERATOR", 
                      "UNEQUAL_OPERATOR", "GREATER_OPERATOR", "LESSER_OPERATOR", 
                      "GREATER_EQ_OPERATOR", "LESSER_EQ_OPERATOR", "AND_OPERATOR", 
                      "OR_OPERATOR", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_PARENTHESIS", 
                      "RIGHT_PARENTHESIS", "LEFT_BRACE", "RIGHT_BRACE", 
                      "DOT_SEPARATOR", "COMMA_SEPARATOR", "COLON_SEPARATOR", 
                      "SEMICOLON_SEPARATOR", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "WHITESPACE", "CLASS_KEYWORD", "MAIN_KEYWORD", "INHERITS_KEYWORD", 
                      "HAS_ATTRIBUTE_KEYWORD", "METHOD_KEYWORD", "CONSTRUCTOR_KEYWORD", 
                      "END_STATEMENT", "CREATE_KEYWORD", "OF_STATEMENT", 
                      "PRINT_KEYWORD", "IF_KEYWORD", "ELSE_KEYWORD", "REPEAT_KEYWORD", 
                      "UNTIL_KEYWORD", "INPUT_STATEMENT", "SELF_KEYWORD", 
                      "ABSTRACT_CLASS", "FINAL_CLASS", "OVERRIDE_METHOD", 
                      "SUPER_CALL", "PUBLIC_MODIFIER", "PRIVATE_MODIFIER", 
                      "LIST_TYPE", "DICTIONARY_TYPE", "RETURN_STATEMENT", 
                      "BREAK_STATEMENT", "CONTINUE_STATEMENT", "IDENTIFIER" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_mainMethod = 2
    RULE_classDecl = 3
    RULE_methodDecl = 4
    RULE_attributeDecl = 5
    RULE_assignment = 6
    RULE_returnStatement = 7
    RULE_expressionStatement = 8
    RULE_printStatement = 9
    RULE_createStatement = 10
    RULE_ifStatement = 11
    RULE_loopStatement = 12
    RULE_block = 13
    RULE_paramList = 14
    RULE_valueExpression = 15
    RULE_logicalExpression = 16
    RULE_anyExpression = 17
    RULE_methodCall = 18
    RULE_argumentList = 19
    RULE_memberAccess = 20
    RULE_typeName = 21

    ruleNames =  [ "program", "statement", "mainMethod", "classDecl", "methodDecl", 
                   "attributeDecl", "assignment", "returnStatement", "expressionStatement", 
                   "printStatement", "createStatement", "ifStatement", "loopStatement", 
                   "block", "paramList", "valueExpression", "logicalExpression", 
                   "anyExpression", "methodCall", "argumentList", "memberAccess", 
                   "typeName" ]

    EOF = Token.EOF
    OOPSY_TYPE_INT=1
    OOPSY_TYPE_FLOAT=2
    OOPSY_TYPE_STRING=3
    OOPSY_TYPE_CHAR=4
    OOPSY_TYPE_BOOL=5
    BOOL_LITERAL_TRUE=6
    BOOL_LITERAL_FALSE=7
    INT_LITERAL=8
    FLOAT_LITERAL=9
    CHAR_LITERAL=10
    STRING_LITERAL=11
    PLUS_OPERATOR=12
    MINUS_OPERATOR=13
    MULTIPLY_OPERATOR=14
    DIVIDE_OPERATOR=15
    MODULO_OPERATOR=16
    INCREMENT_OPERATOR=17
    DECREMENT_OPERATOR=18
    ASSIGNMENT_OPERATOR=19
    ADDITION_ASSIGNMENT_OPERATOR=20
    SUBTRACTION_ASSIGNMENT_OPERATOR=21
    MULTIPLICATION_ASSIGNMENT_OPERATOR=22
    DIVISION_ASSIGNMENT_OPERATOR=23
    EQUAL_OPERATOR=24
    UNEQUAL_OPERATOR=25
    GREATER_OPERATOR=26
    LESSER_OPERATOR=27
    GREATER_EQ_OPERATOR=28
    LESSER_EQ_OPERATOR=29
    AND_OPERATOR=30
    OR_OPERATOR=31
    LEFT_BRACKET=32
    RIGHT_BRACKET=33
    LEFT_PARENTHESIS=34
    RIGHT_PARENTHESIS=35
    LEFT_BRACE=36
    RIGHT_BRACE=37
    DOT_SEPARATOR=38
    COMMA_SEPARATOR=39
    COLON_SEPARATOR=40
    SEMICOLON_SEPARATOR=41
    LINE_COMMENT=42
    BLOCK_COMMENT=43
    WHITESPACE=44
    CLASS_KEYWORD=45
    MAIN_KEYWORD=46
    INHERITS_KEYWORD=47
    HAS_ATTRIBUTE_KEYWORD=48
    METHOD_KEYWORD=49
    CONSTRUCTOR_KEYWORD=50
    END_STATEMENT=51
    CREATE_KEYWORD=52
    OF_STATEMENT=53
    PRINT_KEYWORD=54
    IF_KEYWORD=55
    ELSE_KEYWORD=56
    REPEAT_KEYWORD=57
    UNTIL_KEYWORD=58
    INPUT_STATEMENT=59
    SELF_KEYWORD=60
    ABSTRACT_CLASS=61
    FINAL_CLASS=62
    OVERRIDE_METHOD=63
    SUPER_CALL=64
    PUBLIC_MODIFIER=65
    PRIVATE_MODIFIER=66
    LIST_TYPE=67
    DICTIONARY_TYPE=68
    RETURN_STATEMENT=69
    BREAK_STATEMENT=70
    CONTINUE_STATEMENT=71
    IDENTIFIER=72

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mainMethod(self):
            return self.getTypedRuleContext(OOPsyParser.MainMethodContext,0)


        def EOF(self):
            return self.getToken(OOPsyParser.EOF, 0)

        def classDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OOPsyParser.ClassDeclContext)
            else:
                return self.getTypedRuleContext(OOPsyParser.ClassDeclContext,i)


        def getRuleIndex(self):
            return OOPsyParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = OOPsyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 44
                self.classDecl()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.mainMethod()
            self.state = 51
            self.match(OOPsyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodDecl(self):
            return self.getTypedRuleContext(OOPsyParser.MethodDeclContext,0)


        def attributeDecl(self):
            return self.getTypedRuleContext(OOPsyParser.AttributeDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(OOPsyParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(OOPsyParser.IfStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(OOPsyParser.LoopStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(OOPsyParser.ReturnStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(OOPsyParser.PrintStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(OOPsyParser.ExpressionStatementContext,0)


        def createStatement(self):
            return self.getTypedRuleContext(OOPsyParser.CreateStatementContext,0)


        def getRuleIndex(self):
            return OOPsyParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = OOPsyParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.methodDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.attributeDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 57
                self.loopStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 58
                self.returnStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 59
                self.printStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 60
                self.expressionStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 61
                self.createStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainMethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METHOD_KEYWORD(self):
            return self.getToken(OOPsyParser.METHOD_KEYWORD, 0)

        def MAIN_KEYWORD(self):
            return self.getToken(OOPsyParser.MAIN_KEYWORD, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.RIGHT_PARENTHESIS, 0)

        def block(self):
            return self.getTypedRuleContext(OOPsyParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(OOPsyParser.ParamListContext,0)


        def getRuleIndex(self):
            return OOPsyParser.RULE_mainMethod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainMethod" ):
                listener.enterMainMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainMethod" ):
                listener.exitMainMethod(self)




    def mainMethod(self):

        localctx = OOPsyParser.MainMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mainMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(OOPsyParser.METHOD_KEYWORD)
            self.state = 65
            self.match(OOPsyParser.MAIN_KEYWORD)
            self.state = 66
            self.match(OOPsyParser.LEFT_PARENTHESIS)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==72:
                self.state = 67
                self.paramList()


            self.state = 70
            self.match(OOPsyParser.RIGHT_PARENTHESIS)
            self.state = 71
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS_KEYWORD(self):
            return self.getToken(OOPsyParser.CLASS_KEYWORD, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OOPsyParser.IDENTIFIER)
            else:
                return self.getToken(OOPsyParser.IDENTIFIER, i)

        def LEFT_BRACE(self):
            return self.getToken(OOPsyParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(OOPsyParser.RIGHT_BRACE, 0)

        def INHERITS_KEYWORD(self):
            return self.getToken(OOPsyParser.INHERITS_KEYWORD, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OOPsyParser.StatementContext)
            else:
                return self.getTypedRuleContext(OOPsyParser.StatementContext,i)


        def getRuleIndex(self):
            return OOPsyParser.RULE_classDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDecl" ):
                listener.enterClassDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDecl" ):
                listener.exitClassDecl(self)




    def classDecl(self):

        localctx = OOPsyParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(OOPsyParser.CLASS_KEYWORD)
            self.state = 74
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 75
                self.match(OOPsyParser.INHERITS_KEYWORD)
                self.state = 76
                self.match(OOPsyParser.IDENTIFIER)


            self.state = 79
            self.match(OOPsyParser.LEFT_BRACE)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1356427929948524480) != 0) or _la==69 or _la==72:
                self.state = 80
                self.statement()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(OOPsyParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METHOD_KEYWORD(self):
            return self.getToken(OOPsyParser.METHOD_KEYWORD, 0)

        def IDENTIFIER(self):
            return self.getToken(OOPsyParser.IDENTIFIER, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.RIGHT_PARENTHESIS, 0)

        def block(self):
            return self.getTypedRuleContext(OOPsyParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(OOPsyParser.ParamListContext,0)


        def getRuleIndex(self):
            return OOPsyParser.RULE_methodDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDecl" ):
                listener.enterMethodDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDecl" ):
                listener.exitMethodDecl(self)




    def methodDecl(self):

        localctx = OOPsyParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(OOPsyParser.METHOD_KEYWORD)
            self.state = 89
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 90
            self.match(OOPsyParser.LEFT_PARENTHESIS)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==72:
                self.state = 91
                self.paramList()


            self.state = 94
            self.match(OOPsyParser.RIGHT_PARENTHESIS)
            self.state = 95
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HAS_ATTRIBUTE_KEYWORD(self):
            return self.getToken(OOPsyParser.HAS_ATTRIBUTE_KEYWORD, 0)

        def IDENTIFIER(self):
            return self.getToken(OOPsyParser.IDENTIFIER, 0)

        def COLON_SEPARATOR(self):
            return self.getToken(OOPsyParser.COLON_SEPARATOR, 0)

        def typeName(self):
            return self.getTypedRuleContext(OOPsyParser.TypeNameContext,0)


        def SEMICOLON_SEPARATOR(self):
            return self.getToken(OOPsyParser.SEMICOLON_SEPARATOR, 0)

        def getRuleIndex(self):
            return OOPsyParser.RULE_attributeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeDecl" ):
                listener.enterAttributeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeDecl" ):
                listener.exitAttributeDecl(self)




    def attributeDecl(self):

        localctx = OOPsyParser.AttributeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attributeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(OOPsyParser.HAS_ATTRIBUTE_KEYWORD)
            self.state = 98
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 99
            self.match(OOPsyParser.COLON_SEPARATOR)
            self.state = 100
            self.typeName()
            self.state = 101
            self.match(OOPsyParser.SEMICOLON_SEPARATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNMENT_OPERATOR(self):
            return self.getToken(OOPsyParser.ASSIGNMENT_OPERATOR, 0)

        def valueExpression(self):
            return self.getTypedRuleContext(OOPsyParser.ValueExpressionContext,0)


        def SEMICOLON_SEPARATOR(self):
            return self.getToken(OOPsyParser.SEMICOLON_SEPARATOR, 0)

        def IDENTIFIER(self):
            return self.getToken(OOPsyParser.IDENTIFIER, 0)

        def memberAccess(self):
            return self.getTypedRuleContext(OOPsyParser.MemberAccessContext,0)


        def getRuleIndex(self):
            return OOPsyParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = OOPsyParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 103
                self.match(OOPsyParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 104
                self.memberAccess()
                pass


            self.state = 107
            self.match(OOPsyParser.ASSIGNMENT_OPERATOR)
            self.state = 108
            self.valueExpression(0)
            self.state = 109
            self.match(OOPsyParser.SEMICOLON_SEPARATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_STATEMENT(self):
            return self.getToken(OOPsyParser.RETURN_STATEMENT, 0)

        def SEMICOLON_SEPARATOR(self):
            return self.getToken(OOPsyParser.SEMICOLON_SEPARATOR, 0)

        def valueExpression(self):
            return self.getTypedRuleContext(OOPsyParser.ValueExpressionContext,0)


        def getRuleIndex(self):
            return OOPsyParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = OOPsyParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(OOPsyParser.RETURN_STATEMENT)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1152921521786720192) != 0) or _la==72:
                self.state = 112
                self.valueExpression(0)


            self.state = 115
            self.match(OOPsyParser.SEMICOLON_SEPARATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def anyExpression(self):
            return self.getTypedRuleContext(OOPsyParser.AnyExpressionContext,0)


        def SEMICOLON_SEPARATOR(self):
            return self.getToken(OOPsyParser.SEMICOLON_SEPARATOR, 0)

        def getRuleIndex(self):
            return OOPsyParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)




    def expressionStatement(self):

        localctx = OOPsyParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.anyExpression()
            self.state = 118
            self.match(OOPsyParser.SEMICOLON_SEPARATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT_KEYWORD(self):
            return self.getToken(OOPsyParser.PRINT_KEYWORD, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.LEFT_PARENTHESIS, 0)

        def valueExpression(self):
            return self.getTypedRuleContext(OOPsyParser.ValueExpressionContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.RIGHT_PARENTHESIS, 0)

        def SEMICOLON_SEPARATOR(self):
            return self.getToken(OOPsyParser.SEMICOLON_SEPARATOR, 0)

        def getRuleIndex(self):
            return OOPsyParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)




    def printStatement(self):

        localctx = OOPsyParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(OOPsyParser.PRINT_KEYWORD)
            self.state = 121
            self.match(OOPsyParser.LEFT_PARENTHESIS)
            self.state = 122
            self.valueExpression(0)
            self.state = 123
            self.match(OOPsyParser.RIGHT_PARENTHESIS)
            self.state = 124
            self.match(OOPsyParser.SEMICOLON_SEPARATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE_KEYWORD(self):
            return self.getToken(OOPsyParser.CREATE_KEYWORD, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OOPsyParser.IDENTIFIER)
            else:
                return self.getToken(OOPsyParser.IDENTIFIER, i)

        def OF_STATEMENT(self):
            return self.getToken(OOPsyParser.OF_STATEMENT, 0)

        def SEMICOLON_SEPARATOR(self):
            return self.getToken(OOPsyParser.SEMICOLON_SEPARATOR, 0)

        def getRuleIndex(self):
            return OOPsyParser.RULE_createStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateStatement" ):
                listener.enterCreateStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateStatement" ):
                listener.exitCreateStatement(self)




    def createStatement(self):

        localctx = OOPsyParser.CreateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_createStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(OOPsyParser.CREATE_KEYWORD)
            self.state = 127
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 128
            self.match(OOPsyParser.OF_STATEMENT)
            self.state = 129
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 130
            self.match(OOPsyParser.SEMICOLON_SEPARATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_KEYWORD(self):
            return self.getToken(OOPsyParser.IF_KEYWORD, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(OOPsyParser.LogicalExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OOPsyParser.BlockContext)
            else:
                return self.getTypedRuleContext(OOPsyParser.BlockContext,i)


        def ELSE_KEYWORD(self):
            return self.getToken(OOPsyParser.ELSE_KEYWORD, 0)

        def getRuleIndex(self):
            return OOPsyParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = OOPsyParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(OOPsyParser.IF_KEYWORD)
            self.state = 133
            self.logicalExpression()
            self.state = 134
            self.block()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 135
                self.match(OOPsyParser.ELSE_KEYWORD)
                self.state = 136
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT_KEYWORD(self):
            return self.getToken(OOPsyParser.REPEAT_KEYWORD, 0)

        def block(self):
            return self.getTypedRuleContext(OOPsyParser.BlockContext,0)


        def UNTIL_KEYWORD(self):
            return self.getToken(OOPsyParser.UNTIL_KEYWORD, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(OOPsyParser.LogicalExpressionContext,0)


        def SEMICOLON_SEPARATOR(self):
            return self.getToken(OOPsyParser.SEMICOLON_SEPARATOR, 0)

        def getRuleIndex(self):
            return OOPsyParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)




    def loopStatement(self):

        localctx = OOPsyParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(OOPsyParser.REPEAT_KEYWORD)
            self.state = 140
            self.block()
            self.state = 141
            self.match(OOPsyParser.UNTIL_KEYWORD)
            self.state = 142
            self.logicalExpression()
            self.state = 143
            self.match(OOPsyParser.SEMICOLON_SEPARATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(OOPsyParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(OOPsyParser.RIGHT_BRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OOPsyParser.StatementContext)
            else:
                return self.getTypedRuleContext(OOPsyParser.StatementContext,i)


        def getRuleIndex(self):
            return OOPsyParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = OOPsyParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(OOPsyParser.LEFT_BRACE)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1356427929948524480) != 0) or _la==69 or _la==72:
                self.state = 146
                self.statement()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self.match(OOPsyParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OOPsyParser.IDENTIFIER)
            else:
                return self.getToken(OOPsyParser.IDENTIFIER, i)

        def COMMA_SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(OOPsyParser.COMMA_SEPARATOR)
            else:
                return self.getToken(OOPsyParser.COMMA_SEPARATOR, i)

        def getRuleIndex(self):
            return OOPsyParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)




    def paramList(self):

        localctx = OOPsyParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 155
                self.match(OOPsyParser.COMMA_SEPARATOR)
                self.state = 156
                self.match(OOPsyParser.IDENTIFIER)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OOPsyParser.IDENTIFIER, 0)

        def INT_LITERAL(self):
            return self.getToken(OOPsyParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(OOPsyParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(OOPsyParser.STRING_LITERAL, 0)

        def CHAR_LITERAL(self):
            return self.getToken(OOPsyParser.CHAR_LITERAL, 0)

        def BOOL_LITERAL_TRUE(self):
            return self.getToken(OOPsyParser.BOOL_LITERAL_TRUE, 0)

        def BOOL_LITERAL_FALSE(self):
            return self.getToken(OOPsyParser.BOOL_LITERAL_FALSE, 0)

        def methodCall(self):
            return self.getTypedRuleContext(OOPsyParser.MethodCallContext,0)


        def memberAccess(self):
            return self.getTypedRuleContext(OOPsyParser.MemberAccessContext,0)


        def LEFT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.LEFT_PARENTHESIS, 0)

        def valueExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OOPsyParser.ValueExpressionContext)
            else:
                return self.getTypedRuleContext(OOPsyParser.ValueExpressionContext,i)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.RIGHT_PARENTHESIS, 0)

        def MULTIPLY_OPERATOR(self):
            return self.getToken(OOPsyParser.MULTIPLY_OPERATOR, 0)

        def DIVIDE_OPERATOR(self):
            return self.getToken(OOPsyParser.DIVIDE_OPERATOR, 0)

        def MODULO_OPERATOR(self):
            return self.getToken(OOPsyParser.MODULO_OPERATOR, 0)

        def PLUS_OPERATOR(self):
            return self.getToken(OOPsyParser.PLUS_OPERATOR, 0)

        def MINUS_OPERATOR(self):
            return self.getToken(OOPsyParser.MINUS_OPERATOR, 0)

        def getRuleIndex(self):
            return OOPsyParser.RULE_valueExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueExpression" ):
                listener.enterValueExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueExpression" ):
                listener.exitValueExpression(self)



    def valueExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OOPsyParser.ValueExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_valueExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 163
                self.match(OOPsyParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 164
                self.match(OOPsyParser.INT_LITERAL)
                pass

            elif la_ == 3:
                self.state = 165
                self.match(OOPsyParser.FLOAT_LITERAL)
                pass

            elif la_ == 4:
                self.state = 166
                self.match(OOPsyParser.STRING_LITERAL)
                pass

            elif la_ == 5:
                self.state = 167
                self.match(OOPsyParser.CHAR_LITERAL)
                pass

            elif la_ == 6:
                self.state = 168
                self.match(OOPsyParser.BOOL_LITERAL_TRUE)
                pass

            elif la_ == 7:
                self.state = 169
                self.match(OOPsyParser.BOOL_LITERAL_FALSE)
                pass

            elif la_ == 8:
                self.state = 170
                self.methodCall()
                pass

            elif la_ == 9:
                self.state = 171
                self.memberAccess()
                pass

            elif la_ == 10:
                self.state = 172
                self.match(OOPsyParser.LEFT_PARENTHESIS)
                self.state = 173
                self.valueExpression(0)
                self.state = 174
                self.match(OOPsyParser.RIGHT_PARENTHESIS)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 184
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = OOPsyParser.ValueExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_valueExpression)
                        self.state = 178
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 179
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 180
                        self.valueExpression(13)
                        pass

                    elif la_ == 2:
                        localctx = OOPsyParser.ValueExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_valueExpression)
                        self.state = 181
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 182
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 183
                        self.valueExpression(12)
                        pass

             
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valueExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OOPsyParser.ValueExpressionContext)
            else:
                return self.getTypedRuleContext(OOPsyParser.ValueExpressionContext,i)


        def EQUAL_OPERATOR(self):
            return self.getToken(OOPsyParser.EQUAL_OPERATOR, 0)

        def UNEQUAL_OPERATOR(self):
            return self.getToken(OOPsyParser.UNEQUAL_OPERATOR, 0)

        def LESSER_OPERATOR(self):
            return self.getToken(OOPsyParser.LESSER_OPERATOR, 0)

        def GREATER_OPERATOR(self):
            return self.getToken(OOPsyParser.GREATER_OPERATOR, 0)

        def LESSER_EQ_OPERATOR(self):
            return self.getToken(OOPsyParser.LESSER_EQ_OPERATOR, 0)

        def GREATER_EQ_OPERATOR(self):
            return self.getToken(OOPsyParser.GREATER_EQ_OPERATOR, 0)

        def getRuleIndex(self):
            return OOPsyParser.RULE_logicalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpression" ):
                listener.enterLogicalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpression" ):
                listener.exitLogicalExpression(self)




    def logicalExpression(self):

        localctx = OOPsyParser.LogicalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_logicalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.valueExpression(0)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0):
                self.state = 190
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 191
                self.valueExpression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnyExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valueExpression(self):
            return self.getTypedRuleContext(OOPsyParser.ValueExpressionContext,0)


        def PRINT_KEYWORD(self):
            return self.getToken(OOPsyParser.PRINT_KEYWORD, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.RIGHT_PARENTHESIS, 0)

        def getRuleIndex(self):
            return OOPsyParser.RULE_anyExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnyExpression" ):
                listener.enterAnyExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnyExpression" ):
                listener.exitAnyExpression(self)




    def anyExpression(self):

        localctx = OOPsyParser.AnyExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_anyExpression)
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 8, 9, 10, 11, 34, 60, 72]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.valueExpression(0)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.match(OOPsyParser.PRINT_KEYWORD)
                self.state = 196
                self.match(OOPsyParser.LEFT_PARENTHESIS)
                self.state = 197
                self.valueExpression(0)
                self.state = 198
                self.match(OOPsyParser.RIGHT_PARENTHESIS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OOPsyParser.IDENTIFIER)
            else:
                return self.getToken(OOPsyParser.IDENTIFIER, i)

        def DOT_SEPARATOR(self):
            return self.getToken(OOPsyParser.DOT_SEPARATOR, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.RIGHT_PARENTHESIS, 0)

        def argumentList(self):
            return self.getTypedRuleContext(OOPsyParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return OOPsyParser.RULE_methodCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCall" ):
                listener.enterMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCall" ):
                listener.exitMethodCall(self)




    def methodCall(self):

        localctx = OOPsyParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 203
            self.match(OOPsyParser.DOT_SEPARATOR)
            self.state = 204
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 205
            self.match(OOPsyParser.LEFT_PARENTHESIS)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1152921521786720192) != 0) or _la==72:
                self.state = 206
                self.argumentList()


            self.state = 209
            self.match(OOPsyParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valueExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OOPsyParser.ValueExpressionContext)
            else:
                return self.getTypedRuleContext(OOPsyParser.ValueExpressionContext,i)


        def COMMA_SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(OOPsyParser.COMMA_SEPARATOR)
            else:
                return self.getToken(OOPsyParser.COMMA_SEPARATOR, i)

        def getRuleIndex(self):
            return OOPsyParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)




    def argumentList(self):

        localctx = OOPsyParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.valueExpression(0)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 212
                self.match(OOPsyParser.COMMA_SEPARATOR)
                self.state = 213
                self.valueExpression(0)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT_SEPARATOR(self):
            return self.getToken(OOPsyParser.DOT_SEPARATOR, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OOPsyParser.IDENTIFIER)
            else:
                return self.getToken(OOPsyParser.IDENTIFIER, i)

        def SELF_KEYWORD(self):
            return self.getToken(OOPsyParser.SELF_KEYWORD, 0)

        def getRuleIndex(self):
            return OOPsyParser.RULE_memberAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberAccess" ):
                listener.enterMemberAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberAccess" ):
                listener.exitMemberAccess(self)




    def memberAccess(self):

        localctx = OOPsyParser.MemberAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_memberAccess)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not(_la==60 or _la==72):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 220
            self.match(OOPsyParser.DOT_SEPARATOR)
            self.state = 221
            self.match(OOPsyParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OOPSY_TYPE_INT(self):
            return self.getToken(OOPsyParser.OOPSY_TYPE_INT, 0)

        def OOPSY_TYPE_FLOAT(self):
            return self.getToken(OOPsyParser.OOPSY_TYPE_FLOAT, 0)

        def OOPSY_TYPE_STRING(self):
            return self.getToken(OOPsyParser.OOPSY_TYPE_STRING, 0)

        def OOPSY_TYPE_CHAR(self):
            return self.getToken(OOPsyParser.OOPSY_TYPE_CHAR, 0)

        def OOPSY_TYPE_BOOL(self):
            return self.getToken(OOPsyParser.OOPSY_TYPE_BOOL, 0)

        def IDENTIFIER(self):
            return self.getToken(OOPsyParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return OOPsyParser.RULE_typeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeName" ):
                listener.enterTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeName" ):
                listener.exitTypeName(self)




    def typeName(self):

        localctx = OOPsyParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_typeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0) or _la==72):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.valueExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def valueExpression_sempred(self, localctx:ValueExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         




