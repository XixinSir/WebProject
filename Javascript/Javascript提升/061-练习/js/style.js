function func() {
	// 跳转到红页面
	// window.location.href = "red.html";
	
	// true:直接从缓存里拿结果
	// window.location.reload(true);
	
	// 在浏览器留下痕迹(可前进后退)
	window.location.assign("red.html")
	
	// 不留痕迹
	// window.location.replace("red.html")
}



function yellowfunc() {
	window.location.assign("yellow.html")
}


function forwardPagefunc() {
	window.history.back()
} 


function nextPagefunc() {
	window.history.forward() 
} 



function newWindowfunc() {
	window.open("red.html", "blank",
	"width=400px,height=400px, left=20px,top=0");
}


function closefunc() {
	window.close()
	
}