document.body.onclick = function() {
	this.style.backgroundColor = "yellow";
}

document.getElementById("box").onclick = function(e) {
	var ev = e || window.event
	ev.stopPropagation()
	this.style.backgroundColor = "blue"
}


document.getElementById("put").onclick = function(e) {
	var ev = e || window.event
	ev.stopPropagation()
}

document.getElementById("link").onclick = function(e) {
	var ev = e || window.event
	ev.stopPropagation()
	var info = window.confirm("您浏览的页面存在风险,是否继续??")
	if (info == false) {
		// 阻止跳转的默认行为
		ev.preventDefault()
	}
}