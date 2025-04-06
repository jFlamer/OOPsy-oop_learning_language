lexer grammar OOPsy;

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
LINE_COMMENT  : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;
WHITESPACE    : [ \t\r\n]+ -> skip;

// === OOP Keywords ===
CLASS_KEYWORD          : 'class';
INHERITS_KEYWORD       : 'inherits';
HAS_ATTRIBUTE_KEYWORD  : 'has';
METHOD_KEYWORD         : 'method';
CONSTRUCTOR_KEYWORD    : 'constructor';
END_STATEMENT          : 'end';
CREATE_KEYWORD         : 'create';
OF_STATEMENT           : 'of';
PRINT_KEYWORD          : 'print';
IF_KEYWORD             : 'if';
ELSE_KEYWORD           : 'else';
REPEAT_KEYWORD         : 'repeat';
UNTIL_KEYWORD          : 'until';
INPUT_STATEMENT        : 'input';
SELF_KEYWORD           : 'self';
ABSTRACT_CLASS         : 'abstract';
FINAL_CLASS            : 'final';
OVERRIDE_METHOD        : 'override';
SUPER_CALL             : 'super';
PUBLIC_MODIFIER        : 'public';
PRIVATE_MODIFIER       : 'private';
LIST_TYPE              : 'list';
DICTIONARY_TYPE        : 'dict';
RETURN_STATEMENT       : 'return';
BREAK_STATEMENT        : 'break';
CONTINUE_STATEMENT     : 'continue';

// === Identifiers ===
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
