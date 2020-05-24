function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}

function draw(){
    const canvas = document.getElementById('main_canvas');
    if (canvas.getContext) {
        const ctx = canvas.getContext('2d');

        const divide = 15;
        const length = 750;

        for (let i = 0; i < divide; i++) {
          for (let j = 0; j < divide; j++) {
              ctx.fillStyle = 'rgb(' + getRandomInt(0, 256)+ ',' + getRandomInt(0, 256)+','+getRandomInt(0, 256)+')';
              ctx.strokeRect(j * (length/divide), i * (length/divide), (length/divide), (length/divide));
          }
        }
    } else {
        console.log("KEKW");
    }
}