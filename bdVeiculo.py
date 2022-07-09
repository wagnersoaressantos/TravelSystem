from dicionarios import *

def cadastrasVeiculo():
    print('-'*10,'Cadastrar Veiculo','-'*10)
    while True:
        PLACA = input("Informe a PLACA:")
        if verificarPLACA(PLACA):
            print('Veiculo já cadastrado')
            print('\n')
            break
        tipo = int(input("Qual é o veiculo?\n[1]-Moto \n[2]-Carro\nOpção?"))
        if tipo == 1:
            Tipo = 'Moto'
        elif tipo == 2:
            Tipo = 'Carro'
        else:
            print('Opção invalida')
            break
        motorista='None'
        disponivel=True
        veiculo = {'PLACA': PLACA, 'TIPO': Tipo, 'Motorista': motorista, 'Disponivel':disponivel}
        baseVeiculo[PLACA] = veiculo
        sair = int(input("Cadastrar outro veiculo?\n[1]-SIM\n[2]-NÃO\nOpção: "))
        if sair != 1:
            print('Salvando!')
            compilador()
            print('Salvamento concluido')
            break
def buscarVeiculoPorPlaca():
    print('-'*10,'Buscar Veiculo por Placa','-'*10)
    while True:
        PLACA=input('Digite PLACA do veiculo: ')
        for cadastro in baseVeiculo.values():
            if cadastro.get('PLACA')==PLACA:
                print('{:<17}{:<30}'.format('PLACA', 'Tipo'))
                print('-'*28)
                print('{:<17}{:<30}'.format(cadastro.get('PLACA'),format(cadastro.get('TIPO'))))
                print('-'*28)
                input("click em enter para continuiar!!")
                return
        print('Veiculo não cadastrado')
        input("click em enter para retornar ao menu!!")
        break
def adicionarMotoristaAoVeiculo():
    print('-'*10,'Adicionar Motorista ao veiculo','-'*10)
    while True:
        PLACA=input('Digite a PLACA do veiculo que vai ter motorista: ')
        for cadastro in baseVeiculo.values():
            if cadastro.get('PLACA')==PLACA:
                print('{:<17}{:<30}'.format('PLACA', 'Tipo'))
                print('-'*28)
                print('{:<17}{:<30}'.format(cadastro.get('PLACA'),format(cadastro.get('TIPO'))))
                print('-'*28)
                confirmacao1=int(input('Esté é o veiculo que quer atribuir o motorista?\n[1]-SIM\n[2]-NÃO\nOpção: '))
                if confirmacao1==1:
                    while True:
                        CPF = input('Digite CPF do Motorista: ')
                        for condutor in baseMotorista.values():
                            if condutor.get('CPF') == CPF:
                                print('{:<17}{:<30}'.format('CPF', 'Nome'))
                                print('-' * 28)
                                print('{:<17}{:<30}'.format(condutor.get('CPF'), format(condutor.get('Nome'))))
                                print('-' * 28)
                                confirmacao2 = int(input('Esté é o motorista que quer atribuir ao vaiculo?\n[1]-SIM\n[2]-NÃO\nOpção: '))
                                if confirmacao2 == 1:
                                    validacao=condutor.get('Nome')
                                    if cadastro.get('PLACA') == PLACA:
                                        baseVeiculo[PLACA].update(Motorista=validacao)
                                        print('Salvando!')
                                        compilador()
                                        print('Salvamento concluido')
                                    print('Motorista atribuido com sucesso')
                                    print('{:<17}{:<20}{:<40}'.format('PLACA', 'Tipo','Motorista'))
                                    print('-' * 60)
                                    print('{:<17}{:<20}{:<40}'.format(cadastro.get('PLACA'), format(cadastro.get('TIPO')), format(cadastro.get('Motorista'))))
                                    print('-' * 60)
                                    input("click em enter para retornar ao menu!!")
                                    return
                        print('Motorista não cadastrado')
                        input("click em enter para retornar ao menu!!")
                        return
                return
        print('Veiculo não cadastrado')
        input("click em enter para retornar ao menu!!")
        return
def removerMotoristaDoVeiculo():
    print('-'*10,'Remover Motorista do veiculo','-'*10)
    while True:
        PLACA=input('Digite a PLACA do veiculo que vai ter motorista: ')
        for cadastro in baseVeiculo.values():
            if cadastro.get('PLACA')==PLACA:
                if cadastro.get('Motorista') != 'None':
                    print('{:<17}{:<20}{:<40}'.format('PLACA', 'Tipo', 'Motorista'))
                    print('-'*60)
                    print('{:<17}{:<20}{:<40}'.format(cadastro.get('PLACA'), cadastro.get('TIPO'), cadastro.get('Motorista')))
                    print('-'*60)
                confirmacao1=int(input('É esté é o veiculo que quer remover o motorista?\n[1]-SIM\n[2]-NÃO'))
                if confirmacao1==1:
                    validacao = 'None'
                    if cadastro.get('PLACA') == PLACA:
                        baseVeiculo[PLACA].update(Motorista=validacao)
                        print('Motorista removido com sucesso')
                        print('{:<17}{:<30}'.format('PLACA', 'Tipo'))
                        print('-' * 28)
                        print('{:<17}{:<30}'.format(cadastro.get('PLACA'), format(cadastro.get('TIPO'))))
                        print('-' * 28)
                        input("click em enter para retornar ao menu!!")
                        return
                input("click em enter para retornar ao menu!!")
                return
        print('Veiculo não encontrado')
        input("click em enter para retornar ao menu!!")
        return
def listarVeiculosComMotoristas():
    print('-'*10,'Listar veiculos com motoristas','-'*10)
    print('{:<17}{:<20}{:<40}'.format('PLACA', 'Tipo','Motorista'))
    print('-' * 60)
    for cadastro in baseVeiculo.values():
        if cadastro.get('Motorista') != 'None':
            print('{:<17}{:<20}{:<40}'.format(cadastro.get('PLACA'), cadastro.get('TIPO'),cadastro.get('Motorista')))
    print('-' * 60)
    input("click em enter para continual")
    return
def listarVeiculosSemMotoristas():
    print('-'*10,'Listar veiculos sem motoristas','-'*10)
    print('{:<17}{:<30}'.format('PLACA','Tipo'))
    print('-'*30)
    for cadastro in baseVeiculo.values():
        if cadastro.get('Motorista')== 'None':
            print('{:<17}{:<30}'.format(cadastro.get('PLACA'), cadastro.get('TIPO')))
    print('-'*30)
    input("click em enter para continual")
def removerVeiculo():
    print('7 - Remover Veiculo')
    while True:
        PLACA = input('Digite a PLACA do veiculo: ')
        for veiculo in baseVeiculo.values():
            if veiculo.get('PLACA') == PLACA:
                print('{:<17}{:<30}'.format('PLACA', 'Tipo'))
                print('-' * 28)
                print('{:<17}{:<30}'.format(veiculo.get('PLACA'), format(veiculo.get('TIPO'))))
                print('-' * 28)
                opcao = int(input('Deseja remover baseMotorista ? [1]Sim - [2]Não: '))
                if opcao == 1:
                    del baseVeiculo[PLACA]
                    print('Veiculo excluído com sucesso')
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
def verificarPLACA(PLACA):
    return (PLACA in baseVeiculo)