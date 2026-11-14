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
    print("4 - Alterar informações de um médico")
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
        print(f"Instituição de formação: {medicos[i][5]}")

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
            print(f"Instituição de formação: {medicos[i][5]}")

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
        print("Médico não encontrado.")

    menu_opcoes()


######################### Incluir Novo Médico #############################

def incluir_medico(medicos):
    novo_medico = input("Digite o CRM do novo médico: ").strip()

    while novo_medico == "":
        print()
        print("Esse campo é obrigatório!")
        novo_medico = input("Digite o CRM do novo médico (ex.: SP123456): ").strip()

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
        formado = input("Instituição de formação: ")

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

        # Montando linha
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
        formado = input("Instituição de formação: ")

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

        # Montando linhas a serem gravadas
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

        # Montando linhas a serem gravadas
        for i in range(len(medicos)):
            if i != pos:
                emails_formatados = "|".join(medicos[i][6])
                telefones_formatados = "|".join(medicos[i][7])
                linha = f'{medicos[i][0]};{medicos[i][1]};{medicos[i][2]};{medicos[i][3]};{medicos[i][4]};{medicos[i][5]};{emails_formatados};{telefones_formatados}\n'
                ref_arq.write(linha)

        ref_arq.close()

        print("Médico excluído com sucesso!")
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
    print("4 - Alterar informações de um paciente")
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
        print(f"Plano de saúde: {pacientes[i][4]}")

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

            print(f"CPF: {pacientes[i][0]}")
            print(f"Nome: {pacientes[i][1]}")
            print(f"Data de nascimento: {pacientes[i][2]}")
            print(f"Sexo: {pacientes[i][3]}")
            print(f"Plano de saúde: {pacientes[i][4]}")

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
        print("Paciente não encontrado.")

    menu_opcoes()


######################### Incluir Paciente #############################

def incluir_paciente(pacientes):
    novo_pac = input("Digite o CPF do novo paciente (apenas números): ").strip()
    novo_pac = f'{novo_pac[:3]}.{novo_pac[3:6]}.{novo_pac[6:9]}-{novo_pac[9:]}'

    while novo_pac == "":
        print()
        print("Esse campo é obrigatório!")
        novo_pac = input("Digite o CPF do novo paciente (apenas números): ").strip()

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
        plano = input("Plano de saúde: ")

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

        # Montando linha
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
    alt_pac = input("Digite o CPF do paciente a ser alterado (só números): ")
    alt_pac = f'{alt_pac[:3]}.{alt_pac[3:6]}.{alt_pac[6:9]}-{alt_pac[9:]}'

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
        plano = input("Plano de saúde: ")

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

        # Montando linhas a serem gravadas
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
    exc_pac = input("Digite o CPF do paciente a ser excluído (só números): ")
    exc_pac = f'{exc_pac[:3]}.{exc_pac[3:6]}.{exc_pac[6:9]}-{exc_pac}'

    achou = False
    pos = 0

    for i in range(len(pacientes)):
        if exc_pac == pacientes[i][0]:
            achou = True
            pos = i

    if achou:
        ref_arq = open("pacientes.txt", "w", encoding="utf-8")

        # Montando linhas a serem gravadas
        for i in range(len(pacientes)):
            if i != pos:
                emails_formatados = "|".join(pacientes[i][5])
                telefones_formatados = "|".join(pacientes[i][6])
                linha = f'{pacientes[i][0]};{pacientes[i][1]};{pacientes[i][2]};{pacientes[i][3]};{pacientes[i][4]};{emails_formatados};{telefones_formatados}\n'
                ref_arq.write(linha)

        ref_arq.close()

        print("Paciente excluído com sucesso!")
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
    print("4 - Alterar informações de uma consulta")
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
        listar_consulta_esp(dados)
    elif op_consulta == 3:
        incluir_consulta(dados)
    elif op_consulta == 4:
        alterar_consulta(dados)
    elif op_consulta == 5:
        excluir_consulta(dados)
    else:
        menu_opcoes()


######################### Listar Consultas #############################

def listar_consultas(consultas):
    print("##### Lista de Consultas #####")
    print()

    for i in range(len(consultas)):
        print(f"CRM do médico: {consultas[i][0]}")
        print(f"CPF do paciente: {consultas[i][1]}")
        print(f"Data da consulta: {consultas[i][2]}")
        print(f"Horário da consulta: {consultas[i][3]}")
        print(f"Diagnóstico: {consultas[i][4]}")

        print("Medicamentos receitados: ", end="")
        for j in range(len(consultas[i][5])):
            if j == len(consultas[i][5]) - 1:
                print(f"{consultas[i][5][j]}")
            else:
                print(f"{consultas[i][5][j]}", end=", ")

        print()

    menu_opcoes()


