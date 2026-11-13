import os
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

    dados = ler_medicos()

    if op_medico == 1:
        listar_medicos(dados)
    elif op_medico == 2:
        listar_medico_esp(dados)
    elif op_medico == 3:
        incluir_medico(dados)
    elif op_medico == 4:
        alterar_medico(dados)
    elif op_medico == 5:
        excluir_medico(dados)
    else:
        menu_opcoes()

######################### Listar Médicos #############################

def listar_medicos(medicos):
    print("##### Lista de Médicos #####")
    print()

    for i in range(len(medicos)):
        print(f"CRM: {medicos[i][0]}")
        print(f"Nome: {medicos[i][1]}")
        print(f"Data de nascimento: {medicos[i][2]}")
        print(f"Sexo: {medicos[i][3]}")
        print(f"Especialidade: {medicos[i][4]}")
        print(f"Formado: {medicos[i][5]}")

        print("E-mails: ", end="")
        for j in range(len(medicos[i][6])):
            if j == len(medicos[i][6]) - 1:
                print(f"{medicos[i][6][j]}")
            else:
                print(f"{medicos[i][6][j]}", end=", ")

        print("Telefones: ", end="")
        for j in range(len(medicos[i][7])):
            if j == len(medicos[i][7]) - 1:
                print(f"{medicos[i][7][j]}")
            else:
                print(f"{medicos[i][7][j]}", end=", ")

        print()

    menu_opcoes()

######################### Listar Médico Específico #############################

def listar_medico_esp(medicos):
    print("##### Listar um médico específico #####")
    print()

    med = input("Digite o CRM do médico: ")
    achou = False

    for i in range(len(medicos)):
        if med == medicos[i][0]:
            achou = True

            print(f"CRM: {medicos[i][0]}")
            print(f"Nome: {medicos[i][1]}")
            print(f"Data de nascimento: {medicos[i][2]}")
            print(f"Sexo: {medicos[i][3]}")
            print(f"Especialidade: {medicos[i][4]}")
            print(f"Formado: {medicos[i][5]}")

            print("E-mails: ", end="")
            for j in range(len(medicos[i][6])):
                if j == len(medicos[i][6]) - 1:
                    print(f"{medicos[i][6][j]}")
                else:
                    print(f"{medicos[i][6][j]}", end=", ")

            print("Telefones: ", end="")
            for j in range(len(medicos[i][7])):
                if j == len(medicos[i][7]) - 1:
                    print(f"{medicos[i][7][j]}")
                else:
                    print(f"{medicos[i][7][j]}", end=", ")

            print()

    if achou == False:
        print("Médico não encontrado")

    menu_opcoes()

######################### Incluir Novo Médico #############################

def incluir_medico(medicos):
    novo_medico = input("Digite o CRM do novo médico: ").strip()
    
    while novo_medico == "":
        print()
        print("Esse campo é obrigatório!")
        novo_medico = input("Digite o CRM do novo médico (UFxxxxxx): ").strip()
    
    achou = False

    for i in range(len(medicos)):
        if novo_medico == medicos[i][0]:
            achou = True

    if achou:
        print("Esse CRM já está cadastrado.")
    else:
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        sexo = input("Sexo (F/M): ")
        especialidade = input("Especialidade: ")
        formado = input("Formado: ")

        n_emails = int(input("Quantos e-mails deseja informar? "))
        emails = []

        print("Digite o(s) e-mail(s): ")
        for i in range(n_emails):
            email = input()
            emails.append(email)

        n_tel = int(input("Quantos telefones deseja informar? "))
        telefones = []

        print("Digite o(s) telefone(s) (só números): ")
        for i in range(n_tel):
            tel = input()
            tel = f'({tel[:2]}) {tel[2:7]}-{tel[7:]}'
            telefones.append(tel)

        #Montando Linha
        emails_formatados = "|".join(emails)
        telefones_formatados = "|".join(telefones)

        linha = f"{novo_medico};{nome};{data_nascimento};{sexo};{especialidade};{formado};{emails_formatados};{telefones_formatados}\n"

        ref_arq = open("medicos.txt", "a", encoding="utf-8")
        ref_arq.write(linha)
        ref_arq.close()

        print()
        print("Médico cadastrado com sucesso!")
    
    menu_opcoes()
    
######################### Alterar Médico #############################
        
