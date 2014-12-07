The server here is very basic, like as basic as it can be.

When a player connects they're given a player number and must wait.
When two players connect and aren't in games they will be paired and informed of their enemy numbers.

When the server receives a pickle, it will respond in pretty much one way.
It will echo the command to all the clients, the clients will pick it up and look at the player number, if it matches the enemy number it will look into it.
Otherwise the command will be ignored.
This means every client will receive data from every other client. I don't think it would be an issue with <100 people playing at a time.

If a player disconnects the server will likely crash, especially if it's do to an error.
But I think an unlimited number could play at the same time as long as none disconnected.

That's as far as I got, but now I understand threading and sockets.

If you'd like to know more about how the game is meant to work just shoot me an email at jsande00@nmt.edu
Have a good winter break!