import socket
if __name__ == '__main__':
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    tcp_server_socket.bind(("",9090))
    tcp_server_socket.listen(128)
    new_client,ip_port=tcp_server_socket.accept()
    print("客户端ip和端口号",ip_port)
    recv_data=new_client.recv(1024)
    recv_content=recv_data.decode("gbk")

    tcp_server_socket.close()

