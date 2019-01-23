import ply.lex as lex
import ply.yacc as yacc

import sympy

def parse(s):
    ################################################################################
    # Lexer
    ################################################################################

    reserved = {'sqrt': 'SQRT'}
    tokens = [
        'ID',
        'INT',
        'FLOAT',
        'POWER',
        'ABS'
    ]
    tokens += list(reserved.values())
    literals = ['+', '-', '*', '/', '(', ')']
    t_POWER = r'\^'
    t_ABS = r'\|'

    t_ignore = r' '

    def t_FLOAT(t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t


    def t_INT(t):
        r'\d+'
        t.value = int(t.value)
        return t


    def t_ID(t):
        r'[a-zA-Z_]+'
        t.type = reserved.get(t.value, 'ID')  # Check for reserved words
        return t


    def t_error(t):
        print("Illegal character '{}' at position {}".format(t.value, t.lexpos + 1))
        t.lexer.skip(1)


    lexer = lex.lex()

    ################################################################################
    # Parser
    ################################################################################

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('left', 'POWER', 'SQRT'),
        ('right', 'UMINUS')
    )


    def p_main(p):
        '''
        main : expression
        '''
        p[0] = p[1]


    def p_var_assign(p):
        '''
        var_assign : ID
        '''
        global _sym
        p[0] = sympy.Symbol(p[1])
        _sym = p[1]


    def p_expression(p):
        '''
        expression : INT
                   | FLOAT
                   | SQRT
                   | var_assign
        '''
        p[0] = p[1]

    def p_expression_binop(p):
        '''
        expression : expression '+' expression
                   | expression '-' expression
                   | expression '*' expression
                   | expression '/' expression
                   | expression POWER expression
        '''

        if p[2] == '+':
            p[0] = p[1] + p[3]

        elif p[2] == '-':
            p[0] = p[1] - p[3]

        elif p[2] == '*':
            p[0] = p[1] * p[3]

        elif p[2] == '/':
            p[0] = p[1] / p[3]

        elif p[2] == '^':
            p[0] = p[1] ** p[3]

    def p_expression_sqrt(p):
        '''
        expression : SQRT expression
        '''
        p[0] = sympy.sqrt(p[2])


    def p_expression_uminus(p):
        '''
        expression : '-' expression %prec UMINUS
        '''
        p[0] = -p[2]


    def p_expression_group(p):
        '''
        expression : '(' expression ')'
        '''
        p[0] = p[2]


    def p_expression_abs(p):
        '''
        expression : ABS expression ABS
        '''
        p[0] = sympy.Abs(p[2])

    def p_error(p):
        if p:
            print("Syntax error '{}' at position {}".format(p.value, p.lexpos + 1))
        else:
            print("Syntax error at EOF")


    parser = yacc.yacc()
    temp = parser.parse(s)
    try:
        return temp, _sym
    except NameError:
        return temp, None


if __name__ == '__main__':
    from sympy import S
    while True:
        s = input()
        equation, sym = parse(s)
        if sym:
            res = sympy.solveset(equation, sym, S.Reals)
        else:
            print(equation)

        if type(res) is sympy.EmptySet:
            print("No solutions found")
        else:
            print("Root{}: {}".format('s' if len(res) > 1 else '', ', '.join([str(i) for i in res])))