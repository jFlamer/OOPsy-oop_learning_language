grammar OOPsy;

program         : classDecl* mainMethod EOF ;

statement
    : methodDecl
    | attributeDecl
    | assignment
    | ifStatement
    | loopStatement
    | forStatement
    | returnStatement
    | printStatement
    | expressionStatement
    | createStatement
    | breakStatement
    | continueStatement
    | superCallStatement
    | inputStatement
    | commentStatement
    | localVarDecl
    ;

mainMethod      : METHOD_KEYWORD MAIN_KEYWORD LEFT_PARENTHESIS paramList? RIGHT_PARENTHESIS block ;
classDecl       : (ABSTRACT_KEYWORD | FINAL_KEYWORD)? CLASS_KEYWORD IDENTIFIER (INHERITS_KEYWORD IDENTIFIER)? LEFT_BRACE classElement* RIGHT_BRACE ;
classElement
    : attributeDecl
    | methodDecl
    | constructorDecl
    ;
methodDecl      : (accessModifier)? (ABSTRACT_KEYWORD)? (FINAL_KEYWORD)? OVERRIDE_KEYWORD? METHOD_KEYWORD IDENTIFIER LEFT_PARENTHESIS paramList? RIGHT_PARENTHESIS (block | SEMICOLON_SEPARATOR) ;
attributeDecl   : accessModifier? HAS_ATTRIBUTE_KEYWORD IDENTIFIER COLON_SEPARATOR typeName SEMICOLON_SEPARATOR ;
constructorDecl : accessModifier? CONSTRUCTOR_KEYWORD LEFT_PARENTHESIS paramList? RIGHT_PARENTHESIS block ;
accessModifier
    : PUBLIC_MODIFIER
    | PRIVATE_MODIFIER
    ;

assignment      : (IDENTIFIER | memberAccess | indexedAccess) ASSIGNMENT_OPERATOR valueExpression SEMICOLON_SEPARATOR ;
returnStatement : RETURN_STATEMENT valueExpression? SEMICOLON_SEPARATOR ;
expressionStatement : anyExpression SEMICOLON_SEPARATOR ;
printStatement  : PRINT_KEYWORD LEFT_PARENTHESIS valueExpression RIGHT_PARENTHESIS SEMICOLON_SEPARATOR ;
createStatement : CREATE_KEYWORD IDENTIFIER OF_STATEMENT IDENTIFIER (LEFT_PARENTHESIS argumentList? RIGHT_PARENTHESIS)? SEMICOLON_SEPARATOR ;

ifStatement     : IF_KEYWORD logicalExpression block (ELSE_KEYWORD block)? ;
loopStatement   : REPEAT_KEYWORD block UNTIL_KEYWORD logicalExpression SEMICOLON_SEPARATOR ;
forStatement    : FOR_KEYWORD IDENTIFIER IN_KEYWORD valueExpression DO_KEYWORD block ;
breakStatement  : BREAK_STATEMENT SEMICOLON_SEPARATOR ;
continueStatement   : CONTINUE_STATEMENT SEMICOLON_SEPARATOR ;
superCallStatement  : SUPER_CALL LEFT_PARENTHESIS argumentList? RIGHT_PARENTHESIS SEMICOLON_SEPARATOR ;
inputStatement  : INPUT_STATEMENT LEFT_PARENTHESIS STRING_LITERAL RIGHT_PARENTHESIS ASSIGNMENT_OPERATOR (IDENTIFIER | memberAccess) SEMICOLON_SEPARATOR ;
commentStatement: LINE_COMMENT ;
localVarDecl    : VAR_KEYWORD IDENTIFIER COLON_SEPARATOR typeName ASSIGNMENT_OPERATOR valueExpression SEMICOLON_SEPARATOR ;

block           : LEFT_BRACE statement* RIGHT_BRACE ;

paramList       : typedParam (COMMA_SEPARATOR typedParam)* ;
typedParam      : IDENTIFIER COLON_SEPARATOR typeName ;

valueExpression
    : valueExpression ('*' | '/' | '%') valueExpression
    | valueExpression ('+' | '-') valueExpression
    | IDENTIFIER
    | INT_LITERAL
    | FLOAT_LITERAL
    | STRING_LITERAL
    | CHAR_LITERAL
    | BOOL_LITERAL_TRUE
    | BOOL_LITERAL_FALSE
    | methodCall
    | memberAccess
    | LEFT_PARENTHESIS valueExpression RIGHT_PARENTHESIS
    | inputCall
    | listLiteral
    | dictLiteral
    | indexedAccess
    ;

listLiteral : LEFT_BRACKET (valueExpression (COMMA_SEPARATOR valueExpression)*)? RIGHT_BRACKET ;
dictLiteral : LEFT_BRACE dictEntry (COMMA_SEPARATOR dictEntry)* RIGHT_BRACE ;
dictEntry   : valueExpression COLON_SEPARATOR valueExpression ;

logicalExpression
    : logicalTerm (OR_OPERATOR logicalTerm)*
    ;

logicalTerm
    : logicalFactor (AND_OPERATOR logicalFactor)*
    ;

logicalFactor
    : valueExpression (('==' | '!=' | '<' | '>' | '<=' | '>=') valueExpression)?
    | LEFT_PARENTHESIS logicalExpression RIGHT_PARENTHESIS
    ;


