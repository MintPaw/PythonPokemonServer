import socket
import pickle
from _thread import *

connections = []
needGame = []

def process(d):
	print(d)

	if d["mType"] == "move":
		broadcast(d)

	if d["mType"] == "start":
		d["mType"] = "playerData"
		broadcast(d)

def makeGame():
	global needGame
	global connections

	con1 = needGame.pop(0)
	con2 = needGame.pop(0)

	data = {}
	data["mType"] = "start"
	data["players"] = [connections.index(con1), connections.index(con2)]

	print("Game was made between players " + str(data["players"][0]) + " and " + str(data["players"][1]))

	broadcast(data)

def main():
	global connections
	global needGame

	print("Server started")

	players = []

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(("localhost", 50000))
	sock.listen(5)

	while True:
		c, addr = sock.accept()

		connections.append(c)
		needGame.append(c)

		print("A player has connected")

		data = {}
		data["mType"] = "init"
		data["playerNumber"] = len(connections) - 1

		c.send(pickle.dumps(data))

		start_new_thread(threadLoop, (c,))

		if (len(needGame) >= 2): makeGame()

def broadcast(p):
	for i in connections: i.send(pickle.dumps(p))

def threadLoop(c):
	while True:
		process(pickle.loads(c.recv(4096)))


if (__name__ == "__main__"): main()