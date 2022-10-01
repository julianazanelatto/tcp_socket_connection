"""
    Este tutorial visa realizar a comunicação entre cliente e servivdor
    por meio de socket TCP na camada de transporte do modelo TCP/IP. Dessa forma a função
    connecting busca o endereço de IP que é parâmetro para realizar a connexão com o servidor.


    Este projeto está dentro do paradigma procedural. Portanto, para construir um programa OO
    deve-se inserir as funções dentro da classe

    Socket lib python
    https://docs.python.org/3/library/socket.html

    Para mais informações acesso o site
    www.simplificandoredes.com
"""
import socket

SERVER_IP = ''   # listen in all the interfaces
SERVER_PORT = 8000  # connection port
BUFFER = 1024  # receiving buffer for messages


def bind_to_the_server():
    """
        This function connect the application to the server. Therefore, establish the binding
        between the server and application.
    :return: tcp socket connection

    """
    tcp_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server = (SERVER_IP, SERVER_PORT)
    tcp_connection.bind(socket_server)
    tcp_connection.listen(1)

    # continue or exit?
    close_connection()

    return tcp_connection


def client_confirmation(tcp_connection):
    """
        Client confirmation to proceed with the communication
    :param tcp_connection:
    :return:
    """
    connection, ip_client = current_connection.accept()
    print(f"\nThe client with {ip_client} ip has connected\n")
    return ip_client


def close_connection(tcp_connection):
    """
        This function defines whether the program continues or exits
    :param tcp_connection:

    """
    option = input("Do you wanna close the connection (1-Y, 0-N)? ")

    if option is True:
        # closing and exiting the program
        print("Ending the connection and exit the program...")
        tcp_connection.close()
        exit()


def listening(tcp_connection, ip_client):
    """
        This function listen to the channel looking for messages.
    :param tcp_connection:
    :param ip_client:
    :return: the messages through the print function

    """
    print("If you wanna terminate the connection type exit\n")
    while True:
        recv_message = tcp_connection.recv(BUFFER)
        if recv_message is not None and recv_message != 'exit':
            print(f" Client {ip_client} message:\n {recv_message}")
        if recv_message == 'exit':
            # The client can terminate the connection
            close_connection()

    # else: do nothing


if __name__ == '__main__':
    """
        This main function will interate with the client through the tcp connection
        made by the bind_to_the_server()
    """
    current_connection = bind_to_the_server()
    client = client_confirmation(current_connection)
    listening(current_connection, client)

    # if the connection wasn't closed
    try:
        current_connection.close()
    except ConnectionError as err:
        # the connection is already closed
        pass
    exit()
