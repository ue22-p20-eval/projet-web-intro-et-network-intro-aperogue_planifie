from flask import Flask, render_template 
from flask_socketio import SocketIO
from game_backend import Game

app = Flask(__name__)
socketio = SocketIO(app)
game = Game()


@app.route("/")
def index():
    map = game.getMap()
    return render_template("index.html", mapdata=map, n_row=len(map), n_col=len(map[0]) )

@socketio.on("move")
def on_move_msg(json, methods=["GET", "POST"]):
    #Si on a demandé un nouveau joueur :
    if json['dx'] == 10:
        print("New player")
        x,y = game.newP()
        DATA = [[{'i':-100}],[{'x':f"{x}",'y':f"{y}"}]]
        socketio.emit("response", DATA)
    #Si on a demandé de bouger :
    else :
        print("received move ws message")
        dx = json['dx']
        dy = json["dy"]
        p = json['p']
        
        if p == 0: 
            play = game._player
        else :
            play = game.player2

        data, ret = game.move(dx,dy,play)

        DATA = [data,play.lp, play.atk,play.alive,p,game.player2.atk,game.player2.lp,game._player.atk,game._player.lp]
    
        socketio.emit("response", DATA)

if __name__=="__main__":
    socketio.run(app, port=5001, debug=True)