
var jsBox = document.getElementById("box");
var jsPic = document.getElementById("pic");
var jsLeft = document.getElementById("left");
var jsRight = document.getElementById("right");

var jsLisArr = document.getElementsByTagName("li");



// 第一个li设置为红色
 jsLisArr[0].style.backgroundColor = "red";


//  启动一个定时器去更换jspic中的src属性(切换图片)
var currentPage = 1 
var timer = setInterval(startLoop, 1000)


function startLoop() {
	currentPage ++ 
	changaPage()
}


function changaPage() {
	if (currentPage == 9) {
		currentPage = 1
	} else if (currentPage == 0) {
		currentPage = 8 
	}
	console.log(currentPage)
	jsPic.src = "img/" + currentPage + ".jpg"
	
	// 清空所有小圆点的颜色
	for (var  i = 0; i< jsLisArr.length; i ++) {
		jsLisArr[i].style.backgroundColor = "#aaa"
	}
	jsLisArr[currentPage - 1].style.backgroundColor = "red";
}


// 鼠标进入box 定时器停止  显示左右的两个 
jsBox.addEventListener("mouseover", overFunc, false);


// 鼠标出来 重启定时器 
jsBox.addEventListener("mouseout", outFunc, false)


function overFunc() {
	// 停止定时器
	clearInterval(timer)
	// 显示左右按钮 
	jsLeft.style.display = "block";
	jsRight.style.display = "block";
}

function outFunc() {
	// 重启定时器
	timer = setInterval(startLoop, 1000)
	
	// 隐藏左右按钮
	jsLeft.style.display = "none";
	jsRight.style.display = "none";
}



// 点击左右按钮 
jsLeft.addEventListener("mouseover", deep, false);
jsRight.addEventListener("mouseover", deep, false);
function deep() {
	this.style.backgroundColor = "rgba(0, 0, 0, 0.6)"
}

jsLeft.addEventListener("mouseout", nodeep, false);
jsRight.addEventListener("mouseout", nodeep, false);
function nodeep() {
	this.style.backgroundColor = "rgba(0, 0, 0, 0.2)"
}


jsRight.addEventListener("click", function() {
	currentPage ++ 
	changaPage() 
}, false)


jsLeft.addEventListener("click", function() {
	currentPage --
	changaPage() 
}, false)



// 进入小圆点
for (var i = 0; i < jsLisArr.length; i ++) {
	jsLisArr[i].index = i + 1;
	jsLisArr[i].addEventListener("mouseover", function() {
		// currentPage = parseInt(this.innerHTML)
		currentPage = parseInt(this.index)
		changaPage();
	}, false)
}

