"""Operações de inserção na BST"""


def inserir_valor(raiz, valor):
    """Insere valor na BST mantendo propriedade ordenada."""
    if raiz is None:
        from funcoes.node import Node
        return (Node(valor), True, f"✓ Valor {valor} inserido com sucesso.")
    
    if raiz.valor == valor:
        return (raiz, False, f"✗ Valor {valor} já existe na árvore.")
    
    if valor < raiz.valor:
        raiz.left, sucesso, mensagem = inserir_valor(raiz.left, valor)
    else:
        raiz.right, sucesso, mensagem = inserir_valor(raiz.right, valor)
    
    return (raiz, sucesso, mensagem)


def inserir_multiplos(raiz, entrada):
    """Insere múltiplos valores separados por vírgula."""
    from funcoes.validacao import validar_entrada
    
    valores_str = entrada.split(',')
    mensagens = []
    sucessos = 0
    falhas = 0
    
    for valor_str in valores_str:
        valido, valor, msg_erro = validar_entrada(valor_str)
        
        if not valido:
            mensagens.append(f"✗ '{valor_str.strip()}': {msg_erro}")
            falhas += 1
            continue
        
        raiz, sucesso, mensagem = inserir_valor(raiz, valor)
        mensagens.append(mensagem)
        
        if sucesso:
            sucessos += 1
        else:
            falhas += 1
    
    relatorio = "\n".join(mensagens)
    relatorio += f"\n\nResumo: {sucessos} inserido(s), {falhas} falha(s)"
    
    return (raiz, relatorio)
