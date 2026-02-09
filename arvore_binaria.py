"""
Árvore Binária de Busca (BST) - Menu Interativo
Projeto educacional - Estrutura de Dados
Salvamento automático ativado
"""

import os
import runpy
import atexit

funcoes_dir = os.path.join(os.path.dirname(__file__), 'funcoes')

_node = runpy.run_path(os.path.join(funcoes_dir, 'node.py'))
Node = _node['Node']

_validacao = runpy.run_path(os.path.join(funcoes_dir, 'validacao.py'))
validar_entrada = _validacao['validar_entrada']

_inserir = runpy.run_path(os.path.join(funcoes_dir, 'inserir.py'))
inserir_valor = _inserir['inserir_valor']
inserir_multiplos = _inserir['inserir_multiplos']

_buscar = runpy.run_path(os.path.join(funcoes_dir, 'buscar.py'))
buscar = _buscar['buscar']

_remover = runpy.run_path(os.path.join(funcoes_dir, 'remover.py'))
remover = _remover['remover']

_aux = runpy.run_path(os.path.join(funcoes_dir, 'operacoes_auxiliares.py'))
encontrar_minimo = _aux['encontrar_minimo']
encontrar_maximo = _aux['encontrar_maximo']
calcular_altura = _aux['calcular_altura']
contar_nos = _aux['contar_nos']
verificar_balanceada = _aux['verificar_balanceada']

_percursos = runpy.run_path(os.path.join(funcoes_dir, 'percursos.py'))
percurso_in_order = _percursos['percurso_in_order']
percurso_pre_order = _percursos['percurso_pre_order']
percurso_post_order = _percursos['percurso_post_order']
percurso_level_order = _percursos['percurso_level_order']
percurso_level_order_por_nivel = _percursos['percurso_level_order_por_nivel']

_salvar = runpy.run_path(os.path.join(funcoes_dir, 'salvar_carregar_arvore.py'))
salvar_json = _salvar['salvar_json']
carregar_json = _salvar['carregar_json']
listar_arvores = _salvar['listar_arvores']

_plotar = runpy.run_path(os.path.join(funcoes_dir, 'plotar_arvore.py'))
plotar_arvore = _plotar['plotar_arvore']

arvore_atual = None
ARQUIVO_AUTO_SAVE = "_auto_save_"


def limpar_tela():
    os.system('clear' if os.name != 'nt' else 'cls')


def salvar_automatico():
    """Salva árvore automaticamente ao sair."""
    if arvore_atual is not None:
        salvar_json(arvore_atual, ARQUIVO_AUTO_SAVE)
        print("💾 Árvore salva automaticamente.")


def carregar_automatico():
    """Carrega árvore automaticamente ao iniciar."""
    global arvore_atual
    raiz, sucesso, _ = carregar_json(ARQUIVO_AUTO_SAVE)
    if sucesso:
        arvore_atual = raiz
        return True
    return False


def exibir_menu():
    print("\n" + "="*50)
    print(" BST - ÁRVORE BINÁRIA DE BUSCA ".center(50))
    print("="*50)
    print("\n1. Inserir")
    print("2. Buscar")
    print("3. Remover")
    print("4. Visualizar")
    print("5. Info")
    print("6. Gerenciar")
    print("0. Sair")
    print("="*50)


def menu_inserir():
    global arvore_atual
    entrada = input("\nValor(es) [ex: 42 ou 50,30,70]: ").strip()
    
    if not entrada:
        print("✗ Entrada vazia.")
        return
    
    if ',' in entrada:
        arvore_atual, relatorio = inserir_multiplos(arvore_atual, entrada)
        print("\n" + relatorio)
    else:
        valido, valor, msg_erro = validar_entrada(entrada)
        if not valido:
            print(f"\n{msg_erro}")
            return
        arvore_atual, sucesso, mensagem = inserir_valor(arvore_atual, valor)
        print(f"\n{mensagem}")


def menu_buscar():
    global arvore_atual
    if arvore_atual is None:
        print("\n✗ Árvore vazia.")
        return
    
    entrada = input("\nValor a buscar: ").strip()
    valido, valor, msg_erro = validar_entrada(entrada)
    if not valido:
        print(f"\n{msg_erro}")
        return
    
    encontrado, caminho, mensagem = buscar(arvore_atual, valor)
    print(f"\n{mensagem}")
    
    if caminho:
        visualizar = input("\nVisualizar com destaque? (s/n): ").lower()
        if visualizar == 's':
            try:
                plotar_arvore(arvore_atual, caminho)
            except Exception as e:
                print(f"Erro: {e}")