######################### Listar Consulta Específica #############################

def listar_consulta_esp(consultas):
    print("##### Listar uma consulta específica #####")
    print()

    crm = input("Digite o CRM do médico (ex.: SP123456): ").strip()
    data = input("Digite a data da consulta (dd/mm/aaaa): ").strip()
    hora = input("Digite a hora da consulta (HH:MM): ").strip()

    cpf = input("Digite o CPF do paciente (apenas números): ").strip()
    cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    achou = False

    for i in range(len(consultas)):
        if crm == consultas[i][0] and cpf == consultas[i][1] and data == consultas[i][2] and hora == consultas[i][3]:
            achou = True

            print(f"CRM: {consultas[i][0]}")
            print(f"CPF do paciente: {consultas[i][1]}")
            print(f"Data: {consultas[i][2]}")
            print(f"Horário: {consultas[i][3]}")
            print(f"Diagnóstico: {consultas[i][4]}")

            print("Medicamentos: ", end="")
            for j in range(len(consultas[i][5])):
                if j == len(consultas[i][5]) - 1:
                    print(f"{consultas[i][5][j]}")
                else:
                    print(f"{consultas[i][5][j]}", end=", ")

            print()

    if achou == False:
        print("Consulta não encontrada.")

    menu_opcoes()


######################### Incluir Consulta #############################

def incluir_consulta(consultas):
    print("##### Incluir Consulta #####")
    print()

    crm = input("Digite o CRM do médico (ex.: SP123456): ").strip()
    data = input("Digite a data da consulta (dd/mm/aaaa): ").strip()
    hora = input("Digite a hora da consulta (HH:MM): ").strip()

    cpf = input("Digite o CPF do paciente (apenas números): ").strip()
    cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    achou = False

    for i in range(len(consultas)):
        if crm == consultas[i][0] and cpf == consultas[i][1] and data == consultas[i][2] and hora == consultas[i][3]:
            achou = True

    if achou:
        print("Essa consulta já está cadastrada.")
    else:
        diagnostico = input("Diagnóstico: ")
        n_medicamentos = int(input("Quantos medicamentos deseja informar? "))
        medicamentos = []

        print("Digite o(s) medicamento(s): ")
        for i in range(n_medicamentos):
            medicamento = input()
            medicamentos.append(medicamento)

        # Montando linha
        medicamentos_formatados = "|".join(medicamentos)

        linha = f"{crm};{cpf};{data};{hora};{diagnostico};{medicamentos_formatados}\n"

        ref_arq = open("consultas.txt", "a", encoding="utf-8")
        ref_arq.write(linha)
        ref_arq.close()

        print()
        print("Consulta cadastrada com sucesso!")

    menu_opcoes()


######################### Alterar Consulta #############################

def alterar_consulta(consultas):
    print("##### Alterar Consulta #####")
    print()

    crm = input("Digite o CRM do médico da consulta a ser alterada (ex.: SP123456): ").strip()

    cpf = input("Digite o CPF do paciente da consulta a ser alterada (apenas números): ").strip()
    cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    data = input("Digite a data da consulta a ser alterada (dd/mm/aaaa): ").strip()
    hora = input("Digite a hora da consulta a ser alterada (HH:MM): ").strip()

    achou = False
    pos = 0

    for i in range(len(consultas)):
        if crm == consultas[i][0] and cpf == consultas[i][1] and data == consultas[i][2] and hora == consultas[i][3]:
            achou = True
            pos = i

    if achou:
        novo_crm = input("Digite o novo CRM do médico (ex.: SP123456): ").strip()

        novo_cpf = input("Digite o CPF do paciente (apenas números): ").strip()
        novo_cpf = f'{novo_cpf[:3]}.{novo_cpf[3:6]}.{novo_cpf[6:9]}-{novo_cpf[9:]}'

        nova_data = input("Digite a nova data da consulta (dd/mm/aaaa): ").strip()
        nova_hora = input("Digite a nova hora da consulta (HH:MM): ").strip()

        novo_diagnostico = input("Digite o novo diagnóstico: ")
        n_medicamentos = int(input("Quantos medicamentos deseja informar? "))
        novos_medicamentos = []

        print("Digite o(s) novo(s) medicamento(s): ")
        for i in range(n_medicamentos):
            medicamento = input()
            novos_medicamentos.append(medicamento)

        conferir = False
        for i in range(len(consultas)):
            if i != pos:
                if novo_crm == consultas[i][0] and novo_cpf == consultas[i][1] and nova_data == consultas[i][2] and nova_hora == consultas[i][3]:
                    conferir = True

        if conferir:
            print("Já existe uma consulta com esses dados!")
            menu_opcoes()
            return

        consultas[pos] = [novo_crm, novo_cpf, nova_data, nova_hora, novo_diagnostico, novos_medicamentos]

        # Montando linhas a serem gravadas
        ref_arq = open("consultas.txt", "w", encoding="utf-8")

        for i in range(len(consultas)):
            medicamentos_formatados = "|".join(consultas[i][5])
            linha = f'{consultas[i][0]};{consultas[i][1]};{consultas[i][2]};{consultas[i][3]};{consultas[i][4]};{medicamentos_formatados}\n'
            ref_arq.write(linha)

        ref_arq.close()

        print("Consulta alterada com sucesso!")
    else:
        print("Consulta não cadastrada!")

    menu_opcoes()


