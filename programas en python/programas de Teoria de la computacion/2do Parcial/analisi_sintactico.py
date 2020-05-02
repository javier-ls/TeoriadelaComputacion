def p_calculadora(p):
    """calculadora : operaciones"""
    pass

def p_operaciones(p):
    """operaciones : operacion"""
    pass

def p_operacion(p):
    """operacion : n1 op n2"""
    print(p)

def p_n1(p):
    """n1 : palabra | num"""
    pass

def p_op(p):
    """op : palabra | simbolo"""
    pass

def p_n2(p):
    """n2 : palabra | num"""
    pass

def p_palabra(p):
    """palabra : pal"""
    pass

def p_numero(p):
    """numero : num"""
    pass

def p_simbolo(p):
    """simbolo : suma | resta | mul | div"""
    pass
