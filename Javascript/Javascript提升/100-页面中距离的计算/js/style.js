

var mainScreen = document.getElementById("box");
var Leftbox = document.getElementById("left")

mainScreen.addEventListener("mousedown", function(e) {
	var evt = e || window.event;
	// evt.clientX是相对文档的水平座标 
	console.log("mainScreen.clientX: " + evt.clientX);
	console.log("mainScreen.clientY: " + evt.clientY);
	// pageX是相对文档的水平坐标  和clientX有类似的地方
	console.log("mainScreen.pageX: " + evt.pageX);
	console.log("mainScreen.pageX: " + evt.pageY);
	// offsetX是点击的地方距离其标签的X方向的距离
	console.log("mainScreen.offsetX: " + evt.offsetX);
	console.log("mainScreen.offsetY: " + evt.offsetY);
	/* offsetHeight  控件自身的高度
	offsetWidth   控件自身的宽度
	offsetLeft   左边距离父级控件的距离
	offsetTop    上边距离父级控件的距离*/
	console.log("mainScreen.offsetHeight: ", mainScreen.offsetHeight)
	console.log("mainScreen.offsetWidth: ", mainScreen.offsetWidth)
	console.log("mainScreen.offsetLeft: ", mainScreen.offsetLeft)
	console.log("mainScreen.offsetTop: ", mainScreen.offsetTop)
}, false)


Leftbox.addEventListener("click", function() {
	/* offsetHeight  控件自身的高度
	offsetWidth   控件自身的宽度
	offsetLeft   左边距离父级控件的距离
	offsetTop    上边距离父级控件的距离*/
	console.log("Leftbox.offsetHeight: ", Leftbox.offsetHeight)
	console.log("Leftbox.offsetWidth: ", Leftbox.offsetWidth)
	console.log("Leftbox.offsetLeft: ", Leftbox.offsetLeft)
	console.log("Leftbox.offsetTop: ", Leftbox.offsetTop)
	console.log(this.style.top)
	
}, false)