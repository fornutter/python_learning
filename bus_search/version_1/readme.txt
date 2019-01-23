
文件夹及文件内容介绍

文件 bus_search_v1.py   为功能的py代码实现，
文件 bus_search_1_GUI  对上边的文件进行了重构，生成了一个标准类
文件：bus_search_v1_GUI  调用了上一个类，并实现了GUI 编程
文件夹 dist 下的 为打包后的应用程序，从用了 pyinstaller  打包， 去除了chromedriver 打包过程中的弹出cmd 很窗口问题，相应的解决方式在proble.txt 文件内
文件夹 build 和 dist  是在打包过程中生成的文件夹， 
pyinstaller 的打包格式为 pyinstaller  -F -w -i bus.ico bus_search_v1_GUI.py



程序功能实现


采用了 python+ selenium + chromedriver  的方式 构建爬虫，爬取了lijn 公交车站点信息，点击home 显示的是如果想回家，在学校车站的公交到站时间，work 同样原理