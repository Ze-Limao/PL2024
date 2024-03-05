from ply import lex, yacc
import sys

# SQL reserved words 
reserved = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
    'and': 'AND',
    'or': 'OR',
    'inner': 'INNER',
    'outer': 'OUTER',
    'left': 'LEFT',
    'right': 'RIGHT',
    'full': 'FULL',
    'join': 'JOIN',
    'in' : 'IN',
    'on': 'ON',
    # etc....
}

# Our tokens
tokens = [
    "FIELD",
    "COMMAND",
    "DELIMITER",
    "FINAL_DELIMITER",
    "NUMBER",
    "MATH_OPERATOR",
] + list(reserved.values())


def t_COMMAND(t):
    r"\b[a-zA-Z]+\b"
    if(reserved.get(t.value.lower(), "COMMAND") in reserved):
        t.type = reserved.get(t.value.lower(), "COMMAND")
    else:
        t.type = "FIELD"
    return t

def t_NUMBER(t): 
    r"\d+(\.\d+)?"
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_MATH_OPERATOR(t):
    r">=|<=|\+|-|\*|>|<|="
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    sys.stderr.write(f"Error: Unexpected character {t.value[0]}\n")
    t.lexer.skip(1) # Skip the character


t_DELIMITER = r","
t_FINAL_DELIMITER = r";"
t_ignore = " \t"  # Ignore spaces and tabs

def main (args):
    if len(args) < 2:
        return
    with open(args[1], 'r') as file:
        data = file.read()
        lexer = lex.lex() 
        lexer.input(data)
        for tok in lexer:
            print(tok) 

if __name__ == '__main__':
    main(args=sys.argv)