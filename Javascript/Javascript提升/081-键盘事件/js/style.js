

// 按下
document.addEventListener("keydown", function(e) {
	//         非IE    IE浏览器
	var event = e || window.event;
	console.log(event)
	console.log(event.altKey, event.ctrlKey, event.shiftKey,event.key,event.keyCode)
}, false)


// 抬起
document.addEventListener("keyup", function(e) {
	//         非IE    IE浏览器
	var event = e || window.event;
	console.log(event)
	console.log(event.altKey, event.ctrlKey, event.shiftKey,event.key,event.keyCode)
}, false)



//  按非功能按键的时候触发 shift之类的
document.addEventListener("keypress", function(e) {
	//         非IE    IE浏览器
	var event = e || window.event;
	console.log(event)
	console.log(event.altKey, event.ctrlKey, event.shiftKey,event.key,event.keyCode)
}, false)
