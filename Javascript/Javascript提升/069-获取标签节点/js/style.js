//找到要操作的标签对象

var jsDiv = document.getElementById("idDiv");
console.log(jsDiv);
document.write("<br>");
console.log(typeof(jsDiv));

document.write("<br>");

//  HTMLCollection(4) [div.classDiv, div.classDiv, div.classDiv, div.classDiv]
var jsDivs = document.getElementsByClassName("classDiv"); 
console.log(jsDivs);
document.write("<br>");
console.log(typeof(jsDivs));

document.write("<br>");
var jsInpsArr = document.getElementsByName("inputText");
document.write("<br>"); 
console.log(jsInpsArr);
document.write("<br>");
console.log(typeof(jsInpsArr));


// 拿到所有div标签
document.write("<br>");
var jsAllDivs = document.getElementsByTagName("div")
document.write("<br>"); 
console.log(jsAllDivs);
document.write("<br>");
console.log(typeof(jsAllDivs));
