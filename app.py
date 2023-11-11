import os
def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo a AlmirNet.com')
    # pedir o nome
    nome = input('Digite seu nome: ')
    # pedir o e-mail
    email = input('Digite seu e-mail: ')
    # Oferecer o menu de opções
    input(f'O que gostaria de saber hoje?{os.linesep}[1] - Vale a pena aprender Python?
          {os.linesep}')
    # Processar a resposta enviar
if __name__ == '__main__':
    start()