######################### Excluir Consulta #############################

def excluir_consulta(consultas):
    print("##### Excluir Consulta #####")
    print()

    crm = input("Digite o CRM do médico da consulta a ser excluída (ex.: SP123456): ").strip()

    cpf = input("Digite o CPF do paciente da consulta a ser excluída (apenas números): ").strip()
    cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    data = input("Digite a data da consulta a ser excluída (dd/mm/aaaa): ").strip()
    hora = input("Digite a hora da consulta a ser excluída (HH:MM): ").strip()

    achou = False
    pos = 0

    for i in range(len(consultas)):
        if crm == consultas[i][0] and cpf == consultas[i][1] and data == consultas[i][2] and hora == consultas[i][3]:
            achou = True
            pos = i

    if achou:
        ref_arq = open("consultas.txt", "w", encoding="utf-8")

        # Montando linhas a serem gravadas
        for i in range(len(consultas)):
            if i != pos:
                medicamentos_formatados = "|".join(consultas[i][5])
                linha = f'{consultas[i][0]};{consultas[i][1]};{consultas[i][2]};{consultas[i][3]};{consultas[i][4]};{medicamentos_formatados}\n'
                ref_arq.write(linha)

        ref_arq.close()

        print("Consulta excluída com sucesso!")
    else:
        print("Consulta não cadastrada!")

    menu_opcoes()


###################################################################################
#                                   Relatórios                                    #
###################################################################################

def submenu_relatorios():
    print()
    print("##### Submenu de Relatórios #####")
    print()
    print("1 - Listar médicos por especialidade")
    print("2 - Listar pacientes menores de uma idade informada")
    print("3 - Listar consultas dos últimos X dias")
    print("4 - Voltar")
    print()

    op_relatorio = int(input("Digite o número da opção desejada: "))

    while op_relatorio < 1 or op_relatorio > 4:
        op_relatorio = int(input("Digite o número da opção desejada: "))

    dados_med = ler_medicos()
    dados_pac = ler_pacientes()
    dados_con = ler_consultas()

    if op_relatorio == 1:
        listar_medico_especialidade(dados_med)
    elif op_relatorio == 2:
        listar_paciente_idade(dados_pac)
    elif op_relatorio == 3:
        listar_ultimas_consultas(dados_med, dados_pac, dados_con)
    else:
        menu_opcoes()


######################### Relatório de Médicos por Especialidade #############################

def listar_medico_especialidade(medicos):
    especialidade = input("Qual a especialidade dos médicos a serem listados? ")
    achou = False

    for i in range(len(medicos)):
        if especialidade == medicos[i][4]:
            achou = True

            print(f"CRM: {medicos[i][0]}")
            print(f"Nome: {medicos[i][1]}")
            print(f"Data de nascimento: {medicos[i][2]}")
            print(f"Sexo: {medicos[i][3]}")
            print(f"Especialidade: {medicos[i][4]}")
            print(f"Instituição de formação: {medicos[i][5]}")

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

            emails_formatados = "|".join(medicos[i][6])
            telefones_formatados = "|".join(medicos[i][7])

            linha = f"Relatório de médicos com especialidade em {especialidade};{medicos[i][0]};{medicos[i][1]};{medicos[i][2]};{medicos[i][3]};{medicos[i][4]};{medicos[i][5]};{emails_formatados};{telefones_formatados}\n"

            ref_arq = open("relatorio_medicos.txt", "a", encoding="utf-8")
            ref_arq.write(linha)
            ref_arq.close()

    if achou == False:
        print("Nenhum médico com essa especialidade encontrado!")

    menu_opcoes()


######################### Relatório de Pacientes por Idade #############################

