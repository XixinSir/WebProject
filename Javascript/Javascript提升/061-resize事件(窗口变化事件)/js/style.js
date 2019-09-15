// 窗口大小改变会触发resize事件

window.onresize = function() {
	// 浏览器窗口的宽和高  不同的浏览器用到不一样
	// 高度是除了调试模式的窗口  页面其余的高度
	width = document.documentElement.clientWidth || document.body.clientWidth || window.innerWidth;
	height = document.documentElement.clientHeight || document.body.clientHeight || window.innerHeight;
	console.log(width, height)
	
}