var d = new Date();


// 2019/8/8 下午10:53:53
var str = d.toLocaleString();
document.write(str);
document.write("<br>");


// 2019/8/8
var str1 = d.toLocaleDateString();
document.write(str1);
document.write("<br>");


// 下午10:53:53
var str2 = d.toLocaleTimeString();
document.write(str2);