anyExpression
    : valueExpression
    | PRINT_KEYWORD LEFT_PARENTHESIS valueExpression RIGHT_PARENTHESIS
    ;

indexedAccess : (IDENTIFIER | memberAccess) LEFT_BRACKET valueExpression RIGHT_BRACKET ;
methodCall      : IDENTIFIER DOT_SEPARATOR IDENTIFIER LEFT_PARENTHESIS argumentList? RIGHT_PARENTHESIS ;
inputCall       : INPUT_STATEMENT LEFT_PARENTHESIS valueExpression RIGHT_PARENTHESIS ;
argumentList    : valueExpression (COMMA_SEPARATOR valueExpression)* ;
memberAccess    : (IDENTIFIER | SELF_KEYWORD) DOT_SEPARATOR IDENTIFIER ;

typeName        : simpleType | listType | dictionaryType ;
simpleType      : OOPSY_TYPE_INT | OOPSY_TYPE_FLOAT | OOPSY_TYPE_STRING | OOPSY_TYPE_CHAR | OOPSY_TYPE_BOOL | IDENTIFIER ;
listType        : LIST_TYPE '<' typeName '>' ;
dictionaryType  : DICTIONARY_TYPE '<' typeName COMMA_SEPARATOR typeName '>' ;

// === LEXER RULES ===
// === Data Types ===
OOPSY_TYPE_INT   : 'int';
OOPSY_TYPE_FLOAT : 'float';
OOPSY_TYPE_STRING : 'string';
OOPSY_TYPE_CHAR  : 'char';
OOPSY_TYPE_BOOL  : 'bool';

// === Literals ===
BOOL_LITERAL_TRUE  : 'true';
BOOL_LITERAL_FALSE : 'false';

INT_LITERAL     : [0-9]+;
FLOAT_LITERAL   : [0-9]+ '.' [0-9]+;
CHAR_LITERAL    : '\'' ( ~[\r\n\\] | '\\' . ) '\'';
STRING_LITERAL  : '"' ( ~["\\] | '\\' . )* '"';

// === Arithmetic and Logical Operators ===
PLUS_OPERATOR     : '+';
MINUS_OPERATOR    : '-';
MULTIPLY_OPERATOR : '*';
DIVIDE_OPERATOR   : '/';
MODULO_OPERATOR   : '%';

INCREMENT_OPERATOR : '++';
DECREMENT_OPERATOR : '--';

ASSIGNMENT_OPERATOR               : '=';
ADDITION_ASSIGNMENT_OPERATOR      : '+=';
SUBTRACTION_ASSIGNMENT_OPERATOR   : '-=';
MULTIPLICATION_ASSIGNMENT_OPERATOR: '*=';
DIVISION_ASSIGNMENT_OPERATOR      : '/=';

EQUAL_OPERATOR      : '==';
UNEQUAL_OPERATOR    : '!=';
GREATER_OPERATOR    : '>';
LESSER_OPERATOR     : '<';
GREATER_EQ_OPERATOR : '>=';
LESSER_EQ_OPERATOR  : '<=';

AND_OPERATOR : '&&';
OR_OPERATOR  : '||';

// === Symbols and Separators ===
LEFT_BRACKET         : '[';
RIGHT_BRACKET        : ']';
LEFT_PARENTHESIS     : '(';
RIGHT_PARENTHESIS    : ')';
LEFT_BRACE           : '{';
RIGHT_BRACE          : '}';

DOT_SEPARATOR        : '.';
COMMA_SEPARATOR      : ',';
COLON_SEPARATOR      : ':';
SEMICOLON_SEPARATOR  : ';';

// === Comments and Whitespace ===
LINE_COMMENT  : '//' ~[\r\n]* ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;
WHITESPACE    : [ \t\r\n]+ -> skip;

// === OOP Keywords ===
CLASS_KEYWORD          : 'class';
MAIN_KEYWORD           : 'main';
INHERITS_KEYWORD       : 'inherits';
HAS_ATTRIBUTE_KEYWORD  : 'has';
METHOD_KEYWORD         : 'method';
CONSTRUCTOR_KEYWORD    : 'constructor';
CREATE_KEYWORD         : 'create';
OF_STATEMENT           : 'of';
PRINT_KEYWORD          : 'print';
IF_KEYWORD             : 'if';
ELSE_KEYWORD           : 'else';
REPEAT_KEYWORD         : 'repeat';
UNTIL_KEYWORD          : 'until';
FOR_KEYWORD            : 'for';
IN_KEYWORD             : 'in';
DO_KEYWORD             : 'do';
INPUT_STATEMENT        : 'input';
SELF_KEYWORD           : 'self';
ABSTRACT_KEYWORD       : 'abstract';
FINAL_KEYWORD          : 'final';
OVERRIDE_KEYWORD       : 'override';
SUPER_CALL             : 'super';
PUBLIC_MODIFIER        : 'public';
PRIVATE_MODIFIER       : 'private';
LIST_TYPE              : 'list';
DICTIONARY_TYPE        : 'dict';
RETURN_STATEMENT       : 'return';
BREAK_STATEMENT        : 'break';
CONTINUE_STATEMENT     : 'continue';
VAR_KEYWORD            : 'var';

// === Identifiers ===
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
