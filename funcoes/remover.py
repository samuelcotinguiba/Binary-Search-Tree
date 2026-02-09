"""Operações de remoção na BST"""


def encontrar_minimo_no(raiz):
    """Encontra o nó com menor valor (mais à esquerda)."""
    atual = raiz
    while atual.left is not None:
        atual = atual.left
    return atual


def remover(raiz, valor):
    """
    Remove valor da BST mantendo propriedade ordenada.
    Três casos: sem filhos, um filho, dois filhos.
    """
    if raiz is None:
        return (None, False, f"✗ Valor {valor} não encontrado na árvore.")
    
    if valor < raiz.valor:
        raiz.left, sucesso, mensagem = remover(raiz.left, valor)
        return (raiz, sucesso, mensagem)
    
    elif valor > raiz.valor:
        raiz.right, sucesso, mensagem = remover(raiz.right, valor)
        return (raiz, sucesso, mensagem)
    
    else:
        # Caso 1: Nó folha (sem filhos)
        if raiz.left is None and raiz.right is None:
            return (None, True, f"✓ Valor {valor} removido.")
        
        # Caso 2: Apenas filho direito
        elif raiz.left is None:
            return (raiz.right, True, f"✓ Valor {valor} removido.")
        
        # Caso 3: Apenas filho esquerdo
        elif raiz.right is None:
            return (raiz.left, True, f"✓ Valor {valor} removido.")
        
        # Caso 4: Dois filhos - substitui pelo sucessor
        else:
            sucessor = encontrar_minimo_no(raiz.right)
            raiz.valor = sucessor.valor
            raiz.right, _, _ = remover(raiz.right, sucessor.valor)
            return (raiz, True, f"✓ Valor {valor} removido.")
