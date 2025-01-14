AGENDA = {}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
            print('----------------------------------------------------------------------------------\n')
    else:
        print("Agenda Vazia")

'''def mostrar_contato_individual():
    contato = input("Digite o nome da pessoa em que deseje verificar as info: ")
    if contato in AGENDA:
        print(f'Nome: {contato}')
        print(f'Telefone: {AGENDA[contato]['cell']}')
        print(f'Email: {AGENDA[contato]['email']}')
        print(f'CEP: {AGENDA[contato]['cep']}')
    else:
        print('Pessoa nao encontrada.')''' #JEITO QUE EU FIZ

def buscar_contato(contato):
    try:
        print(f'Nome: {contato}')
        print(f'Telefone: {AGENDA[contato]['cell']}')
        print(f'Email: {AGENDA[contato]['email']}')
        print(f'CEP: {AGENDA[contato]['cep']}')
        print('----------------------------------------------------------------------------------\n')
    except KeyError:
        print('Contato não encontrado')
    except Exception as error:
        print(error)

def ler_detalhes_contato():
    telefone = input('Digite o nome do telefone: ')
    email = input('Digite o nome do email: ')
    cep = input('Digite o nome do cep: ')
    return telefone, email, cep

def incluir_editar_contato(contato,telefone,email,cep):

    AGENDA[contato] = {
        'cell': telefone,
        'email': email,
        'cep': cep,
    }
    salvar()
    print(f"\n>>>>>Contato {contato} adicionado/editado a agenda.<<<<<<\n")

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print(f"\n>>>>>Contato {contato} excluido da agenda.<<<<<<\n")
    except:
        print('Contato não encontrado')

def exportar_contatos(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write('Nome;Telefone;Email;Cep\n')
            for contato in AGENDA:
                tel = AGENDA[contato]['cell']
                email = AGENDA[contato]['email']
                cep = AGENDA[contato]['cep']
                file.write(f'{contato};{tel};{email};{cep}\n')
        print('~~~~~~Agenda exportada')
    except:
        print("+++++++Algo de errado ocorreu")

def importar_contato(file_name):
    try:
        with open(file_name, 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(';')

                # print(detalhes)
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes [2]
                cep = detalhes [3]

                incluir_editar_contato(nome, telefone, email, cep)

    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as error:
        print("Erro inesperado")
        print(error)

def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(';')

                # print(detalhes)
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes [2]
                cep = detalhes [3]

                AGENDA[nome] = {
                    'cell': telefone,
                    'email': email,
                    'cep': cep,
                }
        print("Database carregado com suscesso")
        print(f'{len(AGENDA)} contatos carregados')
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as error:
        print("Erro inesperado")
        print(error)



def imprimir_menu():
    print('''
    ==================================================================================
    1- Mostrar todos os contatos da agenda
    2- Buscar contato
    3- Incluir contato
    4- Editar contato
    5- Excluir contato
    6- Exportar contatos para CSV
    7- Importar Contatos CSV
    8- Salvar
    0- Fechar agenda
    ==================================================================================
    ''')


# INICIO DO PROGRAMA

carregar()

while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('Digite o nome do contato: ')
        
        try:
            AGENDA[contato]
            print("Contato já existente")
        except:
            telefone,email,cep = ler_detalhes_contato()
            incluir_editar_contato(contato,telefone,email,cep)

    elif opcao == '4':
        contato = input('Digite o nome do contato: ')
        
        try:
            AGENDA[contato]
            print("Editando contato", contato)
            telefone,email,cep = ler_detalhes_contato()
            incluir_editar_contato(contato,telefone,email,cep)
        except:
            print('Contato inexistente')

    elif opcao == '5':
        contato = input("Contato que deseja excluir: ")
        excluir_contato(contato)

    elif opcao == '6':
        file = input('Digite o nome para ser exportado: ')
        exportar_contatos(file)

    elif opcao == '7':
        file = input("Digite o nome do arquivo a ser importado: ")
        importar_contato(file)
    
    elif opcao == '8':
        salvar()

    elif opcao == '0':
        print(">>>>Fechando o programa<<<<")
        break

    else:
        print("Opção inválida")

salvar()