def alterar_medico(medicos):
    alt_medico = input("Digite o CRM do médico a ser alterado: ")
    
    achou = False
    pos = 0

    for i in range(len(medicos)):
        if alt_medico == medicos[i][0]:
            achou = True
            pos = i

    if achou:
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        sexo = input("Sexo (F/M): ")
        especialidade = input("Especialidade: ")
        formado = input("Formado: ")

        n_emails = int(input("Quantos e-mails deseja informar? "))
        emails = []

        print("Digite o(s) e-mail(s): ")
        for i in range(n_emails):
            email = input()
            emails.append(email)

        n_tel = int(input("Quantos telefones deseja informar? "))
        telefones = []

        print("Digite o(s) telefone(s) (só números): ")
        for i in range(n_tel):
            tel = input()
            tel = f'({tel[:2]}) {tel[2:7]}-{tel[7:]}'
            telefones.append(tel)
            
        medicos[pos] = [alt_medico, nome, data_nascimento, sexo, especialidade, formado, emails, telefones]

        ref_arq = open("medicos.txt", "w", encoding="utf-8")
        
        #Montando Linhas a Serem Gravadas
        for i in range(len(medicos)):
            emails_formatados = "|".join(medicos[i][6])
            telefones_formatados = "|".join(medicos[i][7])
            linha = f'{medicos[i][0]};{medicos[i][1]};{medicos[i][2]};{medicos[i][3]};{medicos[i][4]};{medicos[i][5]};{emails_formatados};{telefones_formatados}\n'
            ref_arq.write(linha)
            
        ref_arq.close()

        print("Médico alterado com sucesso!")
    else:
        print("Médico não cadastrado!")
    
    menu_opcoes()

######################### Excluir Médico #############################

def excluir_medico(medicos):
    exc_medico = input("Digite o CRM do médico a ser excluído: ")
    
    achou = False
    pos = 0

    for i in range(len(medicos)):
        if exc_medico == medicos[i][0]:
            achou = True
            pos = i

    if achou:
        ref_arq = open("medicos.txt", "w", encoding="utf-8")
        
        #Montando Linhas a Serem Gravadas
        for i in range(len(medicos)):
            if i != pos:
                emails_formatados = "|".join(medicos[i][6])
                telefones_formatados = "|".join(medicos[i][7])
                linha = f'{medicos[i][0]};{medicos[i][1]};{medicos[i][2]};{medicos[i][3]};{medicos[i][4]};{medicos[i][5]};{emails_formatados};{telefones_formatados}\n'
                ref_arq.write(linha)
            
        ref_arq.close()

        print("Médico excluido com sucesso!")
    else:
        print("Médico não cadastrado!")
    
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

    dados = ler_pacientes()

    if op_paciente == 1:
        listar_pacientes(dados)
    elif op_paciente == 2:
        listar_paciente_esp(dados)
    elif op_paciente == 3:
        incluir_paciente(dados)
    elif op_paciente == 4:
        alterar_paciente(dados)
    elif op_paciente == 5:
        excluir_paciente(dados)
    else:
        menu_opcoes()


######################### Listar Pacientes #############################

def listar_pacientes(pacientes):
    print("##### Lista de Pacientes #####")
    print()

    for i in range(len(pacientes)):
        print(f"CPF: {pacientes[i][0]}")
        print(f"Nome: {pacientes[i][1]}")
        print(f"Data de nascimento: {pacientes[i][2]}")
        print(f"Sexo: {pacientes[i][3]}")
        print(f"Plano: {pacientes[i][4]}")

        print("E-mails: ", end="")
        for j in range(len(pacientes[i][5])):
            if j == len(pacientes[i][5]) - 1:
                print(f"{pacientes[i][5][j]}")
            else:
                print(f"{pacientes[i][5][j]}", end=", ")

        print("Telefones: ", end="")
        for j in range(len(pacientes[i][6])):
            if j == len(pacientes[i][6]) - 1:
                print(f"{pacientes[i][6][j]}")
            else:
                print(f"{pacientes[i][6][j]}", end=", ")

        print()

    menu_opcoes()
    
######################### Listar Paciente Específico #############################
    
def listar_paciente_esp(pacientes):
    print("##### Listar um paciente específico #####")
    print()
    
    pac = input("Digite o CPF do paciente (apenas números): ").strip()
    pac = f'{pac[:3]}.{pac[3:6]}.{pac[6:9]}-{pac[9:]}'
    achou = False

    for i in range(len(pacientes)):
        if pac == pacientes[i][0]:
            achou = True

            print(f"CRM: {pacientes[i][0]}")
            print(f"Nome: {pacientes[i][1]}")
            print(f"Data de nascimento: {pacientes[i][2]}")
            print(f"Sexo: {pacientes[i][3]}")
            print(f"Plano: {pacientes[i][4]}")

            print("E-mails: ", end="")
            for j in range(len(pacientes[i][5])):
                if j == len(pacientes[i][5]) - 1:
                    print(f"{pacientes[i][5][j]}")
                else:
                    print(f"{pacientes[i][5][j]}", end=", ")

            print("Telefones: ", end="")
            for j in range(len(pacientes[i][6])):
                if j == len(pacientes[i][6]) - 1:
                    print(f"{pacientes[i][6][j]}")
                else:
                    print(f"{pacientes[i][6][j]}", end=", ")

            print()

    if achou == False:
        print("Paciente não encontrado")

    menu_opcoes()

