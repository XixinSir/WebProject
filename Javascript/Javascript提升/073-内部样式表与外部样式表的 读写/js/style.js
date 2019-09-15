var jsDiv = document.getElementById("box");
	

function changeColor() {
	console.log(1)
	// 72和73中 设置css的属性的方法都是一样的 
	
	// 获取值 内部和 外部的css  方法不一样
	/*
	jsDiv.style.backgroundColor只能获取行间的样式  不能获取外部css中的
	外部的要用 window.getComputedStyle(jsDiv, null)["backgroundColor"]; 获取
	因为style属性外部没有
	
	
	window.getComputedStyle(jsDiv, null)["backgroundColor"] 这个属性所有的通用
	获取也可以都用这个
	*/
	
	var color = window.getComputedStyle(jsDiv, null)["backgroundColor"];
	console.log(color);
}