



function fly() {
	var jsDiv = document.getElementById("box")
	console.log(jsDiv)
	
	// var a = ;
	// console.log(a);  // 0px
	// console.log(typeof(a));  // string 
	
	setInterval(function(){
	   
	   var left =  parseInt(window.getComputedStyle(jsDiv, null).left);
	   jsDiv.style.left  = left + 10 + "px";
	   
	   var top =  parseInt(window.getComputedStyle(jsDiv, null).top);
	   jsDiv.style.top  = left + 10 + "px";
	}, 10)
}