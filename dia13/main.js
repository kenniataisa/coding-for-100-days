setInterval (atualizarClock, 1000);
function atualizarClock(){
  var data = new Date();
  var hora = data.getHours();
  var min = data.getMinutes();
  var seg = data.getSeconds();

  if(hora < 10){
    hora = '0' + hora
  }

  if(min < 10){
    min = '0' + min
  }

  if(seg < 10){
    seg = '0' + seg
  }

  var clock_digital = hora + ':' + min + ':' + seg; 
  document.getElementById('clock').innerHTML = clock_digital;

}

atualizarClock();
