//获取滚动高度 
function $scrollTop() {
	return document.documentElement.scrollTop || document.body.scrollTop;
}

// 根据id获取元素节点
function $(idName) {
	return document.getElementById(idName);
}

// 获取可视化窗口的宽度
function $w() {
	return document.body.width || document.documentElement.width || window.innerWidth;
}


// 获取可视化窗口的高度
function $h() {
	return document.body.height || document.documentElement.height || window.innerHeight;
}


// 随机颜色
function randomColor() {
	// rgb(255, 255, 255)
	var r = parseInt(Math.random() * 256);
	var g= parseInt(Math.random() * 256);
	var b = parseInt(Math.random() * 256);
	return "rgb(" + r + "," + g + "," + b + ")";
	// "#ffffff"
}


// 获取内部样式表  外部样式表中属性的属性值
// obj --> 元素节点
// at  --> 属性名
function getStyle(obj, at) {
	if (obj.currentStyle) {
		// IE
		return obj.currentStyle[at]
	}else {
		return window.getComputedStyle(obj, null)[at];
	}
}





var jsDiv = $("box");
console.log(jsDiv);

// 改变颜色
document.onkeydown = function(e) {
	var evt = e || window.event;
	// shift为true 并且按下的是C 
	if (evt.shiftKey == true && evt.key == "c".toUpperCase()) {
		jsDiv.style.backgroundColor = randomColor()
	}
}


// 移动
document.addEventListener("keydown", funcMove, false);
function funcMove(e) {
	var evt = e || window.event;
	
	switch (e.keyCode){
		case 37:
			jsDiv.style.left = jsDiv.offsetLeft - 5 + "px";
			break;
		case 38:
			jsDiv.style.top = jsDiv.offsetTop - 5 + "px";
			break;
		case 39:
			jsDiv.style.left = jsDiv.offsetLeft + 5 + "px";
			break;
		case 40:
			jsDiv.style.top = jsDiv.offsetTop + 5 + "px";
			break;
		default:
			break;
	}
	0
}