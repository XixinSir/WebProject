var time 

time = window.setInterval(function(){
	console.log("sunck is a good man");
// 每2000ms执行以下函数
}, 2000)


// js中的定时器没有暂停的概念   没有恢复这一说法 

// 想继续执行 只能说再创建一个定时器
function func1() {
	// 清除定时器
	window.clearInterval(time); // time后面是定时器的编号
}

function func2() {
	time = window.setInterval(function(){
		console.log("sunck is a good man");
	}, 2000)
}