from dicionarios import *

def cadastrarMotorista():
    print('-'*10,'Cadastrar Motorista','-'*10)
    while True:
        CPF=input("Informe o CPF:" )
        if verificarCPF(CPF):
            print('Motorista já cadastrado')
            print('\n')
            break
        nome=input("Nome do Motorista: ")
        carteira=input("Qual a classe da Carteira de habilitação?\n[1]-A \n[2]-B\n[3]-AB\nOpção?")
        if carteira=='1':
            CNH='A'
        elif carteira=='2':
            CNH='B'
        elif carteira=='3':
            CNH='AB'
        else:
            print('Opção invalida')
            break
        motorista={'CPF':CPF,'Nome':nome, 'CNH':CNH}
        baseMotorista[CPF]=motorista
        sair=int(input("Cadastrar outro Motorista?\n[1]-SIM\n[2]-NÃO\nOpção: "))
        if sair!=1:
            compilador()
            break
def buscarMotoristaPorCPF():
    print('----------Buscar Motorista por CPF----------')
    while True:
        CPF=input('Digite CPF do Motorista: ')
        if verificarCPF(CPF):
            for motorista in baseMotorista.values():
                if motorista.get('CPF')==CPF:
                    print('{:<17}{:<30}'.format('CPF', 'Nome'))
                    print('-'*28)
                    print('{:<17}{:<30}'.format(motorista.get('CPF'),format(motorista.get('Nome'))))
                    print('-'*28)
            input("click em enter para continuiar!!")
            return
        print('Motorista não cadastrado')
        input("click em enter para retornar ao menu!!")
        break
def editarNomeDoMotorista():
    print('----------Editar Nome do Motorista----------') 
    while True:
        CPF=input('Digite CPF do Motorista: ')
        for motorista in baseMotorista.values():
            if motorista.get('CPF')==CPF:
                novoNome = input('Digite novo nome: ')
                motorista.update(Nome=novoNome)
                baseGeral[CPF] = motorista
                print('Motorista atualizado com sucesso')
                input("click em enter para retornar ao menu!!")
                compilador()
            return
        print('Motorista não cadastrado')
        input("click em enter para retornar ao menu!!")
        return
def removerMotorista():
    print('-'*10,'Remover Motorista','-'*10)
    while True:
        CPF = input('Digite CPF: ')
        for motorista in baseMotorista.values():
            if motorista.get('CPF') == CPF:
                print('{:<17}{:<30}'.format('CPF', 'Nome'))
                print('-' * 28)
                print('{:<17}{:<30}'.format(motorista.get('CPF'), format(motorista.get('Nome'))))
                print('-' * 28)
                opcao = int(input('Deseja remover Motorista ? [1]-Sim - [2]-Não: '))
                if opcao == 1:
                    del baseMotorista[CPF]
                    print('Motorista excluído com sucesso')
                    seCondutor=int(input('Ele também estava escalado para algum veiculo?\n [1]-Sim - [2]-Não : '))
                    if seCondutor==1:
                        PLACA=input('Digite a PLACA:')
                        for piloto in baseVeiculo.values():
                            if piloto.get('PLACA')==PLACA:
                                validacao = 'None'
                                if piloto.get('PLACA') == PLACA:
                                    baseVeiculo[PLACA].update(Motorista=validacao)
                                    print('Motorista removido com sucesso')
                                    input("click em enter para retornar ao menu!!")
                    compilador()
                    return
                elif opcao == 2:
                    print('Exclusão não efetuada')
                    return
                else:
                    print('Opção Inválida')
                    return
        print('Motorista não cadastrado')
        break
def listarTodosOsMotoristasPorTipoDaCarteira():
    print('-'*10,'Listar Todos os Motorista por tipo da carteira','-'*10)  # perguntar antes qual tipo da carteira ('A' - 'B' - 'AB')
    while True:
        carteira=int(input('Escolha qual carteira deseja listar - [1]=A / [2]=B / [3]=AB : '))
        if carteira==1:
            print('{:<17}{:<20}{:<40}'.format('CPF', 'Nome', 'CNH'))
            print('-'*45)
            for cadastro in baseMotorista.values():
                if cadastro.get('CNH')== 'A':
                    print('{:<17}{:<20}{:<40}'.format(cadastro.get('CPF'), cadastro.get('Nome'), cadastro.get('CNH')))
            break
        elif carteira==2:
            print('{:<17}{:<20}{:<40}'.format('CPF', 'Nome', 'CNH'))
            print('-'*45)
            for cadastro in baseMotorista.values():
                if cadastro.get('CNH')== 'B':
                    print('{:<17}{:<20}{:<40}'.format(cadastro.get('CPF'), cadastro.get('Nome'), cadastro.get('CNH')))
        elif carteira==3:
            print('{:<17}{:<20}{:<40}'.format('CPF', 'Nome', 'CNH'))
            print('-'*45)
            for cadastro in baseMotorista.values():
                if cadastro.get('CNH')== 'AB':
                    print('{:<17}{:<20}{:<40}'.format(cadastro.get('CPF'), cadastro.get('Nome'), cadastro.get('CNH')))
        else:
            print('Opção invalálida')
            print('\n')
        break
def listarTodosOsMotorista():
    print('-'*10,'Listar de todos os Motorista','-'*10)
    print('{:<17}{:<20}{:<40}'.format('CPF', 'Nome', 'CNH'))
    print('-'*45)
    for cadastro in baseMotorista.values():
        print('{:<17}{:<20}{:<40}'.format(cadastro.get('CPF'), cadastro.get('Nome'), cadastro.get('CNH')))
    print('-'*45)
def verificarCPF(CPF):
    return (CPF in baseMotorista)