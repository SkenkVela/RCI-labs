# -*- coding: utf-8 -*-
"""
Lab3 - Cliente Web

Docente: João Costa (joaojdacosta@gmail.com)
Outubro, 2024.
"""

import socket

def web_client(server_ip, server_port, file_path):
    # Cria um socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta ao servidor
    client_socket.connect((server_ip, server_port))
    print("Conectado ao servidor {}:{}".format(server_ip, server_port))

    # Formata a requisição HTTP GET
    request = "GET {} HTTP/1.1\r\nHost: {}\r\n\r\n".format(file_path, server_ip)
    client_socket.sendall(request.encode())
    print("Solicitação enviada: {}".format(request))

    # Recebe a resposta do servidor
    response = client_socket.recv(4096)  # 4096 bytes por leitura
    print("Resposta do servidor:")
    print(response.decode())

    # Fecha o socket
    client_socket.close()

# Exemplo de uso
server_ip = '192.168.56.21'  # IP do servidor
server_port = 6789           # Porta do servidor
file_path = '/index.html'     # Caminho do arquivo solicitado

web_client(server_ip, server_port, file_path)
