var jsDiv = document.getElementById("box");

// 区别看图片 

console.log(jsDiv.innerHTML);
console.log(jsDiv.outerHTML);
console.log(jsDiv.innerText);


jsDiv.innerHTML = "<h1>good</h1>"; 
console.log(jsDiv);
