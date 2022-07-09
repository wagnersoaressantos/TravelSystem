from controleMenus import *
from bdMotoristas import *
from bdVeiculo import *
from bdViagens import *
from dicionarios import *

while True:
    baseGeral=carregarBaseGeral()
    opcao=menuPrincipal()
    if opcao==1:
        while True:
            opcaoMotorista = menuMotorista()
            if opcaoMotorista == 1:
                cadastrarMotorista()
            elif opcaoMotorista == 2:
                buscarMotoristaPorCPF()
            elif opcaoMotorista == 3:
                editarNomeDoMotorista()
            elif opcaoMotorista == 4:
                removerMotorista()
            elif opcaoMotorista == 5:
                listarTodosOsMotoristasPorTipoDaCarteira()
            elif opcaoMotorista == 6:
                listarTodosOsMotorista()
            elif opcaoMotorista == 7:
                break
            else:
                print('Opção Inválida!!!')
                break
    elif opcao==2:
        while True:
            opcaoVeiculo = menuVeiculo()
            if opcaoVeiculo == 1:
                cadastrasVeiculo()
            elif opcaoVeiculo == 2:
                buscarVeiculoPorPlaca()
            elif opcaoVeiculo == 3:
                adicionarMotoristaAoVeiculo()
            elif opcaoVeiculo == 4:
                removerMotoristaDoVeiculo()
            elif opcaoVeiculo == 5:
                listarVeiculosComMotoristas()
            elif opcaoVeiculo == 6:
                listarVeiculosSemMotoristas()
            elif opcaoVeiculo == 7:
                removerVeiculo()
            elif opcaoVeiculo == 8:
                break
            else:
                print('Opção Inválida!!!')
                break
    elif opcao==3:
        while True:
            opcaoViagem = menuViagem()
            if opcaoViagem == 1:
                criarViagem()
            elif opcaoViagem == 2:
                finalizarViagemPorPlaca()
            elif opcaoViagem == 3:
                viagensAtivas()
            elif opcaoViagem == 4:
                veiculosQueEstaoEmViagem()
            elif opcaoViagem==5:
                veiculosQueEstãoDisponiveisParaViagem()
            elif opcaoViagem==6:
                listarTodasAsViagens()
            elif opcaoViagem==7:
                listarTodasAsViagensPorPeriodo()
            elif opcaoViagem == 8:
                break
            else:
                print('Opção Inválida menu baseMotorista')
                break
    elif opcao==4:
        print('Programa foi encerrado')
        compilador()
        break
    else:
        print('Opção Inválida')
        break

#Execultar esse arquivo