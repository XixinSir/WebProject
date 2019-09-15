
// 添加拖动
var rectangles = document.querySelectorAll("#box>div");

for (var i = 0; i < rectangles.length; i++) {
	rectangles[i].onmousedown = function(e) {
		var evt = e || window.event;
		
		var disx = evt.clientX - this.offsetLeft;
		var disy = evt.clientY - this.offsetTop;
		var self = this;
		
		document.onmousemove = function(e) {
			var ev = e || window.event;
			
			var x = ev.clientX - disx;
			var y = ev.clienty - disy;
			
			self.style.left = x + "px";
			self.style.top = y + "px";
			
			// 检测是否发生碰撞
			pzjcFunc(rectangles[0], rectangles[1]);
			
			
		}
		// return false
	}
} 


document.onmouseup = function() {
	document.onmousemove = document.onmousedown = null;
}


// 检测是否发生碰撞的方法
function pzjcFunc(obj1, obj2) {
	var obj1Left = obj1.offsetLeft;
	var obj1Width = boj
}