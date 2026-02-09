"""Operações auxiliares da BST"""


def encontrar_minimo(raiz):
    """Encontra o menor valor (nó mais à esquerda)."""
    if raiz is None:
        return None
    
    atual = raiz
    while atual.left is not None:
        atual = atual.left
    
    return atual.valor


def encontrar_maximo(raiz):
    """Encontra o maior valor (nó mais à direita)."""
    if raiz is None:
        return None
    
    atual = raiz
    while atual.right is not None:
        atual = atual.right
    
    return atual.valor


def calcular_altura(raiz):
    """Calcula altura da árvore."""
    if raiz is None:
        return -1
    
    altura_esquerda = calcular_altura(raiz.left)
    altura_direita = calcular_altura(raiz.right)
    
    return 1 + max(altura_esquerda, altura_direita)


def contar_nos(raiz):
    """Conta total de nós na árvore."""
    if raiz is None:
        return 0
    
    return 1 + contar_nos(raiz.left) + contar_nos(raiz.right)


def verificar_balanceada(raiz):
    """Verifica se árvore está balanceada (diferença de altura ≤ 1)."""
    def verificar_altura(node):
        if node is None:
            return (True, -1)
        
        balanceada_esq, altura_esq = verificar_altura(node.left)
        if not balanceada_esq:
            return (False, 0)
        
        balanceada_dir, altura_dir = verificar_altura(node.right)
        if not balanceada_dir:
            return (False, 0)
        
        diferenca = abs(altura_esq - altura_dir)
        
        if diferenca > 1:
            return (False, 0)
        
        altura_atual = 1 + max(altura_esq, altura_dir)
        return (True, altura_atual)
    
    balanceada, _ = verificar_altura(raiz)
    
    if balanceada:
        return (True, "✓ Árvore balanceada.")
    else:
        return (False, "✗ Árvore NÃO balanceada.")
