import re

line = "<H1>Chapter 1 - 介绍正则表达式</H1>"
par1 = '<.*>'  # 贪婪：匹配从开始小于符号 (<) 到关闭 H1 标记的大于符号 (>) 之间的所有内容。
par2 = '<.*?>'  # 非贪婪：如果您只需要匹配开始和结束 H1 标签，下面的非贪婪表达式只匹配 <H1>。
par3 = '<\w+?>'  # 只想匹配开始的 H1 标签，表达式则是：
par4 = '^<H1>Chapter [1-9][0-9]{0,1}'  # 匹配一个章节标题，该标题只包含两个尾随数字，并且出现在行首：
par5 = '.*?</H1>$'  #
par6 = '\Bapt' #原意为匹配Chapter中的apt，但是不行
str = "http://www.runoob.com:80/html/html-tutorial.html" \
      "sdifajofasofjoasidof"
patt1 = '(\w+):\/\/([^/:]+)(:\d*)?([^# ]*)'
patt1='(\w+):\/\/([^//:]+)(:[0-9]*)(.*)'
test='^http.*html$'
str2='adsfdasafsfasf' \
     'a9'
str3='b4'
test1='^[a-z][0-9]$'
#matchObj = re.match(par6, line, re.I)
matchObj =re.match(test1,str3, re.I)


if matchObj:
    print(matchObj.group())
    # for i in range(matchObj.lastindex+1):
    #     print(matchObj.group(i))
else:
    print("No match!!")
