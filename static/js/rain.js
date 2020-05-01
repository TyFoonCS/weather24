function random(min, max) {
    var rand = min + Math.random() * (max + 1 - min);
    rand = Math.floor(rand);
return rand;
}

for (var i=0; i<200; i++) {
    document.getElementsByTagName('body')[0].innerHTML += '<i class="rain" style="left: '+random(-2000, 2000)+'px;transform: translate3d(0, 0, 0);animation-delay: '+(0.01 * i)+'s"></i>';
}