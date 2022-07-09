from datetime import *
from dicionarios import *

def criarViagem():
    print('-'*10,'Criar Viagem','-'*10)
    while True:
        print('-' * 28)
        PLACA = input('Digite Placa do Veiculo para Criar Viagem: ')
        for geralVeiculo in baseVeiculo.values():
            if geralVeiculo.get('PLACA')==PLACA:
                if geralVeiculo.get('Disponivel') == True:
                    Motorista=geralVeiculo.get('Motorista')
                    tipo=geralVeiculo.get('TIPO')
                    baseVeiculo[PLACA].update(Disponivel=False)
                    rota = input('Digite destino da viagem: ')
                    d=date.today()
                    dataDeHoje=d.strftime('%dd/%mm/%YY')
                    print('Data de Hoje é ',dataDeHoje)
                    confirmacao=int(input('Vai iniciar a viagem na data hoje ?\n[1]-SIM\n[2]-NÃO\nOpção: '))
                    if confirmacao==1:
                        dataSaida=dataDeHoje
                    elif confirmacao==2:
                        intervalo=input('Qual a data da viagem?(formato Dia/Mês/Ano): ')
                        dataAgendada=intervalo
                        print('Data de saida ',dataAgendada)
                        confimaData=int(input('Confirma a data de saída?\n[1]-SIM\n[2]-NÃO\nOpção: '))
                        if confimaData==1:
                            dataSaida=dataAgendada
                    else:
                        print('Opção inválida')
                        print('click em enter para retornar ao menu!!')
                    chegada=input('Qual a data de chegada prevista?(formato Dia/Mês/Ano): ')
                    dataFim=chegada
                    print('Date prevista de chegada ',dataFim)
                    confirmaChegada=int(input('Confirma a data de chegada?\n[1]-SIM\n[2]-NÃO\nOpção: '))
                    if confirmaChegada==1:
                        dataChegada=dataFim
                    elif confirmaChegada!=1:
                        print('Criação de viagem cancelada')
                        return
                    viagem = {'PLACA': PLACA,'TIPO':tipo,'Motorista':Motorista, 'rota': rota, 'SAIDA': dataSaida, 'CHEGADA': dataChegada, 'status': True}
                    baseViagens[PLACA] = viagem
                    compilador()
                    print('-------------------------------------')
                    input('click em enter para retornar ao menu!!')
                    return
                print('Veiculo já em uso')
                input('click em enter para retornar ao menu!!.')
                return
        print('Veiculo não cadastrado')
        print('-------------------------------------')
        input('Aperte qualquer tecla para continuar.')
        return

def finalizarViagemPorPlaca():
    print('-'*10,'Finalizar Viagem por placa','-'*10) 
    while True:
        PLACA=input('Digite a PLACA do veiculo: ')
        for cadastro in baseViagens.values():
            if cadastro.get('PLACA')==PLACA:
                if cadastro.get('status') != False:
                    print('{:<17}{:<20}{:<40}'.format('PLACA', 'Tipo', 'Motorista'))
                    print('-'*60)
                    print('{:<17}{:<20}{:<40}'.format(cadastro.get('PLACA'), cadastro.get('TIPO'), cadastro.get('Motorista')))
                    print('-'*60)
                confirmacao1=int(input('Deseja finalizar essa viagem?\n[1]-SIM\n[2]-NÃO: '))
                if confirmacao1==1:
                    if cadastro.get('PLACA') == PLACA:
                        baseViagens[PLACA].update(status=False)
                        baseVeiculo[PLACA].update(Disponivel=True)
                        compilador()
                        print('Viagem finalizada com sucesso')
                        input("click em enter para retornar ao menu!!")
                        return
                input("click em enter para retornar ao menu!!")
                return
        print('Veiculo não encontrado')
        input("click em enter para retornar ao menu!!")
        return
def viagensAtivas():
    print('3 - Viagens Ativas')
    print('{:<17}{:<20}{:<40}'.format('PLACA', 'Tipo', 'Motorista'))
    print('-' * 60)
    for cadastro in baseViagens.values():
        if cadastro.get('status') != False:
            print('{:<17}{:<20}{:<40}'.format(cadastro.get('PLACA'), cadastro.get('TIPO'), cadastro.get('Motorista')))
    print('-' * 60)
    input("click em enter para continual")
    return
def veiculosQueEstaoEmViagem():
    print('-'*10,'Veiculos que estão em Viagem','-'*10)
    print('{:<17}{:<20}{:<40}'.format('PLACA', 'Tipo', 'Motorista'))
    print('-' * 60)
    for cadastro in baseViagens.values():
        if cadastro.get('status') != False:
            print('{:<17}{:<20}{:<40}'.format(cadastro.get('PLACA'), cadastro.get('TIPO'), cadastro.get('Motorista')))
    print('-' * 60)
    input("click em enter para continual")
    return
def veiculosQueEstãoDisponiveisParaViagem():
    print('5 - Veiculos que estão Disponíveis para Viagem')
    print('{:<17}'.format('Placa dos veiculos disponíveis'))
    print('-' * 28)
    for geralVeiculo in baseVeiculo.values():
        if geralVeiculo.get('Disponivel') == True:
            print('{:<17}'.format(geralVeiculo.get('PLACA')))
    print('-------------------------------------')
    input('Aperte qualquer tecla para continuar.')
def listarTodasAsViagens():
    print('-'*10,'Listar todas as viagens','-'*10)
    print('{:<17}{:<20}{:<40}'.format('PLACA', 'TIPO', 'ROTA'))
    print('-' * 45)
    for cadastro in baseViagens.values():
        print('{:<17}{:<20}{:<40}'.format(cadastro.get('PLACA'), cadastro.get('TIPO'), cadastro.get('rota')))
    print('-' * 45)
def listarTodasAsViagensPorPeriodo():
    print('7 - Listar todas as viagens por período') #- data inicial e final (todas as viagens deste período)
    while True:
        inicio=input('Digite data inicial (formato Dia/Mês/Ano): ')
        final=input('Digite data final (formato Dia/Mês/Ano):')
        for viagem in baseViagens.values():
            if viagem.get('status')==True:
                print('{:<17}{:<20}{:<40}'.format('Placa','Data da Viagem'))
                print('-------------------------------------')
                for viagem in baseViagens.values():
                    if inicio<=viagem.get('SAIDA','CHEGADA')<=final:
                        print('{:<17}{:<20}{:<40}'.format(viagem.get('PLACA'), viagem.get('SAIDA'), viagem.get('CHEGADA')))
                print('-------------------------------------')
                input('Aperte qualquer tecla para continuar.')
                return
        print('Nenhuma viagem marcada nesse periodo')
        print('-------------------------------------')
        input('Aperte qualquer tecla para continuar.')
        break
def verificarPLACA(PLACA):
    return (PLACA in baseVeiculo)
def verificarMotorista(Motorista):
    return (Motorista in baseVeiculo)