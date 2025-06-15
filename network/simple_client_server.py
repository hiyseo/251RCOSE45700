import socket

# 서버 (받는 측)
def run_server():
    server = socket.socket()
    server.bind(('localhost', 12345))
    server.listen(1)
    print("서버 대기 중...")
    conn, addr = server.accept()
    print(f"클라이언트 연결됨: {addr}")
    data = conn.recv(1024).decode()
    print(f"수신된 메시지: {data}")
    conn.send("ACK 받음".encode())
    conn.close()

# 클라이언트 (보내는 측)
def run_client():
    client = socket.socket()
    client.connect(('localhost', 12345))
    client.send("안녕하세요 서버님".encode())
    data = client.recv(1024).decode()
    print(f"서버 응답: {data}")
    client.close()

if __name__ == "__main__":
    mode = input("server 또는 client 중 선택하세요: ").strip()
    if mode == "server":
        run_server()
    elif mode == "client":
        run_client()
    else:
        print("잘못된 모드입니다.")