"""Visualização matplotlib da BST"""


def plotar_arvore(raiz, caminho_destacado=None):
    """Desenha BST com matplotlib destacando caminho de busca se fornecido."""
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches
    except ImportError as e:
        print(f"Erro ao importar matplotlib: {e}")
        print("Instale com: pip install matplotlib")
        return
    
    if raiz is None:
        print("Árvore vazia.")
        return
    
    if caminho_destacado is None:
        caminho_destacado = []
    
    positions = {}
    
    def altura_arvore(node):
        if node is None:
            return 0
        return 1 + max(altura_arvore(node.left), altura_arvore(node.right))
    
    def contar_nos(node):
        if node is None:
            return 0
        return 1 + contar_nos(node.left) + contar_nos(node.right)
    
    def verificar_balanceada(node):
        def verificar_altura(n):
            if n is None:
                return (True, -1)
            bal_esq, alt_esq = verificar_altura(n.left)
            if not bal_esq:
                return (False, 0)
            bal_dir, alt_dir = verificar_altura(n.right)
            if not bal_dir:
                return (False, 0)
            if abs(alt_esq - alt_dir) > 1:
                return (False, 0)
            return (True, 1 + max(alt_esq, alt_dir))
        balanceada, _ = verificar_altura(node)
        return balanceada
    
    counter = [0]
    def posicionar_nos(node, depth=0):
        if node is None:
            return
        posicionar_nos(node.left, depth + 1)
        positions[node] = (counter[0], -depth * 2)
        counter[0] += 2
        posicionar_nos(node.right, depth + 1)
    
    try:
        posicionar_nos(raiz)
    except Exception as e:
        print(f"Erro ao calcular posições: {e}")
        return
    
    altura = altura_arvore(raiz)
    tamanho = contar_nos(raiz)
    balanceada = verificar_balanceada(raiz)
    
    total_nos = len(positions)
    fig, ax = plt.subplots(figsize=(max(12, total_nos * 1.5), 8))
    
    for node, (x, y) in positions.items():
        if node.left:
            x2, y2 = positions[node.left]
            ax.plot([x, x2], [y, y2], 'k-', linewidth=2, zorder=1)
        if node.right:
            x2, y2 = positions[node.right]
            ax.plot([x, x2], [y, y2], 'k-', linewidth=2, zorder=1)
    
    for node, (x, y) in positions.items():
        if caminho_destacado and node.valor in caminho_destacado:
            if node.valor == caminho_destacado[-1]:
                color = 'lightgreen'
                edge_color = 'darkgreen'
                edge_width = 3
            else:
                color = 'yellow'
                edge_color = 'orange'
                edge_width = 3
        else:
            color = 'lightblue'
            edge_color = 'darkblue'
            edge_width = 2
        
        circle = patches.Circle((x, y), 0.4, facecolor=color, 
                               edgecolor=edge_color, linewidth=edge_width, zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, str(node.valor), ha='center', va='center', 
               fontsize=14, fontweight='bold', zorder=3)
    
    all_x = [pos[0] for pos in positions.values()]
    all_y = [pos[1] for pos in positions.values()]
    margin = 1.5
    ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
    ax.set_ylim(min(all_y) - margin, max(all_y) + margin)
    
    ax.set_aspect('equal')
    ax.axis('off')
    
    balanceada_str = "Sim" if balanceada else "Não"
    titulo = f'Árvore Binária de Busca (BST)\n'
    titulo += f'Altura: {altura} | Tamanho: {tamanho} nós | Balanceada: {balanceada_str}'
    
    if caminho_destacado:
        caminho_str = " → ".join(map(str, caminho_destacado))
        titulo += f'\nCaminho de Busca: {caminho_str}'
    
    plt.title(titulo, fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    
    try:
        plt.show()
    except Exception as e:
        print(f"\nNão foi possível exibir na tela. Salvando em arquivo...")
        arquivo_saida = 'arvore_bst.png'
        plt.savefig(arquivo_saida, dpi=150, bbox_inches='tight')
        print(f"✓ Árvore salva em: {arquivo_saida}")
        plt.close()
