import socket
import random
from datetime import datetime

MAX_PACKET = 1024
QUEUE_LEN = 1
NAME = 'useless server'
now = datetime.now()
current_hour = now.strftime("%H:%M:%S")


def time():
    return current_hour


def rand():
    random_num = random.randint(1, 11)
    return str(random_num)


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        my_socket.bind(('0.0.0.0', 1729))
        my_socket.listen(QUEUE_LEN)
        while True:
            client_socket, client_address = my_socket.accept()
            try:
                request = client_socket.recv(MAX_PACKET).decode()
                if request == 'rand':
                    client_socket.send(rand().encode())
                elif request == 'name':
                    client_socket.send(NAME.encode())
                elif request == 'exit':
                    print('Closing server.')
                    return
                elif request == 'time':
                    client_socket.send(time().encode())
                else:
                    client_socket.send('not a valid command'.encode())

            except socket.error as err:
                print('received socket error on client socket' + str(err))
            finally:
                client_socket.close()
    except socket.error as err:
        print('received socket error on server socket' + str(err))
    finally:
        my_socket.close()


if __name__ == '__main__':
    main()