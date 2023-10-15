'''
Integrantes:
- Debora da Silva Amaral RM 550412
- Levy Nascimento Junior RM 98655
- Lívia Namba Seraphim RM 97819
- Mateus Iago Sousa Conceição RM 550270
- Sarah Ribeiro da Silva RM 97747
'''

# Definindo de uma vez
class Task:
    def __init__(self, start_date, end_date, completion_real, completion_planned, responsible, description):
        self.start_date = start_date
        self.end_date = end_date
        self.completion_real = completion_real
        self.completion_planned = completion_planned
        self.responsible = responsible
        self.description = description
        self.delay_plan = None  

class ProjectManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

 # Exibe as informações de cada tarefa na lista
    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"Task {i}:")
            print(f"Start Date: {task.start_date}")
            print(f"End Date: {task.end_date}")
            print(f"Completion Real: {task.completion_real}%")
            print(f"Completion Planned: {task.completion_planned}%")
            print(f"Responsible: {task.responsible}")
            print(f"Description: {task.description}")
            if task.delay_plan is not None:  #
                print(f"Delay Plan: {task.delay_plan}")
            print()

# Verificar atrasos nas tarefas e permitir a entrada de um plano de atraso
    def check_delays(self):
        for task in self.tasks:
            if task.completion_real < task.completion_planned:
                task.delay_plan = input(f"Plano de atraso para a tarefa: {task.description}: ")

def main():
    project_manager = ProjectManager()

    while True:
        print("Gerenciamento de Projeto - Escolha uma opção:")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Verificar Atrasos")
        print("4. Resumo da Operação")
        print("5. Encerrar o Programa")

        choice = input("Opção: ")

# Solicitar informações da tarefa e adicionar ao gerenciador de projeto
        if choice == "1":
            start_date = input("Data Inicial: ")
            end_date = input("Data Final: ")
            completion_real = float(input("% de Completude Real: ")) 
            completion_planned = float(input("% de Completude Planejada: "))  
            responsible = input("Responsável: ")
            description = input("Descrição: ")

            task = Task(start_date, end_date, completion_real, completion_planned, responsible, description)
            project_manager.add_task(task)
            print("Tarefa adicionada com sucesso!")

# Exibir as tarefas no gerenciador de projeto
        elif choice == "2":
            project_manager.view_tasks()

# Permite que o usuário adicione um plano de atraso para tarefas atrasadas
        elif choice == "3":
            project_manager.check_delays()

# Exibir resumo das operações
        elif choice == "4":
            print("Resumo da Operação:")
            print(f"Total de Tarefas: {len(project_manager.tasks)}")
            print("Tarefas com Atraso:")
            for task in project_manager.tasks:
                if task.completion_real < task.completion_planned:
                    print(f"- {task.description}")

        elif choice == "5":
            print("Encerrando o programa...")
            break

if __name__ == "__main__":
    main()
