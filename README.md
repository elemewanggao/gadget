[toc]
# gadget
## 解决csv文件用excel打开出现乱码问题小工具
### 背景说明
在简体中文环境下，excel打开csv文件时默认是用ANSI编码打开的，如果文件本身的编码为utf-8或unicode编码，会导致乱码问题出现
### 解决思路
在excel头部加上\xef\xbb\xbf这个标志，这个是UTF-8的BOM，相当于文件头，表明这个文件的编码格式为UTF-8，EXCEL打开时知道文件编码为UTF-8后，就会以正确的编码格式打开这个文件，不会出现乱码问题
### 工具说明
运行命令: python open_csv_for_excel.py /Users/wanggao/Desktop/1.csv
说明: 参数必填,为csv文件路径或目录路径，可以一个或多个参数，生成一个新的csv文件/Users/wanggao/Desktop/1_new.csv,可以用Excel打开




















