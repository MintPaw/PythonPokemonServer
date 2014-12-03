import socket
from _thread import *

playerNumber = 0
connections = []
needGame = []

def process(s):
	debugPrint(s.decode("utf-8"))

def debugPrint(m):
	print(m)

def makeGame():
	global needGame
	global connections

	con1 = needGame.pop(0)
	con2 = needGame.pop(0)

	connections.pop(connections.index(con1))
	connections.pop(connections.index(con2))

def main():
	global connections
	global needGame

	players = []

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(("localhost", 50000))
	sock.listen(5)

	while True:
		c, addr = sock.accept()

		connections.append(c)
		needGame.append(c)

		if (len(needGame) >= 2): makeGame()

		start_new_thread(threadLoop, (c,))

def threadLoop(c):
	global playerNumber

	c.send(str("playerNumber:" + str(playerNumber)).encode("utf-8"))
	debugPrint("A player has connected")

	playerNumber += 1

	while True:
		process(c.recv(1024))


if (__name__ == "__main__"): main()