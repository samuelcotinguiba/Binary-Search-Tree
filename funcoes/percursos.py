"""Percursos (traversals) da BST"""

from collections import deque


def percurso_in_order(raiz, resultado=None):
    """In-Order: Esquerda → Raiz → Direita (ordem crescente em BST)."""
    if resultado is None:
        resultado = []
    
    if raiz is not None:
        percurso_in_order(raiz.left, resultado)
        resultado.append(raiz.valor)
        percurso_in_order(raiz.right, resultado)
    
    return resultado


def percurso_pre_order(raiz, resultado=None):
    """Pre-Order: Raiz → Esquerda → Direita."""
    if resultado is None:
        resultado = []
    
    if raiz is not None:
        resultado.append(raiz.valor)
        percurso_pre_order(raiz.left, resultado)
        percurso_pre_order(raiz.right, resultado)
    
    return resultado


def percurso_post_order(raiz, resultado=None):
    """Post-Order: Esquerda → Direita → Raiz."""
    if resultado is None:
        resultado = []
    
    if raiz is not None:
        percurso_post_order(raiz.left, resultado)
        percurso_post_order(raiz.right, resultado)
        resultado.append(raiz.valor)
    
    return resultado


def percurso_level_order(raiz):
    """Level-Order: Por nível (BFS com fila)."""
    if raiz is None:
        return []
    
    resultado = []
    fila = deque([raiz])
    
    while fila:
        no_atual = fila.popleft()
        resultado.append(no_atual.valor)
        
        if no_atual.left:
            fila.append(no_atual.left)
        if no_atual.right:
            fila.append(no_atual.right)
    
    return resultado


def percurso_level_order_por_nivel(raiz):
    """Level-Order separado por níveis."""
    if raiz is None:
        return []
    
    resultado = []
    fila = deque([raiz])
    
    while fila:
        nivel_atual = []
        tamanho_nivel = len(fila)
        
        for _ in range(tamanho_nivel):
            no = fila.popleft()
            nivel_atual.append(no.valor)
            
            if no.left:
                fila.append(no.left)
            if no.right:
                fila.append(no.right)
        
        resultado.append(nivel_atual)
    
    return resultado
