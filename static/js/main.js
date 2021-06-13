window.addEventListener("DOMContentLoaded", (event) => {
    var socket = io.connect("http://" + document.domain + ":" + location.port );

    /*Pour le player1*/
    document.onkeydown = function(e){
        switch(e.keyCode){
            case 37:
                socket.emit("move", {dx:-1, dy:0, p:0}); /* On met p:0 pour player1 sinon p:1*/
                
                break;
            case 38:
                socket.emit("move", {dx:0, dy:-1, p:0});
                
                break;
            case 39:
                socket.emit("move", {dx:1, dy:0, p:0});
                
                break;
            case 40:
                socket.emit("move", {dx:0, dy:1, p:0});
                
                break;

            /*Pour le player2 on utilise les touches zqsd*/ 
            case 81:
                socket.emit("move", {dx:-1, dy:0, p:1}); /* On met p:1 pour player2*/
                
                break;
            case 90:
                socket.emit("move", {dx:0, dy:-1, p:1});
                
                break;
            case 68:
                socket.emit("move", {dx:1, dy:0, p:1});
                
                break;
            case 83:
                socket.emit("move", {dx:0, dy:1, p:1});
                
                break;
        }


    };
    
    var btn_n = document.getElementById("go_n");
    btn_n.onclick = function(e) {
        console.log("Clicked on button north");
        socket.emit("move", {dx:0, dy:-1, p:0});
        
    };

    var btn_s = document.getElementById("go_s");
    btn_s.onclick = function(e) {
        console.log("Clicked on button south");
        socket.emit("move", {dx:0, dy:1, p:0});
        
    };

    var btn_w = document.getElementById("go_w");
    btn_w.onclick = function(e) {
        console.log("Clicked on button w");
        socket.emit("move", {dx:-1, dy:0, p:0});
        
    };

    var btn_e = document.getElementById("go_e");
    btn_e.onclick = function(e) {
        console.log("Clicked on button e");
        socket.emit("move", {dx:1, dy:0, p:0});
        
    };

    
    
    var btn_nb = document.getElementById("go_nb");
    btn_nb.onclick = function(e) {
        console.log("Clicked on button north");
        socket.emit("move", {dx:0, dy:-1, p:1});
        
    };

    var btn_sb = document.getElementById("go_sb");
    btn_sb.onclick = function(e) {
        console.log("Clicked on button south");
        socket.emit("move", {dx:0, dy:1, p:1});
        
    };

    var btn_wb = document.getElementById("go_wb");
    btn_wb.onclick = function(e) {
        console.log("Clicked on button w");
        socket.emit("move", {dx:-1, dy:0, p:1});
        
    };

    var btn_eb = document.getElementById("go_eb");
    btn_eb.onclick = function(e) {
        console.log("Clicked on button e");
        socket.emit("move", {dx:1, dy:0, p:1});
        
    };

    var btn_newplayer = document.getElementById("New Player");
    btn_newplayer.onclick = function(e){
        console.log("New Player")
        socket.emit("move", {dx:10, dy:10}); /* On ne peut pas donner de mouvements +10 +10 autrement que
        par ce bouton*/
    }

    socket.on("response", function(DATA){
        console.log(DATA);
        data = DATA[0]

        if (data[0] == undefined) {
            console.log("Mur ou personne")
            var LP = document.getElementById("lp")
            LP.textContent = DATA[8]
            var atk = document.getElementById("atk")
            atk.textContent = DATA[7]
            var LP = document.getElementById("lp2")
            LP.textContent = DATA[6]
            var atk = document.getElementById("atk2")
            atk.textContent = DATA[5]
        }
        else if (data[0].i == -100) {
            var NP = document.getElementById("New Player")
            NP.style.display = "none";
            var pos_x = DATA[1][0].x;
            var pos_y = DATA[1][0].y;            
            myGameArea.context.drawImage(Table_eq.get("G"),pos_x*res,pos_y*res);
            var tab2 = document.getElementById("tab2");
            tab2.innerHTML = "Player2 <br> Use zqsd";
            

        }
        else {
            
            var LP = document.getElementById("lp")
            LP.textContent = DATA[8]
            var atk = document.getElementById("atk")
            atk.textContent = DATA[7]
            var LP = document.getElementById("lp2")
            LP.textContent = DATA[6]
            var atk = document.getElementById("atk2")
            atk.textContent = DATA[5]

            
    
            for( var p=0; p<2; p++){
                var pos_x = data[p].j;
                var pos_y = data[p].i;
                var element = data[p].content; 
                myGameArea.context.drawImage(Table_eq.get(element),pos_x*res,pos_y*res);
    
                
            }
        }
        
        
        
        if( DATA[3] == false ) /* Si le joueur est mort*/
        {

            var jeu = document.getElementsByTagName("canvas");
            for(var o=0;o < jeu.length;o++){
                jeu[o].style.display = 'none';
            } 
            var fleche = document.getElementById("fleche")
            fleche.style.display = "none";

            var game_over = document.getElementById("game_over");
            game_over.style.display = "flex";
            if (DATA[4] ==0) {
                game_over.textContent = "Game Over for player 1"
            } else {
                game_over.textContent = "Game over for player 2"
            }

            
            
        }
    });

});