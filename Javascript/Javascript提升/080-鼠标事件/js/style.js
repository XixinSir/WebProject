

var lis = document.getElementsByTagName("li");
console.log(lis)

for (var i = 0; i < lis.length; i++) {
	
	// 鼠标进入
	lis[i].addEventListener("mouseover", function() {
		this.style.backgroundColor = "red"
	}, false)
	
	
	// 鼠标离开
	lis[i].addEventListener("mouseout", function() {
		this.style.backgroundColor = "blue"
	}, false)
	
	
	// 鼠标按下
	lis[i].addEventListener("mousedown", function() {
		this.style.fontSize = parseInt(getComputedStyle(this, null).fontSize) * 2 + "px";
	}, false)
	
	
	// 鼠标抬起
	lis[i].addEventListener("mouseup", function() {
		this.style.fontSize = parseInt(getComputedStyle(this, null).fontSize) / 2 + "px";
	}, false)

	
	// 鼠标移动
	document.addEventListener("mousemove", function() {
		console.log("鼠标在移动");
	}, false)
}