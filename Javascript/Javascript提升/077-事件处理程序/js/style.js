/* 
在div3和div4的时间函数中 
this 代表的是当前的标签 
在普通函数func()中,this代表的是window
*/



function func(self) {
	console.log(self);
	console.log(this)
	self.style.backgroundColor = "black";
	// alert("点的好爽")
}


var div3 = document.getElementById("box3");
div3.onclick = function() {
	console.log(this)
	// alert("hehe")
}

// 事件清除
// div3.onclick = null 

// 事件相互之间不影响  如果写两个都执行   用onclick就会覆盖
var div4 = document.getElementById("box4");
function listen() {
	console.log(this)
	// alert("监听")
}
div4.addEventListener("click", listen, false)

// div4.removeEventListener("click", listen, false)

