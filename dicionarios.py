import json
import os
baseGeral={}
baseMotorista={}
baseVeiculo={}
baseViagens={}
def compilador():
    geral={'Motorista':baseMotorista,'Veiculo':baseVeiculo,'Viagens':baseViagens}
    baseGeral=geral
    gravar(baseGeral)
    for k,v in baseGeral.items():
        return k,'é',v
    return

def gravar(baseGeral):
    with open('baseGeral.json','w') as f:
        json.dump(baseGeral,f,indent=4)
def carregarBaseGeral():
    if os.path.exists('baseGeral.json'):
        with open ('baseGeral.json','r') as f:
            baseGeral=json.load(f)
            motorista={}
            veiculo={}
            viagens={}
            motorista.update(baseGeral['Motorista'])
            veiculo.update(baseGeral['Veiculo'])
            viagens.update(baseGeral['Viagens'])
            baseMotorista.update(motorista)
            baseVeiculo.update(veiculo)
            baseViagens.update(viagens)
    return