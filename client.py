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

SERVER_PORT = 8000  # constant


def connecting():
    """
        This function will ask for the ip address to
         connected with the server
    :return: a new socket connection

    """
    value = input("Press the ip address to start the chat:\n")
    confirmation = input(f"\nThe destination is: {value}. Is that correct?"
                         f"\n1-Yes \n2-No\n")
    if confirmation is False:
        print('Ending...')
        exit()

    return start_connection(value)


def checking_ip_address(ip_address):
    """
        Verification function for the ip_address
    :param ip_address:
    :return: True or exit
    """

    if len(ip_address) == 9 and ip_address is not None:
        return True
    print("Ending the program... Check if the ip address is corrected")
    exit()


def start_connection(ip_address):
    """
        This function will establish the connection with the server
    :param ip_address:
    :return: tcp connection
    """
    print('Trying to connect to the server...')
    checking_ip_address(ip_address)
    tcp_connection = socket.socket(
                        socket.AF_INET,
                        socket.SOCK_STREAM)

    destiny = (ip_address, SERVER_PORT)
    try:
        tcp_connection.connect(destiny)
    except ConnectionError as error:
        print("Connection refused. Try again!\n"
              f"Type of error: {type(error)}")

    # everything is ok
    return tcp_connection


def close_connection(tcp_connection):
    print("Ending the tcp connection...")
    tcp_connection.close()


def conversation(tcp_connection):

    print("Starting the chat!\n\nObs: To exit the conversation press: exit")
    message = None
    message_one = input("You: ")
    tcp_connection.send(bytes(message_one, "utf8"))

    while True:
        recv_message = tcp_connection.recv(1024).decode("ascii")

        # se tiver mensagem exibe
        if recv_message is not None:
            print(f"Server message: {recv_message}")
        else:
            message = input("You: ")

        #se tiver input envia
        if message is not None:
            tcp_connection.send(bytes(message, "utf8"))
            if message == 'exit':
                break

    print("Exiting...")
    close_connection(tcp_connection)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to the chat with socket communication!\n")
    connection = connecting()
    conversation(connection)

    # if the connection wasn't closed
    try:
        connection.close()
    except ConnectionError as err:
        print("The TCP Connection is end")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
