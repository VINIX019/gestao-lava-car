from datetime import datetime, timedelta
menu = '''
--- Lava car ---
Carro pequeno[1]
Carro medio[2]
Carro grande[3]
Carro de Luxo[4]
Sair[5]
---------------
'''
def carro_pequeno():
    carro_p = 30
        
    data_atual = datetime.now()
    data_prevista = data_atual + timedelta(minutes=carro_p)
    data_formatada = data_atual.strftime('%d/%m/%Y %H:%M')
    data_prevista_formatada = data_prevista.strftime('%d/%m/%Y %H:%M')
    
    valor = float(input('Digite o valor do servico: R$'))
    
    print(f'''
          ---Extrato de Serviço---
          Carro Pequeno
          Inicio do Serviço:  {data_formatada}
          Entrega Prevista:   {data_prevista_formatada}
          Duracao do servico: {carro_p} minutos
          
          
          Valor:              R${valor:.2f}  
          ''')
    
def carro_medio():
    carro_m = 45
    
    data_atual = datetime.now()
    data_prevista = data_atual + timedelta(minutes=carro_m)
    data_formatada = data_atual.strftime('%d/%m/%Y %H:%M')
    data_prevista_formatada = data_prevista.strftime('%d/%m/%Y %H:%M')
    
    valor = float(input('Digite o valor do servico: R$'))
    
    print(f'''
          ---Extrato de Serviço---
          Carro Medio
          Inicio do Serviço:  {data_formatada}
          Entrega Prevista:   {data_prevista_formatada}
          Duracao do servico: {carro_m} minutos
          
          
          Valor:              R${valor:.2f}  
          ''')
def carro_grande():
    carro_g = 60
    data_atual = datetime.now()
    data_prevista = data_atual + timedelta(minutes=carro_g)
    data_formatada = data_atual.strftime('%d/%m/%Y %H:%M')
    data_prevista_formatada = data_prevista.strftime('%d/%m/%Y %H:%M')
    
    valor = float(input('Digite o valor do servico: R$'))
    
    print(f'''
          ---Extrato de Serviço---
          Carro Grande
          Inicio do Serviço:  {data_formatada}
          Entrega Prevista:   {data_prevista_formatada}
          Duracao do servico: {carro_g} minutos
          
          
          Valor:              R${valor:.2f}  
          ''')
    
def carro_luxo():
    carro_l = 90
    data_atual = datetime.now()
    data_prevista = data_atual + timedelta(minutes=carro_l)
    data_formatada = data_atual.strftime('%d/%m/%Y %H:%M')
    data_prevista_formatada = data_prevista.strftime('%d/%m/%Y %H:%M')
    
    valor = float(input('Digite o valor do servico: R$'))
    
    print(f'''
          ---Extrato de Serviço---
          Carro de Luxo
          Inicio do Serviço:  {data_formatada}
          Entrega Prevista:   {data_prevista_formatada}
          Duracao do servico: {carro_l} minutos
          
          
          Valor:              R${valor:.2f}  
          ''')
while True:
        opcao = int(input(f'{menu}\n Digite qual carro deseja:'))
        if opcao == 1:
            carro_pequeno()
        elif opcao == 2:
            carro_medio()
        elif opcao == 3:
            carro_grande()
        elif opcao == 4:
            carro_luxo()
        elif opcao == 5:
            print('Obrigado!')
            break
        else:
            print('Digite um valor valido!')