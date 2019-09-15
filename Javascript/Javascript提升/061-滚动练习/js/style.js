
// 不需要调用 滚动救会触发
window.onscroll = function(){
	
	// 高度(滚动条)
	var a = document.documentElement.scrollTop || document.body.scrollTop
	console.log(a);
	console.log("发生了滚动");
	if (a == 500) {
		console.log("加载新的数据");
	}
	
} 

