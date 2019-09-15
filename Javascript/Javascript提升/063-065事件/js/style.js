// 当页面完全加载成功触发该事件
window.onload = function() {
	// 你瞅啥先执行   页面加载成功才执行下面这个
	alert("页面加载成功");
}
alert("你瞅啥?")


// 页面关闭时执行
window.onunload = function() {
	alert("确认关闭?")
} 
 
 
 
 window.onscroll = function() {
	 alert("scroll")
 }