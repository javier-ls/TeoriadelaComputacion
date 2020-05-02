import ply.lex as lex

tokens=("numero", "suma","resta","mul","div","pal")
t_numero=r'([0-9]+)'
t_suma=r'([\+])'
t_resta=r'([\-])'
t_mul=r'([\*])'
t_div=r'([\/])'
t_pal=r'([a-z]+)'

t_ignore_space=r'\s+'


def t_error(t):
    print"Error: Simbolo Ilegal '%s' en linea %s"%(t.value[0],t.lexer.lineno)
    t.lexer.skip(1)
lexer=lex.lex()
def prueba(entrada):
    lexer.input(entrada)
    while True:
        token=lexer.token()
        if not token:
            break

        print token

while True:
    entrada=raw_input('entrada:')
    prueba(entrada)
