"""Operações de busca na BST"""


def buscar(raiz, valor, caminho=None):
    """Busca valor na BST e retorna caminho percorrido."""
    if caminho is None:
        caminho = []
    
    if raiz is None:
        if not caminho:
            mensagem = f"✗ Valor {valor} não encontrado. Árvore vazia."
        else:
            caminho_str = " → ".join(map(str, caminho))
            mensagem = f"✗ Valor {valor} não encontrado. Caminho percorrido: {caminho_str}"
        return (False, caminho, mensagem)
    
    caminho.append(raiz.valor)
    
    if raiz.valor == valor:
        caminho_str = " → ".join(map(str, caminho))
        mensagem = f"✓ Valor {valor} encontrado! Caminho: {caminho_str}"
        return (True, caminho, mensagem)
    
    if valor < raiz.valor:
        return buscar(raiz.left, valor, caminho)
    else:
        return buscar(raiz.right, valor, caminho)
