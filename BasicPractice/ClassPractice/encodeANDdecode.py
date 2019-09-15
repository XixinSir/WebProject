"""
https://github.com/taizilongxu/interview_python
decode和encode则能解决大部分python中出现的乱码问题，python使用的是Unicode编码


decode 的作用是将其他编码的字符串转换成 Unicode 编码，
eg:   name.decode("GB2312"),表示将GB2312编码的字符串name转换成Unicode编码
表示这个对象按照对象解码，在python环境下显示输出就正常了。


encode 的作用是将Unicode编码转换成其他编码的字符串，
eg:  name.encode(”GB2312“)，表示将Unicode编码的字符串name转换成GB2312编码
name对象就像被加密了，这时候显示输出就是乱码。
"""

str1 = "Hello The World!"
str2 = "我是吴彦祖, I am Wu Sir!"
str3 = "我是吴彦祖,我好帅!"

str4 = str2.encode("utf-8")
str5 = str2.encode("GBK")
str6 = str2.encode("GB2312")
str7 = str2.encode("utf-16")
str8 = str2.encode("utf-32")

print("--------------------编码---------------------")
print(str4)
print(str5)
print(str6)
print(str7)
print(str8)


print("--------------------解码---------------------")
print(str4.decode("utf-8"))
print(str5.decode("GBK"))
print(str6.decode("GB2312"))
print(str7.decode("utf-16"))
print(str8.decode("utf-32"))


# 将GB2312编码的字符串转换为UTF-8格式的
