import socket
import sys

HOST = socket.gethostbyname('localhost')
PORT = 4000
# host = '133.14.234.245'
# host = '133.20.178.81'
if len(sys.argv) > 1:
    PORT = int(sys.argv[1])
name = "えるざっぷ"
if len(sys.argv) > 2:
    name = sys.argv[2]
if len(sys.argv) > 3:
    HOST = socket.gethostbyname(sys.argv[3])


data = '{"SSIDs":["TDU_MRCL_WLAN_DOT1X","TDU_MRCL_WLAN","eduroam","TDU_MRCL_GUEST","Buffalo-G-3658"], "name":"%(name)s"}' % locals()

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")
finally:
    sock.close()

res_data = received.encode('UTF-8')
print("Sent:     {}".format(data))
print("Received: {}".format(res_data))
