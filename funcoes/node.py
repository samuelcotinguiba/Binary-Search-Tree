"""Classe Node - Representa um nó da BST"""


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.valor < other.valor
    
    def __repr__(self):
        return f"Node(valor={self.valor})"
    
    def __str__(self):
        return str(self.valor)
