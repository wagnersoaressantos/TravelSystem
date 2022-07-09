def menuPrincipal():
    print('-----------MENU---------')
    print('1 - Menu de Motorista')
    print('2 - Menu de Veiculo')
    print('3 - Menu de Viagem')
    print('4 - SAIR')
    opcao=int(input("Escolha uma das opções: "))
    return opcao

def menuMotorista():
    print('-----------MENU MOTORISTAS---------')
    print('1 - Cadastrar Motorista')
    print('2 - Buscar Motorista por CPF')
    print('3 - Editar Nome do Motorista') 
    print('4 - Remover Motorista')
    print('5 - Listar Todos os Motorista por tipo da carteira')
    print('6 - Listar Todos os Motorista')
    print('7 - SAIR')
    opcaoMotorista=int(input("Escolha uma das opções: "))
    return opcaoMotorista

def menuVeiculo():
    print('-----------MENU---------')
    print('1 - Cadastrar Veiculo')
    print('2 - Buscar Veiculo por Placa')
    print('3 - Adicionar Motorista ao veiculo')
    print('4 - Remover Motorista do veiculo')
    print('5 - Listar veiculos com motoristas')
    print('6 - Listar veiculos sem motoristas')
    print('7 - Remover Veiculo')
    print('8 - SAIR')
    opcaoVeiculo = int(input("Escolha uma das opções: "))
    return opcaoVeiculo

def menuViagem():
    print('-----------MENU---------')
    print('1 - Criar Viagem')
    print('2 - Finalizar Viagem por placa') 
    print('3 - Viagens Ativas')
    print('4 - Veiculos que estão em Viagem')
    print('5 - Veiculos que estão Disponíveis para Viagem')
    print('6 - Listar todas as viagens')
    print('7 - Listar todas as viagens por período')
    print('8 - SAIR')
    opcaoViagem = int(input("Escolha uma das opções: "))
    return opcaoViagem
