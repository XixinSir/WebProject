/*
思考:   把最后一行的b换为a为什么不行?
*/


var div = document.getElementById("box");



var a = document.createElement("p");
a.innerHTML = "sunck is a good man";
a.style.backgroundColor = "red"
console.log(a);


// var i = document.createElement("input");
// i.text = "text";
// console.log(i);
// 


// 添加到某一个节点前面 
// 注意: 按照正常写法  最后一个是空节点(文本节点)  要把div和
div.insertBefore(a, div.lastChild);


var b = document.createElement("p");
b.innerHTML = "sunck is a good man";
b.style.backgroundColor = "blue"
console.log(b);
// 
// 
// // 把创建的标签放到页面上
// // 添加到最后面
// div.appendChild(b);



// 替换节点 
div.replaceChild(b, div.lastChild)


//克隆  只能复制父级节点 子节点复制不了  加上true全部复制
var newDiv = div.cloneNode(true);
document.write(newDiv);



// 删除最后一个
div.removeChild(div.lastChild);
