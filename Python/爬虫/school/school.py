#!/usr/bin/python3
import webbrowser,time

a='''
https://www.google.com/search?q=上海理工大学印刷出版专科学校 bbs -myubbs.com
https://www.google.com/search?q=上海科技职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海交通职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海行建职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海农林职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海城建职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海电子信息职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海济光职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海东海职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海工商职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海邦德职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海中桥职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海震旦职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海民远职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海思博职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海电影艺术职业学院 bbs -myubbs.com
https://www.google.com/search?q=上海工商外国语职业学院 bbs -myubbs.com

'''

for i in a.splitlines():
	webbrowser.open_new_tab(i);
	time.sleep(5);