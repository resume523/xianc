import socket

if __name__ == '__main__':
    tcp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_client_socket.connect("192.168.22.78",9090)
    send_content="你好，我是客户端小白"
    send_data=send_content.encode("utf-8")
    tcp_client_socket.send(send_data)
    recv_data=tcp_client_socket.recv(1024)
    print(recv_data)
    tcp_client_socket.close()
