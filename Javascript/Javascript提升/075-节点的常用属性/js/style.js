

var jsDiv1 = document.getElementById("box1");
var jsDiv2 = document.getElementById("box2");
var jsDiv3 = document.getElementById("box3");
var jsInput = document.getElementById("input")
var s = jsInput.placeholder 

console.log(s);  // sunck is a good man


console.log(jsDiv1.nodeName, jsDiv1.nodeType, jsDiv1.nodeValue);  //   DIV    1  null
console.log(jsInput.nodeName, jsInput.nodeType, jsInput.nodeValue);  //   INPUT   1  null
console.log(s.nodeName, s.nodeType, s.nodeValue);  //  undefined undefined undefined 


// 所有的子节点(用这种方法获取  空格会作为文本节点)
// 文本节点的nodeType为3 
var allChilds = jsDiv1.childNodes
console.log(allChilds)

// 获取第一个子节点
var firstChild = jsDiv1.firstChild
console.log(firstChild)

// 获取父节点
console.log(firstChild.parentNode)


// 当前节点的前一个同级节点
console.log(jsDiv3.previousSibling)



// 当前节点的所有属性节点
console.log(jsInput.attributes)
console.log(jsInput.attributes[1])