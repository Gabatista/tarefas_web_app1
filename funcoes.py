ARQUIVO = "a_fazer.txt"

def get_tarefas(arquivo=ARQUIVO):
    with open(arquivo, 'r') as arq_local:
        tarefas_local = arq_local.readlines()
    return tarefas_local

def write_tarefas(tarefas, arquivo=ARQUIVO):
    with open(arquivo, 'w') as arq:
        arq.writelines(tarefas)

if __name__ == '__main__':
    print(get_tarefas())