def listar_paciente_idade(pacientes):
    idade = int(input("Listar pacientes menores de quantos anos? "))

    data_atual = input("Informe a data de hoje (dd/mm/aaaa): ")
    data_atual = data_atual.split("/")

    dia_atual = int(data_atual[0])
    mes_atual = int(data_atual[1])
    ano_atual = int(data_atual[2])

    for i in range(len(pacientes)):
        data_paciente = pacientes[i][2].split("/")
        dia_nasc = int(data_paciente[0])
        mes_nasc = int(data_paciente[1])
        ano_nasc = int(data_paciente[2])

        # d_soma = (dia_atual - dia_nasc) + ((mes_atual - mes_nasc)*30) + ((ano_atual - ano_nasc)*365)

        idade_paciente = ano_atual - ano_nasc

        if mes_atual < mes_nasc:
            idade_paciente = idade_paciente - 1
        elif mes_atual == mes_nasc and dia_atual < dia_nasc:
            idade_paciente = idade_paciente - 1

        if idade_paciente < idade:
            print(f"CPF: {pacientes[i][0]}")
            print(f"Nome: {pacientes[i][1]}")
            print(f"Data de nascimento: {pacientes[i][2]}")
            print(f"Sexo: {pacientes[i][3]}")
            print(f"Plano de saúde: {pacientes[i][4]}")

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

            emails_formatados = "|".join(pacientes[i][5])
            telefones_formatados = "|".join(pacientes[i][6])

            linha = f"Relatório dos pacientes menores de {idade} anos;{pacientes[i][0]};{pacientes[i][1]};{pacientes[i][2]};{pacientes[i][3]};{pacientes[i][4]};{emails_formatados};{telefones_formatados}\n"

            ref_arq = open("relatorio_pacientes.txt", "a", encoding="utf-8")
            ref_arq.write(linha)
            ref_arq.close()

    menu_opcoes()


######################### Relatório das Últimas Consultas #############################

def listar_ultimas_consultas(medicos, pacientes, consultas):
    data_atual = input("Data atual (dd/mm/aaaa): ")
    data_atual = data_atual.split("/")

    dias = int(input("Deseja listar as consultas dos últimos quantos dias? "))

    dia_atual = int(data_atual[0])
    mes_atual = int(data_atual[1])
    ano_atual = int(data_atual[2])

    for i in range(len(consultas)):
        data_consulta = consultas[i][2].split("/")
        dia_con = int(data_consulta[0])
        mes_con = int(data_consulta[1])
        ano_con = int(data_consulta[2])

        dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        total_atual = ano_atual * 365 + dia_atual
        for k in range(mes_atual - 1):
            total_atual = total_atual + dias_meses[k]

        total_consulta = ano_con * 365 + dia_con
        for k in range(mes_con - 1):
            total_consulta = total_consulta + dias_meses[k]

        d_soma = total_atual - total_consulta

        if 0 <= d_soma <= dias:
            nome_medico = "Cadastro excluído ou não encontrado"
            nome_paciente = "Cadastro excluído ou não encontrado"

            for j in range(len(medicos)):
                if medicos[j][0] == consultas[i][0]:
                    nome_medico = medicos[j][1]

            for j in range(len(pacientes)):
                if pacientes[j][0] == consultas[i][1]:
                    nome_paciente = pacientes[j][1]

            print(f"CRM: {consultas[i][0]}")
            print(f"Nome do médico: {nome_medico}")
            print(f"CPF do paciente: {consultas[i][1]}")
            print(f"Nome do paciente: {nome_paciente}")

            lista = [consultas[i][0], nome_medico, consultas[i][1], nome_paciente]

            print(f"Data da consulta: {consultas[i][2]}")
            print(f"Horário da consulta: {consultas[i][3]}")
            print(f"Diagnóstico: {consultas[i][4]}")

            print("Medicamentos receitados: ", end="")
            for j in range(len(consultas[i][5])):
                if j == len(consultas[i][5]) - 1:
                    print(f"{consultas[i][5][j]}")
                else:
                    print(f"{consultas[i][5][j]}", end=", ")

            lista.append(consultas[i][2])
            lista.append(consultas[i][3])
            lista.append(consultas[i][4])
            lista.append(consultas[i][5])

            print()

            medicamentos_formatados = "|".join(consultas[i][5])

            linha = f"Relatório de consultas dos últimos {dias} dias;{lista[0]};{lista[1]};{lista[2]};{lista[3]};{lista[4]};{lista[5]};{lista[6]};{medicamentos_formatados}\n"

            ref_arq = open("relatorio_consultas.txt", "a", encoding="utf-8")
            ref_arq.write(linha)
            ref_arq.close()

    menu_opcoes()


###################################################################################
#                                    Ler dados                                    #
###################################################################################

def ler_medicos():
    medicos = []
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

    op = int(input("Digite o número da opção desejada: "))

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
        print("Obrigado por usar o sistema!")
        print("Encerrando...")


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