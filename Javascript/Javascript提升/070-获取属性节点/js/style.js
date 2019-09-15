


//  获取属性节点


// 官方定义的属性可以这样直接获取
var jsInput = document.getElementById("in");
console.log(jsInput.placeholder);

//获取自定义的属性
console.log(jsInput.getAttribute("my"))


function func(){
	
	// 修改属性的值
	jsInput.placeholder= "你被我改了"
	
	jsInput.setAttribute("my", "你的")
	
	console.log(jsInput)
	

}


function func1() {
	// 官方和自定义的都可以这样写
	jsInput.removeAttribute("my", "你的")
	console.log(jsInput)
}


function funcadd() {
	//  增加 属性值
	jsInput.setAttribute("abcd", "abcd")
	console.log(jsInput)
}