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
        4,1,71,281,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,77,8,1,1,2,1,2,1,2,1,2,3,2,
        83,8,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,92,8,3,1,3,1,3,5,3,96,8,3,
        10,3,12,3,99,9,3,1,3,1,3,1,4,1,4,1,4,3,4,106,8,4,1,5,1,5,1,5,1,5,
        3,5,112,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,
        126,8,7,1,7,1,7,1,7,1,8,1,8,3,8,133,8,8,1,8,1,8,1,8,1,8,1,9,1,9,
        3,9,141,8,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,13,165,
        8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,
        1,17,1,17,5,17,181,8,17,10,17,12,17,184,9,17,1,17,1,17,1,18,1,18,
        1,18,5,18,191,8,18,10,18,12,18,194,9,18,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,210,8,19,1,19,
        1,19,1,19,1,19,1,19,1,19,5,19,218,8,19,10,19,12,19,221,9,19,1,20,
        1,20,1,20,5,20,226,8,20,10,20,12,20,229,9,20,1,21,1,21,1,21,5,21,
        234,8,21,10,21,12,21,237,9,21,1,22,1,22,1,22,3,22,242,8,22,1,22,
        1,22,1,22,1,22,3,22,248,8,22,1,23,1,23,1,23,1,23,1,23,1,23,3,23,
        256,8,23,1,24,1,24,1,24,1,24,1,24,3,24,263,8,24,1,24,1,24,1,25,1,
        25,1,25,5,25,270,8,25,10,25,12,25,273,9,25,1,26,1,26,1,26,1,26,1,
        27,1,27,1,27,0,1,38,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,0,5,1,0,14,16,1,0,12,13,1,0,
        24,29,2,0,59,59,71,71,2,0,1,5,71,71,293,0,59,1,0,0,0,2,76,1,0,0,
        0,4,78,1,0,0,0,6,87,1,0,0,0,8,105,1,0,0,0,10,107,1,0,0,0,12,116,
        1,0,0,0,14,122,1,0,0,0,16,132,1,0,0,0,18,138,1,0,0,0,20,144,1,0,
        0,0,22,147,1,0,0,0,24,153,1,0,0,0,26,159,1,0,0,0,28,166,1,0,0,0,
        30,172,1,0,0,0,32,175,1,0,0,0,34,178,1,0,0,0,36,187,1,0,0,0,38,209,
        1,0,0,0,40,222,1,0,0,0,42,230,1,0,0,0,44,247,1,0,0,0,46,255,1,0,
        0,0,48,257,1,0,0,0,50,266,1,0,0,0,52,274,1,0,0,0,54,278,1,0,0,0,
        56,58,3,6,3,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,
        0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,63,3,4,2,0,63,64,5,0,0,1,64,
        1,1,0,0,0,65,77,3,10,5,0,66,77,3,12,6,0,67,77,3,16,8,0,68,77,3,26,
        13,0,69,77,3,28,14,0,70,77,3,18,9,0,71,77,3,22,11,0,72,77,3,20,10,
        0,73,77,3,24,12,0,74,77,3,30,15,0,75,77,3,32,16,0,76,65,1,0,0,0,
        76,66,1,0,0,0,76,67,1,0,0,0,76,68,1,0,0,0,76,69,1,0,0,0,76,70,1,
        0,0,0,76,71,1,0,0,0,76,72,1,0,0,0,76,73,1,0,0,0,76,74,1,0,0,0,76,
        75,1,0,0,0,77,3,1,0,0,0,78,79,5,49,0,0,79,80,5,46,0,0,80,82,5,34,
        0,0,81,83,3,36,18,0,82,81,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,
        85,5,35,0,0,85,86,3,34,17,0,86,5,1,0,0,0,87,88,5,45,0,0,88,91,5,
        71,0,0,89,90,5,47,0,0,90,92,5,71,0,0,91,89,1,0,0,0,91,92,1,0,0,0,
        92,93,1,0,0,0,93,97,5,36,0,0,94,96,3,8,4,0,95,94,1,0,0,0,96,99,1,
        0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,
        101,5,37,0,0,101,7,1,0,0,0,102,106,3,12,6,0,103,106,3,10,5,0,104,
        106,3,14,7,0,105,102,1,0,0,0,105,103,1,0,0,0,105,104,1,0,0,0,106,
        9,1,0,0,0,107,108,5,49,0,0,108,109,5,71,0,0,109,111,5,34,0,0,110,
        112,3,36,18,0,111,110,1,0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,
        114,5,35,0,0,114,115,3,34,17,0,115,11,1,0,0,0,116,117,5,48,0,0,117,
        118,5,71,0,0,118,119,5,40,0,0,119,120,3,54,27,0,120,121,5,41,0,0,
        121,13,1,0,0,0,122,123,5,50,0,0,123,125,5,34,0,0,124,126,3,36,18,
        0,125,124,1,0,0,0,125,126,1,0,0,0,126,127,1,0,0,0,127,128,5,35,0,
        0,128,129,3,34,17,0,129,15,1,0,0,0,130,133,5,71,0,0,131,133,3,52,
        26,0,132,130,1,0,0,0,132,131,1,0,0,0,133,134,1,0,0,0,134,135,5,19,
        0,0,135,136,3,38,19,0,136,137,5,41,0,0,137,17,1,0,0,0,138,140,5,
        68,0,0,139,141,3,38,19,0,140,139,1,0,0,0,140,141,1,0,0,0,141,142,
        1,0,0,0,142,143,5,41,0,0,143,19,1,0,0,0,144,145,3,46,23,0,145,146,
        5,41,0,0,146,21,1,0,0,0,147,148,5,53,0,0,148,149,5,34,0,0,149,150,
        3,38,19,0,150,151,5,35,0,0,151,152,5,41,0,0,152,23,1,0,0,0,153,154,
        5,51,0,0,154,155,5,71,0,0,155,156,5,52,0,0,156,157,5,71,0,0,157,
        158,5,41,0,0,158,25,1,0,0,0,159,160,5,54,0,0,160,161,3,40,20,0,161,
        164,3,34,17,0,162,163,5,55,0,0,163,165,3,34,17,0,164,162,1,0,0,0,
        164,165,1,0,0,0,165,27,1,0,0,0,166,167,5,56,0,0,167,168,3,34,17,
        0,168,169,5,57,0,0,169,170,3,40,20,0,170,171,5,41,0,0,171,29,1,0,
        0,0,172,173,5,69,0,0,173,174,5,41,0,0,174,31,1,0,0,0,175,176,5,70,
        0,0,176,177,5,41,0,0,177,33,1,0,0,0,178,182,5,36,0,0,179,181,3,2,
        1,0,180,179,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,183,1,0,
        0,0,183,185,1,0,0,0,184,182,1,0,0,0,185,186,5,37,0,0,186,35,1,0,
        0,0,187,192,5,71,0,0,188,189,5,39,0,0,189,191,5,71,0,0,190,188,1,
        0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,37,1,0,
        0,0,194,192,1,0,0,0,195,196,6,19,-1,0,196,210,5,71,0,0,197,210,5,
        8,0,0,198,210,5,9,0,0,199,210,5,11,0,0,200,210,5,10,0,0,201,210,
        5,6,0,0,202,210,5,7,0,0,203,210,3,48,24,0,204,210,3,52,26,0,205,
        206,5,34,0,0,206,207,3,38,19,0,207,208,5,35,0,0,208,210,1,0,0,0,
        209,195,1,0,0,0,209,197,1,0,0,0,209,198,1,0,0,0,209,199,1,0,0,0,
        209,200,1,0,0,0,209,201,1,0,0,0,209,202,1,0,0,0,209,203,1,0,0,0,
        209,204,1,0,0,0,209,205,1,0,0,0,210,219,1,0,0,0,211,212,10,12,0,
        0,212,213,7,0,0,0,213,218,3,38,19,13,214,215,10,11,0,0,215,216,7,
        1,0,0,216,218,3,38,19,12,217,211,1,0,0,0,217,214,1,0,0,0,218,221,
        1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,39,1,0,0,0,221,219,1,
        0,0,0,222,227,3,42,21,0,223,224,5,31,0,0,224,226,3,42,21,0,225,223,
        1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,41,1,
        0,0,0,229,227,1,0,0,0,230,235,3,44,22,0,231,232,5,30,0,0,232,234,
        3,44,22,0,233,231,1,0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,235,236,
        1,0,0,0,236,43,1,0,0,0,237,235,1,0,0,0,238,241,3,38,19,0,239,240,
        7,2,0,0,240,242,3,38,19,0,241,239,1,0,0,0,241,242,1,0,0,0,242,248,
        1,0,0,0,243,244,5,34,0,0,244,245,3,40,20,0,245,246,5,35,0,0,246,
        248,1,0,0,0,247,238,1,0,0,0,247,243,1,0,0,0,248,45,1,0,0,0,249,256,
        3,38,19,0,250,251,5,53,0,0,251,252,5,34,0,0,252,253,3,38,19,0,253,
        254,5,35,0,0,254,256,1,0,0,0,255,249,1,0,0,0,255,250,1,0,0,0,256,
        47,1,0,0,0,257,258,5,71,0,0,258,259,5,38,0,0,259,260,5,71,0,0,260,
        262,5,34,0,0,261,263,3,50,25,0,262,261,1,0,0,0,262,263,1,0,0,0,263,
        264,1,0,0,0,264,265,5,35,0,0,265,49,1,0,0,0,266,271,3,38,19,0,267,
        268,5,39,0,0,268,270,3,38,19,0,269,267,1,0,0,0,270,273,1,0,0,0,271,
        269,1,0,0,0,271,272,1,0,0,0,272,51,1,0,0,0,273,271,1,0,0,0,274,275,
        7,3,0,0,275,276,5,38,0,0,276,277,5,71,0,0,277,53,1,0,0,0,278,279,
        7,4,0,0,279,55,1,0,0,0,23,59,76,82,91,97,105,111,125,132,140,164,
        182,192,209,217,219,227,235,241,247,255,262,271
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
                     "'method'", "'constructor'", "'create'", "'of'", "'print'", 
                     "'if'", "'else'", "'repeat'", "'until'", "'input'", 
                     "'self'", "'abstract'", "'final'", "'override'", "'super'", 
                     "'public'", "'private'", "'list'", "'dict'", "'return'", 
                     "'break'", "'continue'" ]

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
                      "CREATE_KEYWORD", "OF_STATEMENT", "PRINT_KEYWORD", 
                      "IF_KEYWORD", "ELSE_KEYWORD", "REPEAT_KEYWORD", "UNTIL_KEYWORD", 
                      "INPUT_STATEMENT", "SELF_KEYWORD", "ABSTRACT_CLASS", 
                      "FINAL_CLASS", "OVERRIDE_METHOD", "SUPER_CALL", "PUBLIC_MODIFIER", 
                      "PRIVATE_MODIFIER", "LIST_TYPE", "DICTIONARY_TYPE", 
                      "RETURN_STATEMENT", "BREAK_STATEMENT", "CONTINUE_STATEMENT", 
                      "IDENTIFIER" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_mainMethod = 2
    RULE_classDecl = 3
    RULE_classElement = 4
    RULE_methodDecl = 5
    RULE_attributeDecl = 6
    RULE_constructorDecl = 7
    RULE_assignment = 8
    RULE_returnStatement = 9
    RULE_expressionStatement = 10
    RULE_printStatement = 11
    RULE_createStatement = 12
    RULE_ifStatement = 13
    RULE_loopStatement = 14
    RULE_breakStatement = 15
    RULE_continueStatement = 16
    RULE_block = 17
    RULE_paramList = 18
    RULE_valueExpression = 19
    RULE_logicalExpression = 20
    RULE_logicalTerm = 21
    RULE_logicalFactor = 22
    RULE_anyExpression = 23
    RULE_methodCall = 24
    RULE_argumentList = 25
    RULE_memberAccess = 26
    RULE_typeName = 27

    ruleNames =  [ "program", "statement", "mainMethod", "classDecl", "classElement", 
                   "methodDecl", "attributeDecl", "constructorDecl", "assignment", 
                   "returnStatement", "expressionStatement", "printStatement", 
                   "createStatement", "ifStatement", "loopStatement", "breakStatement", 
                   "continueStatement", "block", "paramList", "valueExpression", 
                   "logicalExpression", "logicalTerm", "logicalFactor", 
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
    CREATE_KEYWORD=51
    OF_STATEMENT=52
    PRINT_KEYWORD=53
    IF_KEYWORD=54
    ELSE_KEYWORD=55
    REPEAT_KEYWORD=56
    UNTIL_KEYWORD=57
    INPUT_STATEMENT=58
    SELF_KEYWORD=59
    ABSTRACT_CLASS=60
    FINAL_CLASS=61
    OVERRIDE_METHOD=62
    SUPER_CALL=63
    PUBLIC_MODIFIER=64
    PRIVATE_MODIFIER=65
    LIST_TYPE=66
    DICTIONARY_TYPE=67
    RETURN_STATEMENT=68
    BREAK_STATEMENT=69
    CONTINUE_STATEMENT=70
    IDENTIFIER=71

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = OOPsyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 56
                self.classDecl()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.mainMethod()
            self.state = 63
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


        def breakStatement(self):
            return self.getTypedRuleContext(OOPsyParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(OOPsyParser.ContinueStatementContext,0)


        def getRuleIndex(self):
            return OOPsyParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = OOPsyParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.methodDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.attributeDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.loopStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 70
                self.returnStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 71
                self.printStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 72
                self.expressionStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 73
                self.createStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 74
                self.breakStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 75
                self.continueStatement()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainMethod" ):
                return visitor.visitMainMethod(self)
            else:
                return visitor.visitChildren(self)




    def mainMethod(self):

        localctx = OOPsyParser.MainMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mainMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(OOPsyParser.METHOD_KEYWORD)
            self.state = 79
            self.match(OOPsyParser.MAIN_KEYWORD)
            self.state = 80
            self.match(OOPsyParser.LEFT_PARENTHESIS)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 81
                self.paramList()


            self.state = 84
            self.match(OOPsyParser.RIGHT_PARENTHESIS)
            self.state = 85
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

        def classElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OOPsyParser.ClassElementContext)
            else:
                return self.getTypedRuleContext(OOPsyParser.ClassElementContext,i)


        def getRuleIndex(self):
            return OOPsyParser.RULE_classDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDecl" ):
                listener.enterClassDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDecl" ):
                listener.exitClassDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = OOPsyParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(OOPsyParser.CLASS_KEYWORD)
            self.state = 88
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 89
                self.match(OOPsyParser.INHERITS_KEYWORD)
                self.state = 90
                self.match(OOPsyParser.IDENTIFIER)


            self.state = 93
            self.match(OOPsyParser.LEFT_BRACE)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1970324836974592) != 0):
                self.state = 94
                self.classElement()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.match(OOPsyParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeDecl(self):
            return self.getTypedRuleContext(OOPsyParser.AttributeDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(OOPsyParser.MethodDeclContext,0)


        def constructorDecl(self):
            return self.getTypedRuleContext(OOPsyParser.ConstructorDeclContext,0)


        def getRuleIndex(self):
            return OOPsyParser.RULE_classElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassElement" ):
                listener.enterClassElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassElement" ):
                listener.exitClassElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassElement" ):
                return visitor.visitClassElement(self)
            else:
                return visitor.visitChildren(self)




    def classElement(self):

        localctx = OOPsyParser.ClassElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classElement)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.attributeDecl()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.methodDecl()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.constructorDecl()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = OOPsyParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(OOPsyParser.METHOD_KEYWORD)
            self.state = 108
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 109
            self.match(OOPsyParser.LEFT_PARENTHESIS)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 110
                self.paramList()


            self.state = 113
            self.match(OOPsyParser.RIGHT_PARENTHESIS)
            self.state = 114
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeDecl" ):
                return visitor.visitAttributeDecl(self)
            else:
                return visitor.visitChildren(self)




    def attributeDecl(self):

        localctx = OOPsyParser.AttributeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attributeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(OOPsyParser.HAS_ATTRIBUTE_KEYWORD)
            self.state = 117
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 118
            self.match(OOPsyParser.COLON_SEPARATOR)
            self.state = 119
            self.typeName()
            self.state = 120
            self.match(OOPsyParser.SEMICOLON_SEPARATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR_KEYWORD(self):
            return self.getToken(OOPsyParser.CONSTRUCTOR_KEYWORD, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.RIGHT_PARENTHESIS, 0)

        def block(self):
            return self.getTypedRuleContext(OOPsyParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(OOPsyParser.ParamListContext,0)


        def getRuleIndex(self):
            return OOPsyParser.RULE_constructorDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorDecl" ):
                listener.enterConstructorDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorDecl" ):
                listener.exitConstructorDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorDecl" ):
                return visitor.visitConstructorDecl(self)
            else:
                return visitor.visitChildren(self)




    def constructorDecl(self):

        localctx = OOPsyParser.ConstructorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constructorDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(OOPsyParser.CONSTRUCTOR_KEYWORD)
            self.state = 123
            self.match(OOPsyParser.LEFT_PARENTHESIS)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 124
                self.paramList()


            self.state = 127
            self.match(OOPsyParser.RIGHT_PARENTHESIS)
            self.state = 128
            self.block()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = OOPsyParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 130
                self.match(OOPsyParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 131
                self.memberAccess()
                pass


            self.state = 134
            self.match(OOPsyParser.ASSIGNMENT_OPERATOR)
            self.state = 135
            self.valueExpression(0)
            self.state = 136
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = OOPsyParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(OOPsyParser.RETURN_STATEMENT)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460769483296704) != 0) or _la==71:
                self.state = 139
                self.valueExpression(0)


            self.state = 142
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = OOPsyParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.anyExpression()
            self.state = 145
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = OOPsyParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(OOPsyParser.PRINT_KEYWORD)
            self.state = 148
            self.match(OOPsyParser.LEFT_PARENTHESIS)
            self.state = 149
            self.valueExpression(0)
            self.state = 150
            self.match(OOPsyParser.RIGHT_PARENTHESIS)
            self.state = 151
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateStatement" ):
                return visitor.visitCreateStatement(self)
            else:
                return visitor.visitChildren(self)




    def createStatement(self):

        localctx = OOPsyParser.CreateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_createStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(OOPsyParser.CREATE_KEYWORD)
            self.state = 154
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 155
            self.match(OOPsyParser.OF_STATEMENT)
            self.state = 156
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 157
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = OOPsyParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(OOPsyParser.IF_KEYWORD)
            self.state = 160
            self.logicalExpression()
            self.state = 161
            self.block()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 162
                self.match(OOPsyParser.ELSE_KEYWORD)
                self.state = 163
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = OOPsyParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(OOPsyParser.REPEAT_KEYWORD)
            self.state = 167
            self.block()
            self.state = 168
            self.match(OOPsyParser.UNTIL_KEYWORD)
            self.state = 169
            self.logicalExpression()
            self.state = 170
            self.match(OOPsyParser.SEMICOLON_SEPARATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_STATEMENT(self):
            return self.getToken(OOPsyParser.BREAK_STATEMENT, 0)

        def SEMICOLON_SEPARATOR(self):
            return self.getToken(OOPsyParser.SEMICOLON_SEPARATOR, 0)

        def getRuleIndex(self):
            return OOPsyParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = OOPsyParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(OOPsyParser.BREAK_STATEMENT)
            self.state = 173
            self.match(OOPsyParser.SEMICOLON_SEPARATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE_STATEMENT(self):
            return self.getToken(OOPsyParser.CONTINUE_STATEMENT, 0)

        def SEMICOLON_SEPARATOR(self):
            return self.getToken(OOPsyParser.SEMICOLON_SEPARATOR, 0)

        def getRuleIndex(self):
            return OOPsyParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = OOPsyParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(OOPsyParser.CONTINUE_STATEMENT)
            self.state = 176
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = OOPsyParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(OOPsyParser.LEFT_BRACE)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 678636186029264832) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 15) != 0):
                self.state = 179
                self.statement()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = OOPsyParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 188
                self.match(OOPsyParser.COMMA_SEPARATOR)
                self.state = 189
                self.match(OOPsyParser.IDENTIFIER)
                self.state = 194
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueExpression" ):
                return visitor.visitValueExpression(self)
            else:
                return visitor.visitChildren(self)



    def valueExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OOPsyParser.ValueExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_valueExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 196
                self.match(OOPsyParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 197
                self.match(OOPsyParser.INT_LITERAL)
                pass

            elif la_ == 3:
                self.state = 198
                self.match(OOPsyParser.FLOAT_LITERAL)
                pass

            elif la_ == 4:
                self.state = 199
                self.match(OOPsyParser.STRING_LITERAL)
                pass

            elif la_ == 5:
                self.state = 200
                self.match(OOPsyParser.CHAR_LITERAL)
                pass

            elif la_ == 6:
                self.state = 201
                self.match(OOPsyParser.BOOL_LITERAL_TRUE)
                pass

            elif la_ == 7:
                self.state = 202
                self.match(OOPsyParser.BOOL_LITERAL_FALSE)
                pass

            elif la_ == 8:
                self.state = 203
                self.methodCall()
                pass

            elif la_ == 9:
                self.state = 204
                self.memberAccess()
                pass

            elif la_ == 10:
                self.state = 205
                self.match(OOPsyParser.LEFT_PARENTHESIS)
                self.state = 206
                self.valueExpression(0)
                self.state = 207
                self.match(OOPsyParser.RIGHT_PARENTHESIS)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 217
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = OOPsyParser.ValueExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_valueExpression)
                        self.state = 211
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 212
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 213
                        self.valueExpression(13)
                        pass

                    elif la_ == 2:
                        localctx = OOPsyParser.ValueExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_valueExpression)
                        self.state = 214
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 215
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 216
                        self.valueExpression(12)
                        pass

             
                self.state = 221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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

        def logicalTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OOPsyParser.LogicalTermContext)
            else:
                return self.getTypedRuleContext(OOPsyParser.LogicalTermContext,i)


        def OR_OPERATOR(self, i:int=None):
            if i is None:
                return self.getTokens(OOPsyParser.OR_OPERATOR)
            else:
                return self.getToken(OOPsyParser.OR_OPERATOR, i)

        def getRuleIndex(self):
            return OOPsyParser.RULE_logicalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpression" ):
                listener.enterLogicalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpression" ):
                listener.exitLogicalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpression" ):
                return visitor.visitLogicalExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalExpression(self):

        localctx = OOPsyParser.LogicalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_logicalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.logicalTerm()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 223
                self.match(OOPsyParser.OR_OPERATOR)
                self.state = 224
                self.logicalTerm()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalFactor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OOPsyParser.LogicalFactorContext)
            else:
                return self.getTypedRuleContext(OOPsyParser.LogicalFactorContext,i)


        def AND_OPERATOR(self, i:int=None):
            if i is None:
                return self.getTokens(OOPsyParser.AND_OPERATOR)
            else:
                return self.getToken(OOPsyParser.AND_OPERATOR, i)

        def getRuleIndex(self):
            return OOPsyParser.RULE_logicalTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalTerm" ):
                listener.enterLogicalTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalTerm" ):
                listener.exitLogicalTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalTerm" ):
                return visitor.visitLogicalTerm(self)
            else:
                return visitor.visitChildren(self)




    def logicalTerm(self):

        localctx = OOPsyParser.LogicalTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_logicalTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.logicalFactor()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 231
                self.match(OOPsyParser.AND_OPERATOR)
                self.state = 232
                self.logicalFactor()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalFactorContext(ParserRuleContext):
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

        def LEFT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.LEFT_PARENTHESIS, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(OOPsyParser.LogicalExpressionContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(OOPsyParser.RIGHT_PARENTHESIS, 0)

        def getRuleIndex(self):
            return OOPsyParser.RULE_logicalFactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalFactor" ):
                listener.enterLogicalFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalFactor" ):
                listener.exitLogicalFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalFactor" ):
                return visitor.visitLogicalFactor(self)
            else:
                return visitor.visitChildren(self)




    def logicalFactor(self):

        localctx = OOPsyParser.LogicalFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_logicalFactor)
        self._la = 0 # Token type
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.valueExpression(0)
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0):
                    self.state = 239
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 240
                    self.valueExpression(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.match(OOPsyParser.LEFT_PARENTHESIS)
                self.state = 244
                self.logicalExpression()
                self.state = 245
                self.match(OOPsyParser.RIGHT_PARENTHESIS)
                pass


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnyExpression" ):
                return visitor.visitAnyExpression(self)
            else:
                return visitor.visitChildren(self)




    def anyExpression(self):

        localctx = OOPsyParser.AnyExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_anyExpression)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 8, 9, 10, 11, 34, 59, 71]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.valueExpression(0)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(OOPsyParser.PRINT_KEYWORD)
                self.state = 251
                self.match(OOPsyParser.LEFT_PARENTHESIS)
                self.state = 252
                self.valueExpression(0)
                self.state = 253
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = OOPsyParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 258
            self.match(OOPsyParser.DOT_SEPARATOR)
            self.state = 259
            self.match(OOPsyParser.IDENTIFIER)
            self.state = 260
            self.match(OOPsyParser.LEFT_PARENTHESIS)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460769483296704) != 0) or _la==71:
                self.state = 261
                self.argumentList()


            self.state = 264
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = OOPsyParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.valueExpression(0)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 267
                self.match(OOPsyParser.COMMA_SEPARATOR)
                self.state = 268
                self.valueExpression(0)
                self.state = 273
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberAccess" ):
                return visitor.visitMemberAccess(self)
            else:
                return visitor.visitChildren(self)




    def memberAccess(self):

        localctx = OOPsyParser.MemberAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_memberAccess)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            _la = self._input.LA(1)
            if not(_la==59 or _la==71):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 275
            self.match(OOPsyParser.DOT_SEPARATOR)
            self.state = 276
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeName" ):
                return visitor.visitTypeName(self)
            else:
                return visitor.visitChildren(self)




    def typeName(self):

        localctx = OOPsyParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_typeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0) or _la==71):
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
        self._predicates[19] = self.valueExpression_sempred
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
         




