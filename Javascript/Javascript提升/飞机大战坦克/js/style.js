
var mainScreen = document.getElementById("mainScreen")

// 让背景动起来

var jsBg1 = document.getElementById("bg1");
var jsBg2 = document.getElementById("bg2");


var timerBg = setInterval(function() {
	jsBg1.style.top = jsBg1.offsetTop + 1 + "px";
	jsBg2.style.top = jsBg2.offsetTop + 1 + "px";
	
	
	if (jsBg1.offsetTop > 555) {
		jsBg1.style.top = "-550px"
	}
	
	if (jsBg2.offsetTop > 555) {
		jsBg2.style.top = "-550px"
	}

})



// 拖拽效果 


var airplane = document.getElementById("airplane");
// 给飞机添加鼠标按下事件
basex = 0 
basey = 0 

airplane.addEventListener("mousedown", function(e){
	var ev = e || window.event
	basex = ev.pageX;
	basey = ev.pageY
	console.log(basex, basey)
	movex = 0 
    movey = 0
	
	// 给主屏幕添加鼠标移动事件
	mainScreen.addEventListener("mousemove", function(e){
		var en = e || window.event
		movex = en.pageX - basex;
	    basex = en.pageX
		movey = en.pageY - basey
		basey = en.pageY
		airplane.style.left = airplane.offsetLeft + movex + "px";
		airplane.style.top = airplane.offsetTop + movey + "px";
	}, false)
}, false) 


// 发射子弹 
var timerBullent = setInterval(function() {
	// 创建子弹
	var bullent = document.createElement("div");
	bullent.className = "bullent";
	bullent.style.left = airplane.offsetLeft + 47 + "px";
	bullent.style.top= airplane.offsetTop - 23 + "px";
	mainScreen.appendChild(bullent)
	// 让子弹飞
	// 如果超出屏幕 就将此元素删除
	var timerBullentFly = setInterval(function() {
		bullent.style.top = bullent.offsetTop - 10 + "px";
		if (bullent.offsetTop <= -20) {
			clearInterval(timerBullentFly);
			mainScreen.removeChild(bullent)
		}
	}, 50)
}, 1000)



// 敌人下落 
var timertank = setInterval(function() {
	// 创建子弹
	var tank = document.createElement("div");
	tank.className = "tank";
	tank.style.left = randomNum(0, 332) + "px";
	tank.style.top = "0px"
	mainScreen.appendChild(tank)
	// 让坦克飞
	// 如果超出屏幕 就将此元素删除
	var timerBullentFly = setInterval(function() {
		tank.style.top = tank.offsetTop + 10 + "px";
		if (tank.offsetTop >= 555) {
			clearInterval(timerBullentFly);
			mainScreen.removeChild(tank)
		}
	}, 50)
}, 1000)