###################################################################################
#                                   Médicos                                       #
###################################################################################

def submenu_medicos():
    print()
    print("##### Submenu de Médicos #####")
    print()
    print("1 - Listar todos os médicos")
    print("2 - Listar um médico específico")
    print("3 - Incluir novo médico")
    print("4 - Alterar informação de um médico")
    print("5 - Excluir médico")
    print("6 - Voltar")
    print()
    
    op_medico = int(input("Digite o número da opção desejada: "))
    
    while op_medico < 1 or op_medico > 6:
        op_medico = int(input("Digite o número da opção desejada: "))
    
    if op_medico == 1:
        dados = ler_medicos()
        listar_medicos(dados)
    elif op_medico == 2:
        listar_medico_esp()
    elif op_medico == 3:
        incluir_medico()
    elif op_medico == 4:
        alterar_medico()
    elif op_medico == 5:
        excluir_medico()
    else:
        menu_opcoes()
        
def listar_medicos(medicos):
    print("##### Lista de Médicos #####")
    print()
    for i in range(len(medicos)):
        print(f'CRM: {medicos[i][0]}')
        print(f'Nome: {medicos[i][1]}')
        print(f'Data de nascimento: {medicos[i][2]}')
        print(f'Sexo: {medicos[i][3]}')
        print(f'Especialidade: {medicos[i][4]}')
        print(f'Formado: {medicos[i][5]}')
        
        print(f'E-mails: ', end='')
        for j in range(len(medicos[i][6])):
            if j == len(medicos[i][6])-1:
                print(f'{medicos[i][6][j]}')
            else:
                print(f'{medicos[i][6][j]}', end=', ')
                
        print(f'Telefones: ', end='')
        for j in range(len(medicos[i][7])):
            if j == len(medicos[i][7])-1:
                print(f'{medicos[i][7][j]}')
            else:
                print(f'{medicos[i][7][j]}', end=', ')
        print()
    
    menu_opcoes()
    
###################################################################################
#                                   Pacientes                                     #
###################################################################################
    
def submenu_pacientes():
    print()
    print("##### Submenu de Pacientes #####")
    print()
    print("1 - Listar todos os pacientes")
    print("2 - Listar um paciente específico")
    print("3 - Incluir novo paciente")
    print("4 - Alterar informação de um paciente")
    print("5 - Excluir paciente")
    print("6 - Voltar")
    print()
    
    op_paciente = int(input("Digite o número da opção desejada: "))
    
    while op_paciente < 1 or op_paciente > 6:
        op_paciente = int(input("Digite o número da opção desejada: "))
    
    if op_paciente == 1:
        listar_pacientes()
    elif op_paciente == 2:
        listar_paciente_esp()
    elif op_paciente == 3:
        incluir_paciente()
    elif op_paciente == 4:
        alterar_paciente()
    elif op_paciente == 5:
        excluir_paciente()
    else:
        menu_opcoes()

###################################################################################
#                                   Consultas                                     #
###################################################################################

def submenu_consultas():
    print()
    print("##### Submenu de Consultas #####")
    print()
    print("1 - Listar todos as consultas")
    print("2 - Listar uma consulta específica")
    print("3 - Incluir nova consulta")
    print("4 - Alterar informação de uma consulta")
    print("5 - Excluir consulta")
    print("6 - Voltar")
    print()
    
    op_consulta = int(input("Digite o número da opção desejada: "))
    
    while op_consulta < 1 or op_consulta > 6:
        op_consulta = int(input("Digite o número da opção desejada: "))
    
    if op_consulta == 1:
        listar_consultas()
    elif op_consulta == 2:
        listar_consul_esp()
    elif op_consulta == 3:
        incluir_consulta()
    elif op_consulta == 4:
        alterar_consulta()
    elif op_consulta == 5:
        excluir_consulta()
    else:
        menu_opcoes()
        
###################################################################################
#                                   Relatórios                                    #
###################################################################################

def submenu_relatorios():
    print()
    print("##### Submenu de Relátorios #####")
    print()
    print("1 - Listar todos os relatórios")
    print("2 - Listar um relatório específico")
    print("3 - Incluir novo relatório")
    print("4 - Alterar informação de um relatório")
    print("5 - Excluir relatório")
    print("6 - Voltar")
    print()
    
    op_relatorio = int(input("Digite o número da opção desejada: "))
    
    while op_relatorio < 1 or op_relatorio > 6:
        op_relatorio = int(input("Digite o número da opção desejada: "))
    
    if op_relatorio == 1:
        listar_pacientes()
    elif op_relatorio == 2:
        listar_paciente_esp()
    elif op_relatorio == 3:
        incluir_paciente()
    elif op_relatorio == 4:
        alterar_paciente()
    elif op_relatorio == 5:
        excluir_paciente()
    else:
        menu_opcoes()
        
###################################################################################
#                                    Ler dados                                    #
###################################################################################

def ler_medicos():
    
    medicos = []
    
    ref_arq = open("Projeto_hospital/medicos.txt", "r", encoding="utf-8")
    
    for linha in ref_arq:
        lista = linha.split(";")
        medico = []
        
        emails = lista[6].split("|")
        
        telefones = lista[7].split("|")
        
        for i in range(len(telefones)):
            if i == len(telefones)-1:
                telefones[i] = telefones[i][:-1]
        
        for i in range(len(lista)-2):
            medico.append(lista[i])
        
        medico.append(emails)
        medico.append(telefones)
        medicos.append(medico)
    
    return medicos
            
        
        
    
###################################################################################
#                                  Menu de Opções                                 #
###################################################################################

def menu_opcoes():
    print()
    print("##### Menu de Opções #####")
    print()
    print("1 - Submenu de Médicos")
    print("2 - Submenu de Pacientes")
    print("3 - Submenu de Consultas")
    print("4 - Submenu de Relátorios")
    print("5 - Sair")
    print()

    op=int(input("Insira um número para acessar os menus abaixo: "))
    while op <1 or op >6:
        op=int(input("Digite o número da opção desejada: "))

    if op==1:
        submenu_medicos()
    elif op==2:
        submenu_pacientes()
    elif op==3:
        submenu_consultas()
    elif op==4:
        submenu_relatorios()
    elif op==5:
        print("Obrigado por usar o sistema")
        print("encerrando")


def main():
    menu_opcoes()

###################################################################################
#                                 Código Principal                                #
###################################################################################

print("Início")
print()

main()

print()
print("Fim")