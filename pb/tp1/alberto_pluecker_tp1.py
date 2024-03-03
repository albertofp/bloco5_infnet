from datetime import date
from datetime import datetime
from enum import Enum

class Urgencia(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3

class Tarefa:
    def __init__(self, descricao: str, prazo_final: str, urgencia: Urgencia, data_criacao = date.today().strftime('%Y-%m-%d')):
        self.descricao = descricao
        self.data_criacao = data_criacao,
        self.prazo_final = prazo_final
        self.urgencia= urgencia
        self.concluida = False

def adicionar_tarefa(lista_tarefas: list[Tarefa], descricao: str, prazo_final: str, urgencia: Urgencia):
    """
    Adiciona uma nova tarefa à lista de tarefas.

    Args:
        lista_tarefas (list): Lista de tarefas onde a nova tarefa será adicionada.
        descricao (str): Descrição da tarefa.
        prazo_final (str, opcional): Prazo final da tarefa (formato: YYYY-MM-DD).
        urgencia (str, opcional): Nível de urgência da tarefa.

    Returns:
        None
    """
    nova_tarefa: Tarefa = Tarefa(descricao, prazo_final, urgencia)
    lista_tarefas.append(nova_tarefa)

def listar_tarefas(lista_tarefas: list[Tarefa]):
    """
    Lista todas as tarefas pendentes na lista.

    Args:
        lista_tarefas (list): Lista de tarefas a serem listadas.

    Returns:
        None
    """
    print("Lista de Tarefas Pendentes:")
    for idx, tarefa in enumerate(lista_tarefas, start=1):
        if not tarefa.concluida:
            print(f"{idx}. Descrição: {tarefa.descricao}")
            print(f"   Data de Criação: {tarefa.data_criacao}")
            print(f"   Prazo Final: {tarefa.prazo_final}")
            print(f"   Urgência: {tarefa.urgencia.name if tarefa.urgencia else 'Não especificada'}")
            print("")

def marcar_tarefa_concluida(lista_tarefas: list[Tarefa], indice: int):
    """
    Marca uma tarefa específica como concluída.

    Args:
        lista_tarefas (list): Lista de tarefas onde a tarefa será marcada como concluída.
        indice (int): Índice da tarefa a ser marcada como concluída na lista.

    Returns:
        None
    """
    if 0 < indice <= len(lista_tarefas):
        lista_tarefas[indice-1].concluida = True
    else:
        print("Índice inválido!")

def remover_tarefa(lista_tarefas: list[Tarefa], indice: int):
    """
    Remove uma tarefa específica da lista.

    Args:
        lista_tarefas (list): Lista de tarefas onde a tarefa será removida.
        indice (int): Índice da tarefa a ser removida na lista.

    Returns:
        None
    """
    if 0 < indice <= len(lista_tarefas):
        del lista_tarefas[indice-1]
    else:
        print("Índice inválido!")

def main():
    tarefas = [
        Tarefa("Reunião de equipe", "2024-03-10", Urgencia.MEDIA),
        Tarefa("Preparar relatório mensal", "2024-03-12", Urgencia.ALTA),
        Tarefa("Enviar convites para o evento", "2024-03-08", Urgencia.ALTA),
        Tarefa("Revisar contrato com fornecedor", "2024-03-15", Urgencia.BAIXA),
        Tarefa("Treinamento de novos funcionários", "2024-03-05", Urgencia.MEDIA),
        Tarefa("Atualizar site da empresa", "2024-03-18", Urgencia.ALTA),
        Tarefa("Fazer compras para o escritório", "2024-03-07", Urgencia.MEDIA),
        Tarefa("Elaborar plano de marketing", "2024-03-14", Urgencia.ALTA),
        Tarefa("Conferir faturas pendentes", "2024-03-09", Urgencia.BAIXA),
        Tarefa("Resolver problemas de TI", "2024-03-11", Urgencia.ALTA)
    ]


    while True:
        print("\n=== Sistema de Gestão de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da tarefa: ")
            while True:
                prazo_final = input("Digite o prazo final da tarefa (formato: YYYY-MM-DD): ")
                try:
                    datetime.strptime(prazo_final, '%Y-%m-%d')
                    break
                except ValueError:
                    print("Formato inválido. Por favor, insira a data no formato YYYY-MM-DD.")
            urgencia = input("Digite o nível de urgência da tarefa: (1 - Baixa, 2 - Media, 3 - Alta)")
            if urgencia == '1':
                urgencia = Urgencia.BAIXA
            elif urgencia == '2':
                urgencia = Urgencia.MEDIA
            elif urgencia == '3':
                urgencia = Urgencia.ALTA
            else:
                urgencia = Urgencia.BAIXA
            
            adicionar_tarefa(tarefas, descricao, prazo_final, urgencia)
        elif escolha == '2':
            if tarefas:
                print("\n=== Tarefas Pendentes ===")
                listar_tarefas(tarefas)
            else:
                print("Não há tarefas pendentes.")
        elif escolha == '3':
            if tarefas:
                listar_tarefas(tarefas)
                indice = int(input("Digite o índice da tarefa a ser marcada como concluída: "))
                marcar_tarefa_concluida(tarefas, indice)
            else:
                print("Não há tarefas para marcar como concluídas.")
        elif escolha == '4':
            if tarefas:
                listar_tarefas(tarefas)
                indice = int(input("Digite o índice da tarefa a ser removida: "))
                remover_tarefa(tarefas, indice)
            else:
                print("Não há tarefas para remover.")
        elif escolha == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