def menu_remover():
    global arvore_atual
    if arvore_atual is None:
        print("\n✗ Árvore vazia.")
        return
    
    entrada = input("\nValor a remover: ").strip()
    valido, valor, msg_erro = validar_entrada(entrada)
    if not valido:
        print(f"\n{msg_erro}")
        return
    
    arvore_atual, sucesso, mensagem = remover(arvore_atual, valor)
    print(f"\n{mensagem}")


def menu_visualizar():
    if arvore_atual is None:
        print("\n✗ Árvore vazia.")
        return
    
    try:
        plotar_arvore(arvore_atual)
    except Exception as e:
        print(f"Erro: {e}")


def menu_info():
    """Exibe percursos e estatísticas."""
    if arvore_atual is None:
        print("\n✗ Árvore vazia.")
        return
    
    minimo = encontrar_minimo(arvore_atual)
    maximo = encontrar_maximo(arvore_atual)
    altura = calcular_altura(arvore_atual)
    tamanho = contar_nos(arvore_atual)
    balanceada, msg_balance = verificar_balanceada(arvore_atual)
    
    print("\n" + "-"*50)
    print("📊 INFORMAÇÕES DA ÁRVORE")
    print("-"*50)
    print(f"Tamanho: {tamanho} | Altura: {altura}")
    print(f"Mínimo: {minimo} | Máximo: {maximo}")
    print(f"{msg_balance}")
    
    print("\n📋 PERCURSOS:")
    print(f"In-Order: {percurso_in_order(arvore_atual)}")
    print(f"Level-Order: {percurso_level_order(arvore_atual)}")


def menu_gerenciar():
    """Menu para salvar/carregar/limpar árvores."""
    global arvore_atual
    
    print("\n" + "-"*50)
    print("💾 GERENCIAMENTO")
    print("-"*50)
    print("1. Salvar com nome")
    print("2. Carregar árvore")
    print("3. Listar salvas")
    print("4. Limpar atual")
    print("0. Voltar")
    
    sub_opcao = input("\nOpção: ").strip()
    
    match sub_opcao:
        case '1':
            if arvore_atual is None:
                print("\n✗ Árvore vazia.")
                return
            nome = input("\nNome: ").strip()
            if nome:
                sucesso, mensagem = salvar_json(arvore_atual, nome)
                print(f"\n{mensagem}")
        
        case '2':
            arvores, _, msg = listar_arvores()
            if not arvores:
                print(f"\n{msg}")
                return
            
            print(f"\n{msg}")
            for arv in arvores:
                if not arv['nome'].startswith('_'):
                    print(f"  - {arv['nome']}")
            
            nome = input("\nNome: ").strip()
            if nome:
                nova_raiz, sucesso, mensagem = carregar_json(nome)
                if sucesso:
                    arvore_atual = nova_raiz
                print(f"\n{mensagem}")
        
        case '3':
            arvores, _, msg = listar_arvores()
            print(f"\n{msg}")
            if arvores:
                for arv in arvores:
                    if not arv['nome'].startswith('_'):
                        print(f"  - {arv['nome']} ({arv['data']})")
        
        case '4':
            if arvore_atual is None:
                print("\n✗ Já vazia.")
            else:
                confirmar = input("\n  Limpar? (s/n): ").lower()
                if confirmar == 's':
                    arvore_atual = None
                    print("✓ Limpa.")


def main():
    global arvore_atual
    
    # Registra salvamento automático ao sair
    atexit.register(salvar_automatico)
    
    # Carrega árvore anterior se existir
    if carregar_automatico():
        print("💾 Árvore anterior carregada automaticamente.")
        input("Pressione ENTER...")
    
    while True:
        limpar_tela()
        
        # Status
        if arvore_atual is None:
            print("📍 Árvore vazia")
        else:
            tamanho = contar_nos(arvore_atual)
            altura = calcular_altura(arvore_atual)
            valores = percurso_in_order(arvore_atual)
            print(f"📍 {tamanho} nó(s) | Altura: {altura}")
            print(f"Valores: {valores[:10]}{' ...' if len(valores) > 10 else ''}")
        
        exibir_menu()
        opcao = input("\n→ ").strip()
        
        match opcao:
            case '1':
                menu_inserir()
            case '2':
                menu_buscar()
            case '3':
                menu_remover()
            case '4':
                menu_visualizar()
            case '5':
                menu_info()
            case '6':
                menu_gerenciar()
            case '0':
                print("\n👋 Salvando e saindo...\n")
                break
            case _:
                print("\n✗ Opção inválida.")
        
        input("\n⏎ ENTER...")


if __name__ == "__main__":
    main()
