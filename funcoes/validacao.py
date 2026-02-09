"""Validação de entradas do usuário"""


def validar_entrada(entrada):
    """Valida e converte entrada para inteiro."""
    entrada = entrada.strip()
    
    if not entrada:
        return (False, None, "Erro: Entrada vazia.")
    
    if '.' in entrada or ',' in entrada:
        return (False, None, "Erro: Digite apenas números inteiros (sem decimais).")
    
    try:
        valor = int(entrada)
        return (True, valor, "")
    except ValueError:
        return (False, None, "Erro: Digite apenas números inteiros.")


def verificar_duplicado(raiz, valor):
    """Verifica se valor já existe na árvore."""
    if raiz is None:
        return False
    
    if raiz.valor == valor:
        return True
    
    if valor < raiz.valor:
        return verificar_duplicado(raiz.left, valor)
    else:
        return verificar_duplicado(raiz.right, valor)
