import os 

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} É bastante útil e paga muito bem. Futuramente, vai ser utilizado.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} É bastante útil e paga muito bem. Futuramente, vai ser utilizado.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} É bastante útil e paga muito bem. Futuramente, vai ser utilizado.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} É bastante útil e paga muito bem. Futuramente, vai ser utilizado.{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')
        

def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo a AlmirNet.com')
    # pedir o nome
    nome = input('Digite seu nome: ')
    # pedir o e-mail
    email = input('Digite seu e-mail: ')
    
    while True:
        # Oferecer o menu de opções
        resposta = input(f'''O que gostaria de saber hoje?{os.linesep}
        [1] - Vale a pena aprender Python?{os.linesep}
        [2] - Quanto tempo leva para conseguir um emprego com Python?{os.linesep}
        [3] - Quando vou saber que estou BOM o suficiente para conseguir um emprego?{os.linesep}
        [4] - Onde me recomenda estudar Python para conseguir um emprego hoje?{os.linesep}
        ''')

        if resposta in ['1', '2', '3', '4']:
            processar_resposta(resposta, nome)
            break  # Sai do loop após processar a resposta válida
        else:
            print('Digite apenas 1, 2, 3 ou 4')

if __name__ == '__main__':
    start()
