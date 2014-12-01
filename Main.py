import socket
from thread import *

def process(s):
	print(s)

def main():
	players = []

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(("", 50000))
	sock.listen(5)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	while True:
		c, addr = sock.accept()
		print(addr)

		start_new_thread(threadLoop, (c,))

def threadLoop(c):
	c.send("Started")
	while True:
		process(c.recv(1024))


if (__name__ == "__main__"): main()