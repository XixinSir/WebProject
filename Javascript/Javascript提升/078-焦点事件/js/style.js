
var inp = document.getElementById("in");


// 聚焦
inp.addEventListener("focus", function() {
	console.log("聚焦事件");
}, false)


// 离焦
inp.addEventListener("blur", function() {
	console.log("离焦事件");
}, false)

