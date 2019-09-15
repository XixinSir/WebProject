
var ball = document.getElementById("ball");
console.log(ball)
//  以对象的形式显示
console.log([ball])

var speedx = 5
var speedy = 5
setInterval(function(){
	
	
	ball.style.left = ball.offsetLeft + speedx + "px";
	ball.style.top = ball.offsetTop + speedy + "px";
	
	console.log(ball.offsetTop)
	if (ball.offsetTop >= 400 - 50 || ball.offsetTop <= 0) {
		speedy *= -1 
	}
	
	if (ball.offsetLeft >= 600 - 50 || ball.offsetLeft <= 0) {
		speedx *= -1 
	}
	
	
}, 10);
