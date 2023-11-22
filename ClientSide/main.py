"""
Author: Ido Karadi
Program Name: Cyber2.6
Desc: Server&Client sides of a basic 4 command server
Date: 14/11/23
"""
import socket

MAX_PACKET = 1024

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def main():
    """
    Client main function: connects to server and receives user input for server command. Disconnects after command.
    """
    try:
        my_socket.connect(('127.0.0.1', 1729))
        my_socket.send(input('Choose a command: ').encode())
        response = my_socket.recv(MAX_PACKET).decode()
        print(response + '\nDisconnecting from server...')
    except socket.error as err:
        print('received socket error ' + str(err))
    finally:
        my_socket.close()


if __name__ == '__main__':
    main()