from ply import lex

# Defining our tokens
tokens = ('KEYWORD', 'ID', 'NUMBER', 'STRING', 'COMMENT', 'RELOP', 'OP', 'LPAR', 'RPAR', 'L_SQUARE_B', 'R_SQUARE_B',
          'L_CURLY_BRACE', 'R_CURLY_BRACE', 'SEMICOLON')

# Defining the rules for our lexer
def t_KEYWORD(t):
    r'auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while'
    t.type = 'KEYWORD'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'ID'
    return t

def t_NUMBER(t):
    r'[+-]?\d+(\.\d+)?([eE][+-]?\d+)?'
    t.type = 'NUMBER'
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    t.type = 'STRING'
    return t

def t_COMMENT(t):
    r'\/\*(.|\n)*?\*\/|\/\/[^\n]*'
    t.type = 'COMMENT'
    # Count the number of newlines in the comment and update the lexer's line count
    t.lexer.lineno += t.value.count('\n')
    pass

def t_RELOP(t):
    r'==|!=|<=|>=|<|>|='
    t.type = 'RELOP'
    return t

def t_OP(t):
    r'\+|\-|\*|\/|\%'
    t.type = 'OP'
    return t

def t_LPAR(t):
    r'\('
    t.type = 'LPAR'
    return t

def t_RPAR(t):
    r'\)'
    t.type = 'RPAR'
    return t

def t_L_SQUARE_B(t):
    r'\['
    t.type = 'L_SQUARE_B'
    return t

def t_R_SQUARE_B(t):
    r'\]'
    t.type = 'R_SQUARE_B'
    return t

def t_L_CURLY_BRACE(t):
    r'\{'
    t.type = 'L_CURLY_BRACE'
    return t

def t_R_CURLY_BRACE(t):
    r'\}'
    t.type = 'R_CURLY_BRACE'
    return t

def t_SEMICOLON(t):
    r';'
    t.type = 'SEMICOLON'
    return t

# If our lexer encounters a lexeme that does not match any pattern
def t_error(t):
    print(f"<ERROR, {t.value[0]}>")
    t.lexer.skip(1)

# Handling newline characters
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Handling whitespaces
t_ignore = ' \t\n\v\f\r'

# Building the lexer by creating an instance for it
lexer = lex.lex()

# Test Code to generate a stream of tokens
code = '''
// Below is a very basic program for C programming Langauge
int main()
{
    printf("Hello World");
    return 0;
}
'''

# Passing the code to the lexer, with defined rules
lexer.input(code)

# Printing our tokens
for token in lexer:
    print(f"<{token.type}, {token.value}>")


