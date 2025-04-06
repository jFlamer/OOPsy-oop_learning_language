grammar OOPsy;

program         : statement* EOF ;

statement
    : classDecl
    | methodDecl
    | attributeDecl
    | assignment
    | ifStatement
    | loopStatement
    | returnStatement
    | expressionStatement
    ;

classDecl       : CLASS_KEYWORD IDENTIFIER (INHERITS_KEYWORD IDENTIFIER)? LEFT_BRACE statement* RIGHT_BRACE ;
methodDecl      : METHOD_KEYWORD IDENTIFIER LEFT_PARENTHESIS paramList? RIGHT_PARENTHESIS block ;
attributeDecl   : HAS_ATTRIBUTE_KEYWORD IDENTIFIER COLON_SEPARATOR type SEMICOLON_SEPARATOR ;

assignment      : IDENTIFIER ASSIGNMENT_OPERATOR expression SEMICOLON_SEPARATOR ;
returnStatement : RETURN_STATEMENT expression? SEMICOLON_SEPARATOR ;
expressionStatement : expression SEMICOLON_SEPARATOR ;

ifStatement     : IF_KEYWORD expression block (ELSE_KEYWORD block)? ;
loopStatement   : REPEAT_KEYWORD block UNTIL_KEYWORD expression SEMICOLON_SEPARATOR ;

block           : LEFT_BRACE statement* RIGHT_BRACE ;

paramList       : IDENTIFIER (COMMA_SEPARATOR IDENTIFIER)* ;

expression
    : expression operator=('*' | '/' | '%') expression
    | expression operator=('+' | '-') expression
    | expression operator=('==' | '!=' | '<' | '>' | '<=' | '>=') expression
    | IDENTIFIER
    | INT_LITERAL
    | FLOAT_LITERAL
    | STRING_LITERAL
    | CHAR_LITERAL
    | BOOL_LITERAL_TRUE
    | BOOL_LITERAL_FALSE
    | methodCall
    | LEFT_PARENTHESIS expression RIGHT_PARENTHESIS
    ;

methodCall      : IDENTIFIER DOT_SEPARATOR IDENTIFIER LEFT_PARENTHESIS argumentList? RIGHT_PARENTHESIS ;
argumentList    : expression (COMMA_SEPARATOR expression)* ;

type            : TYPE_INT | TYPE_FLOAT | TYPE_STRING | TYPE_CHAR | TYPE_BOOL | IDENTIFIER ;

IDENTIFIER      : [a-zA-Z_][a-zA-Z0-9_]* ;