######################### Incluir Paciente #############################

def incluir_paciente(pacientes):
    novo_pac = input("Digite o CPF do novo médico: ").strip()
    
    while novo_pac == "":
        print()
        print("Esse campo é obrigatório!")
        novo_pac = input("Digite o CRM do novo médico (UFxxxxxx): ").strip()
    
    achou = False

    for i in range(len(pacientes)):
        if novo_pac == pacientes[i][0]:
            achou = True

    if achou:
        print("Esse CPF já está cadastrado.")
    else:
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        sexo = input("Sexo (F/M): ")
        plano = input("Plano: ")

        n_emails = int(input("Quantos e-mails deseja informar? "))
        emails = []

        print("Digite o(s) e-mail(s): ")
        for i in range(n_emails):
            email = input()
            emails.append(email)

        n_tel = int(input("Quantos telefones deseja informar? "))
        telefones = []

        print("Digite o(s) telefone(s) (só números): ")
        for i in range(n_tel):
            tel = input()
            tel = f'({tel[:2]}) {tel[2:7]}-{tel[7:]}'
            telefones.append(tel)

        #Montando Linha
        emails_formatados = "|".join(emails)
        telefones_formatados = "|".join(telefones)

        linha = f"{novo_pac};{nome};{data_nascimento};{sexo};{plano};{emails_formatados};{telefones_formatados}\n"

        ref_arq = open("pacientes.txt", "a", encoding="utf-8")
        ref_arq.write(linha)
        ref_arq.close()

        print()
        print("Paciente cadastrado com sucesso!")
    
    menu_opcoes()

######################### Alterar Paciente #############################
        
def alterar_paciente(pacientes):
    alt_pac = input("Digite o CRM do médico a ser alterado: ")
    
    achou = False
    pos = 0

    for i in range(len(pacientes)):
        if alt_pac == pacientes[i][0]:
            achou = True
            pos = i

    if achou:
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        sexo = input("Sexo (F/M): ")
        plano = input("Especialidade: ")

        n_emails = int(input("Quantos e-mails deseja informar? "))
        emails = []

        print("Digite o(s) e-mail(s): ")
        for i in range(n_emails):
            email = input()
            emails.append(email)

        n_tel = int(input("Quantos telefones deseja informar? "))
        telefones = []

        print("Digite o(s) telefone(s) (só números): ")
        for i in range(n_tel):
            tel = input()
            tel = f'({tel[:2]}) {tel[2:7]}-{tel[7:]}'
            telefones.append(tel)
            
        pacientes[pos] = [alt_pac, nome, data_nascimento, sexo, plano, emails, telefones]

        ref_arq = open("pacientes.txt", "w", encoding="utf-8")
        
        #Montando Linhas a Serem Gravadas
        for i in range(len(pacientes)):
            emails_formatados = "|".join(pacientes[i][5])
            telefones_formatados = "|".join(pacientes[i][6])
            linha = f'{pacientes[i][0]};{pacientes[i][1]};{pacientes[i][2]};{pacientes[i][3]};{pacientes[i][4]};{emails_formatados};{telefones_formatados}\n'
            ref_arq.write(linha)
            
        ref_arq.close()

        print("Paciente alterado com sucesso!")
    else:
        print("Paciente não cadastrado!")
    
    menu_opcoes()

######################### Excluir Paciente #############################

def excluir_paciente(pacientes):
    excluir_paciente = input("Digite o CPF do médico a ser excluído: ")
    
    achou = False
    pos = 0

    for i in range(len(pacientes)):
        if excluir_paciente == pacientes[i][0]:
            achou = True
            pos = i

    if achou:
        ref_arq = open("pacientes.txt", "w", encoding="utf-8")
        
        #Montando Linhas a Serem Gravadas
        for i in range(len(pacientes)):
            if i != pos:
                emails_formatados = "|".join(pacientes[i][5])
                telefones_formatados = "|".join(pacientes[i][6])
                linha = f'{pacientes[i][0]};{pacientes[i][1]};{pacientes[i][2]};{pacientes[i][3]};{pacientes[i][4]};{emails_formatados};{telefones_formatados}\n'
                ref_arq.write(linha)
            
        ref_arq.close()

        print("Paciente excluido com sucesso!")
    else:
        print("Paciente não cadastrado!")
    
    menu_opcoes()


