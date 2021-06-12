window.addEventListener("DOMContentLoaded", (event) => {
    var socket = io.connect("http://" + document.domain + ":" + location.port );

    document.onkeydown = function(e){
        switch(e.keyCode){
            case 37:
                socket.emit("move", {dx:-1, dy:0});
                
                break;
            case 38:
                socket.emit("move", {dx:0, dy:-1});
                
                break;
            case 39:
                socket.emit("move", {dx:1, dy:0});
                
                break;
            case 40:
                socket.emit("move", {dx:0, dy:1});
                
                break;
        }


    };
    
    var btn_n = document.getElementById("go_n");
    btn_n.onclick = function(e) {
        console.log("Clicked on button north");
        socket.emit("move", {dx:0, dy:-1});
        
    };

    var btn_s = document.getElementById("go_s");
    btn_s.onclick = function(e) {
        console.log("Clicked on button south");
        socket.emit("move", {dx:0, dy:1});
        
    };

    var btn_w = document.getElementById("go_w");
    btn_w.onclick = function(e) {
        console.log("Clicked on button w");
        socket.emit("move", {dx:-1, dy:0});
        
    };

    var btn_e = document.getElementById("go_e");
    btn_e.onclick = function(e) {
        console.log("Clicked on button e");
        socket.emit("move", {dx:1, dy:0});
        
    };
    
    function component(element, x, y) { /* Draw an image with x and y the coordinates of the NW point */
        ctx = myGameArea.context;
        
        ctx.drawImage(element,x, y);
    }

    socket.on("response", function(DATA){
        console.log(DATA);
        data = DATA[0]

        for( var p=0; p<2; p++){
            var pos_x = data[p].j;
            var pos_y = data[p].i;
            var element = data[p].content; 
            component(Table_eq.get(element),pos_x*res,pos_y*res);

            
        }
        
        /* New : */
        var LP = document.getElementById("lp")
        LP.textContent = DATA[1]
        var atk = document.getElementById("atk")
        atk.textContent = DATA[2]

        if( DATA[3] == false ) /* a modif*/
        {
            var div_to_hide = document.getElementById("flexbox")
            div_to_hide.style.display = 'none';
            var game_over = document.getElementById("game_over");
            game_over.style.display = 'flex';
        }
    });

});