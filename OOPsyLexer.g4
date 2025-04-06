lexer grammar OOPsyLexer;

// === Types ===
TYPE_INT         : 'int';
TYPE_FLOAT       : 'float';
TYPE_CHAR        : 'char';
TYPE_STRING      : 'string';
TYPE_BOOL        : 'bool';

// === Literals ===
BOOL_LITERAL_TRUE    : 'true';
BOOL_LITERAL_FALSE   : 'false';
INT_LITERAL          : [0-9]+;
FLOAT_LITERAL        : [0-9]+ '.' [0-9]+;
CHAR_LITERAL         : '\'' . '\'';
STRING_LITERAL       : '"' (~["\r\n])* '"';
NULL_LITERAL         : 'null';

// === Arithmetic & Assignment Operators ===
PLUS_OPERATOR                   : '+';
MINUS_OPERATOR                  : '-';
MULTIPLY_OPERATOR               : '*';
DIVIDE_OPERATOR                 : '/';
MODULO_OPERATOR                 : '%';
INCREMENT_OPERATOR              : '++';
DECREMENT_OPERATOR              : '--';

ASSIGNMENT_OPERATOR             : '=';
ADDITION_ASSIGNMENT_OPERATOR    : '+=';
SUBTRACTION_ASSIGNMENT_OPERATOR : '-=';
MULTIPLICATION_ASSIGNMENT_OPERATOR : '*=';
DIVISION_ASSIGNMENT_OPERATOR    : '/=';

// === Comparison Operators ===
EQUAL_OPERATOR        : '==';
UNEQUAL_OPERATOR      : '!=';
GREATER_OPERATOR      : '>';
LESSER_OPERATOR       : '<';
GREATER_EQ_OPERATOR   : '>=';
LESSER_EQ_OPERATOR    : '<=';

// === Symbols & Punctuation ===
LEFT_BRACKET        : '[';
RIGHT_BRACKET       : ']';
LEFT_PARENTHESIS    : '(';
RIGHT_PARENTHESIS   : ')';
LEFT_BRACE          : '{';
RIGHT_BRACE         : '}';
DOT_SEPARATOR       : '.';
COMMA_SEPARATOR     : ',';
COLON_SEPARATOR     : ':';
SEMICOLON_SEPARATOR : ';';

// === Logical Operators ===
AND_OPERATOR : 'and';
OR_OPERATOR  : 'or';
NOT_OPERATOR : 'not';

// === Class & OOP Keywords ===
CLASS_KEYWORD           : 'class';
INHERITS_KEYWORD        : 'inherits';
HAS_ATTRIBUTE_KEYWORD   : 'has';
METHOD_KEYWORD          : 'method';
CONSTRUCTOR_KEYWORD     : 'constructor';
END_STATEMENT           : 'end';
CREATE_KEYWORD          : 'create';
OF_STATEMENT            : 'of';
PRINT_KEYWORD           : 'print';
INPUT_STATEMENT         : 'input';
SELF_KEYWORD            : 'self';

// === OOP Enhancements ===
ABSTRACT_CLASS      : 'abstract';
FINAL_CLASS         : 'final';
OVERRIDE_METHOD     : 'override';
SUPER_CALL          : 'super';
RETURN_STATEMENT    : 'return';
PUBLIC_MODIFIER     : 'public';
PRIVATE_MODIFIER    : 'private';
PROTECTED_MODIFIER  : 'protected';

// === Control Flow ===
IF_KEYWORD      : 'if';
ELSE_KEYWORD    : 'else';
REPEAT_KEYWORD  : 'repeat';
UNTIL_KEYWORD   : 'until';
BREAK_STATEMENT : 'break';
CONTINUE_STATEMENT : 'continue';

// === Data Types ===
LIST_TYPE       : 'list';
DICTIONARY_TYPE : 'dictionary';
OBJECT_TYPE     : 'object';

// === Comments & Whitespace ===
LINE_COMMENT  : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;
WHITESPACE    : [ \t\r\n]+ -> skip;

// === Identifier ===
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
