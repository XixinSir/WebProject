
var jsDiv = document.getElementById("box")


// backgroundColor--------background-color
function changeColor() {
	jsDiv.style.backgroundColor = "yellow";
	jsDiv.style.width = "200px";
	// jsDiv.style.["width"] = "200px";
	jsDiv.style.height = "100px";
	jsDiv.style.left = "100px";
	
	
	
	var color = window.getComputedStyle(jsDiv, null)["backgroundColor"] ;
	console.log(color);
}