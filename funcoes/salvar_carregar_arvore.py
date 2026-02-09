"""Persistência JSON para BST"""

import json
import os
from datetime import datetime


def serializar_arvore(raiz):
    """Converte Node para dicionário."""
    if raiz is None:
        return None
    
    return {
        "valor": raiz.valor,
        "left": serializar_arvore(raiz.left),
        "right": serializar_arvore(raiz.right)
    }


def desserializar_arvore(dados):
    """Converte dicionário para Node."""
    if dados is None:
        return None
    
    from funcoes.node import Node
    
    raiz = Node(dados["valor"])
    raiz.left = desserializar_arvore(dados.get("left"))
    raiz.right = desserializar_arvore(dados.get("right"))
    
    return raiz


def salvar_json(raiz, nome_arvore, arquivo="arvores_bst.json"):
    """Salva árvore no arquivo JSON."""
    try:
        if os.path.exists(arquivo):
            with open(arquivo, 'r', encoding='utf-8') as f:
                arvores = json.load(f)
        else:
            arvores = []
        
        for i, arvore in enumerate(arvores):
            if arvore.get("nome") == nome_arvore:
                arvores[i] = {
                    "nome": nome_arvore,
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "raiz": serializar_arvore(raiz)
                }
                break
        else:
            arvores.append({
                "nome": nome_arvore,
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "raiz": serializar_arvore(raiz)
            })
        
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(arvores, f, indent=2, ensure_ascii=False)
        
        return (True, f"✓ Árvore '{nome_arvore}' salva com sucesso!")
    
    except Exception as e:
        return (False, f"✗ Erro ao salvar árvore: {e}")


def carregar_json(nome_arvore, arquivo="arvores_bst.json"):
    """Carrega árvore do arquivo JSON."""
    try:
        if not os.path.exists(arquivo):
            return (None, False, f"✗ Arquivo '{arquivo}' não encontrado.")
        
        with open(arquivo, 'r', encoding='utf-8') as f:
            arvores = json.load(f)
        
        for arvore in arvores:
            if arvore.get("nome") == nome_arvore:
                raiz = desserializar_arvore(arvore.get("raiz"))
                data = arvore.get("data", "data desconhecida")
                return (raiz, True, f"✓ Árvore '{nome_arvore}' carregada! (salva em {data})")
        
        return (None, False, f"✗ Árvore '{nome_arvore}' não encontrada.")
    
    except Exception as e:
        return (None, False, f"✗ Erro ao carregar árvore: {e}")


def listar_arvores(arquivo="arvores_bst.json"):
    """Lista todas as árvores salvas."""
    try:
        if not os.path.exists(arquivo):
            return ([], True, "Nenhuma árvore salva ainda.")
        
        with open(arquivo, 'r', encoding='utf-8') as f:
            arvores = json.load(f)
        
        if not arvores:
            return ([], True, "Nenhuma árvore salva ainda.")
        
        info_arvores = []
        for arv in arvores:
            info_arvores.append({
                "nome": arv.get("nome", "sem nome"),
                "data": arv.get("data", "data desconhecida")
            })
        
        return (info_arvores, True, f"{len(arvores)} árvore(s) encontrada(s).")
    
    except Exception as e:
        return ([], False, f"✗ Erro ao listar árvores: {e}")