###################################################################################
#                                   Consultas                                     #
###################################################################################


def submenu_consultas():
    print()
    print("##### Submenu de Consultas #####")
    print()
    print("1 - Listar todas as consultas")
    print("2 - Listar uma consulta específica")
    print("3 - Incluir nova consulta")
    print("4 - Alterar informação de uma consulta")
    print("5 - Excluir consulta")
    print("6 - Voltar")
    print()

    op_consulta = int(input("Digite o número da opção desejada: "))

    while op_consulta < 1 or op_consulta > 6:
        op_consulta = int(input("Digite o número da opção desejada: "))

    dados = ler_consultas()

    if op_consulta == 1:
        listar_consultas(dados)
    elif op_consulta == 2:
        listar_consul_esp(dados)
    elif op_consulta == 3:
        incluir_consulta(dados)
    elif op_consulta == 4:
        alterar_consulta(dados)
    elif op_consulta == 5:
        excluir_consulta(dados)
    else:
        menu_opcoes()


def listar_consultas(consultas):
    print("##### Lista de Consultas #####")
    print()

    for i in range(len(consultas)):
        print(f"CRM do Médico: {consultas[i][0]}")
        print(f"CPF do Paciente: {consultas[i][1]}")
        print(f"Data da consulta: {consultas[i][2]}")
        print(f"Horário da consulta: {consultas[i][3]}")
        print(f"Diagnóstico: {consultas[i][4]}")

        print("Medicamento(s) Receitado(s): ", end="")
        for j in range(len(consultas[i][5])):
            if j == len(consultas[i][5]) - 1:
                print(f"{consultas[i][5][j]}")
            else:
                print(f"{consultas[i][5][j]}", end=", ")

        print()

    menu_opcoes()


###################################################################################
#                                   Relatórios                                    #
###################################################################################


def submenu_relatorios():
    print()
    print("##### Submenu de Relatórios #####")
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

    # Estas chamadas ainda precisam ser adaptadas para os relatórios.
    if op_relatorio == 1:
        listar_paciente()
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
    print(os.getcwd())
    ref_arq = open("medicos.txt", "r", encoding="utf-8")

    for linha in ref_arq:
        lista = linha.split(";")
        medico = []

        emails = lista[6].split("|")
        telefones = lista[7].split("|")

        for i in range(len(telefones)):
            if i == len(telefones) - 1:
                telefones[i] = telefones[i][:-1]

        for i in range(len(lista) - 2):
            medico.append(lista[i])

        medico.append(emails)
        medico.append(telefones)
        medicos.append(medico)

    ref_arq.close()

    return medicos


def ler_pacientes():
    pacientes = []

    ref_arq = open("pacientes.txt", "r", encoding="utf-8")

    for linha in ref_arq:
        lista = linha.split(";")
        paciente = []

        emails = lista[5].split("|")
        telefones = lista[6].split("|")

        for i in range(len(telefones)):
            if i == len(telefones) - 1:
                telefones[i] = telefones[i][:-1]

        for i in range(len(lista) - 2):
            paciente.append(lista[i])

        paciente.append(emails)
        paciente.append(telefones)
        pacientes.append(paciente)

    ref_arq.close()

    return pacientes


def ler_consultas():
    consultas = []

    ref_arq = open("consultas.txt", "r", encoding="utf-8")

    for linha in ref_arq:
        lista = linha.split(";")
        consulta = []

        medicamento = lista[5].split("|")

        for i in range(len(medicamento)):
            if i == len(medicamento) - 1:
                medicamento[i] = medicamento[i][:-1]

        for i in range(len(lista) - 1):
            consulta.append(lista[i])

        consulta.append(medicamento)
        consultas.append(consulta)

    ref_arq.close()

    return consultas


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
    print("4 - Submenu de Relatórios")
    print("5 - Sair")
    print()

    op = int(input("Insira um número para acessar os menus abaixo: "))

    while op < 1 or op > 5:
        op = int(input("Digite o número da opção desejada: "))

    if op == 1:
        submenu_medicos()
    elif op == 2:
        submenu_pacientes()
    elif op == 3:
        submenu_consultas()
    elif op == 4:
        submenu_relatorios()
    elif op == 5:
        print("Obrigado por usar o sistema")
        print("Encerrando")


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
