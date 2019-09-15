var jsDiv = document.getElementById("box") 

basex = 0;
basey = 0;
movex = 0;
movey = 0;

jsDiv.addEventListener("mousedown", function(e) {
	var ev = e || window.event 
	
	basex = ev.pageX;
	basey = ev.pageY;

	document.onmousemove =  function(e) {
		var ee = e || window.event
		
		movex = ee.pageX - basex;
		basex = ee.pageX;
		
		movey = ee.pageY - basey;
		basey = ee.pageY
		
		jsDiv.style.left = jsDiv.offsetLeft + movex + "px";
		jsDiv.style.top = jsDiv.offsetTop + movey + "px";
	}
}, false)


document.addEventListener("mouseup", function(){
	document.onmousemove = null
}, false)