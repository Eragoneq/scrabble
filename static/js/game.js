function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}

function draw(){
    const canvas = document.getElementById('main_canvas');
    if (canvas.getContext) {
        const ctx = canvas.getContext('2d');

        const podzial = 11
        const dl = 750

        for (let i = 0; i < podzial; i++) {
          for (let j = 0; j < podzial; j++) {
              ctx.fillStyle = 'rgb(' + getRandomInt(0, 256)+ ',' + getRandomInt(0, 256)+','+getRandomInt(0, 256)+')';
              ctx.strokeRect(j * (dl/podzial), i * (dl/podzial), (dl/podzial), (dl/podzial));
          }
        }
    } else {
        console.log("KEKW");
    }
}