chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data)['username']
    let player = document.createElement("div")
    player.className = "col-5 border border-dark rounded p-2 m-1 bg-light";
    player.innerText = data;
    document.getElementById("player-list").appendChild(player);
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};
document.querySelector('#nick-input').focus();
document.querySelector('#nick-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#nick-submit').click();
    }
};

document.getElementById('nick-submit').onclick = function(e) {
    const nick_input = document.querySelector('#nick-input');
    const nickname = nick_input.value;
    chatSocket.send(JSON.stringify({
        'command': 'add_user',
        'username': nickname
    }));
    nick_input.value = '';
    console.log("Wysłano!")
};