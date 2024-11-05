# -*- coding: utf-8 -*-
"""
Lab3 - Servidor e Cliente Web

Docente: João Costa (joaojdacosta@gmail.com)
Outubro, 2024.
"""

from socket import *  # importa o módulo socket
import sys  # Para terminar o programa

# Cria um socket do servidor TCP
# (AF_INET é utilizado para o protocolo IPv4)
# (SOCK_STREAM é utilizado para o TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Atribui o número de porta
serverPort = 6789

# TODO #1: Vincular o socket ao endereço e porta do servidor
# Preencha o início
serverSocket.bind(('', serverPort))
# Preencha o fim

# TODO #2: Escutar, no máximo, 1 conexão por vez
# Preencha o início
serverSocket.listen(1)
# Preencha o fim

# O servidor deve estar Up, em execução e a escuta
# por novas conexões
while True:
    print('O servidor está pronto para receber')

    # TODO #3: Configurar uma nova conexão do cliente
    # Preencha o início
    connectionSocket, addr = serverSocket.accept()
    # Preencha o fim

    # Se ocorrer uma excepção durante a execução da cláusula try
    # o resto da cláusula é ignorado
    # Se o tipo de exceção corresponder à palavra após except
    # a cláusula except é executada
    try:
        # TODO #4: Receber a mensagem de solicitação do cliente
        # Preencha o início
        message = connectionSocket.recv(1024).decode()
        # Preencha o fim

        # Extrai o caminho do objeto solicitado da mensagem
        # O caminho é a segunda parte do cabeçalho HTTP,
        # identificado por [1]
        filename = message.split()[1]

        # O caminho extraído da solicitação HTTP inclui
        # um caractere '\', lemos o caminho do
        # segundo caractere
        f = open(filename[1:])

        # Armazena todo o conteúdo do ficheiro solicitado
        # em um buffer temporário
        outputdata = f.read()

        # TODO #5: Enviar a linha de cabeçalho de resposta HTTP
        # para o socket de conexão
        # Preencha o início
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        # Preencha o fim

        # Envia o conteúdo do ficheiro solicitado
        # para o socket de conexão
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Fecha o socket de conexão do cliente
        connectionSocket.close()

    except IOError:
        # TODO #6: Enviar mensagem de resposta HTTP para ficheiro não encontrado
        # Preencha o início
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        # Preencha o fim

        # TODO #7: Fechar o socket de conexão do cliente
        # Preencha o início
        connectionSocket.close()
        # Preencha o fim

# Fecha o socket do servidor ao encerrar o programa
serverSocket.close()
sys.exit()  # Encerra o programa após enviar os dados correspondentes
