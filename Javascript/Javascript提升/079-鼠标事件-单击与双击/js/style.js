var inp = document.getElementById("in");
var time 

// 如果单击和双击同时存在  需要用定时器


// 单击
inp.addEventListener("click", function() {
	clearTimeout(time)
	time = setTimeout(function() {
		console.log("单击");
	}, 1000)
}, false)

// 双击

/*
如果是双击  第一次单击也会执行一遍 延时300ms再执行单击 
如果再点一次 就确定是双击了 就把定时器清掉  上面就不会执行  执行的就是双击
*/
inp.addEventListener("dblclick", function() {
	clearTimeout(time)
	console.log("双击");
}, false)

