#coding=utf-8

"""
题目

对应字段如下（每一个逗号分隔的，“”内的，则是字段的详细信息。空白则代表没有。）：

bid    消息ID 
uid     用户ID 
username 用户名  
ugrade 用户等级字段 
content(text) 微博内容
img(message包含图片链接) 
created_at 微博发布时间 
source(来源)
rt_num, 转发数 
cm_num, 评论数 
rt_uid, 转发UID
rt_username, 转发用户名
rt_v_class, 转发者等级 
rt_content, 转发内容 
rt_img, 转发内容所涉及图片 
src_rt_num, 源微博回复数 
src_cm_num, 源微博评论数 
gender,(用户性别) 
rt_mid（转发mid） 
geo 地区
lat() 经度
lon 纬度
place 地点
hashtags 
ats  @谁 
rt_hashtags, 回复标签
rt_ats, 回复@谁
v_url, 源微博URL 
rt_v_url 转发URL 


twitter文本附件的排序格式如下

fields=bid,uid,username,v_class,content,img,time,source,rt_num,cm_num,rt_uid,rt_username,rt_v_class,rt_content,rt_img,src_rt_num,src_cm_num,gender,rt_mid,location,rt_mid,mid,lat,lon,lbs_type,lbs_title,poiid,links,hashtags,ats,rt_links,rt_hashtags,rt_ats,v_url,rt_v_url

要求如下：

1.该文本里，有多少个用户。（要求：输出为一个整数。）

2.该文本里，每一个用户的名字。 （要求：输出为一个list。）

3.该文本里，有多少个2012年11月发布的tweets。 （要求：输出为一个整数。提示：请阅读python的time模块）

4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）

5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）

6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）

7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets） 

8. 统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]）

9. 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个。(要求，输出一个整数。)

10. UID为573638104的用户 发了多少个微博 （要求：输出一个整数）

11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。

12. 该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）

13. 该文本里，谁转发的URL最多 （要求：输出用户的uid，字符串格式。）

14. 该文本里，11点钟，谁发的微博次数最多。 （要求：输出用户的uid，字符串格式。）

15. 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）
"""

import linecache
import time

now = time.time() # 代码开始时间

#数据整理

data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')


keys = {data_keys[k]: k for k in range(0, len(data_keys))}

# input:{'bid': 0, 'uid': 1, 'username': 2, 'v_class': 3, 'content': 4, 'img': 5, 'created_at': 6, 'source': 7, 'rt_num': 8, 'cm_num': 9, 'rt_uid': 10, 'rt_username': 11, 'rt_v_class': 12, 'rt_content': 13, 'rt_img': 14, 'src_rt_num': 15, 'src_cm_num': 16, 'gender': 17, 'rt_bid': 18, 'location': 19, 'rt_mid': 20, 'mid': 21, 'lat': 22, 'lon': 23, 'lbs_type': 24, 'lbs_title': 25, 'poiid': 26, 'links': 27, 'hashtags': 28, 'ats': 29, 'rt_links': 30, 'rt_hashtags': 31, 'rt_ats': 32, 'v_url': 33, 'rt_v_url': 34}

f = linecache.getlines('t.txt')

lines = [x[1:-1].split('","') for x in f] #拆分

#1 输出用户总数。 

users = set([line[keys['username']] for line in lines])

user_total = len(set(users))

assert type(user_total) == int

"""
assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况.

assert expression 
等价于
if not expression:
    raise AssertionError

assert expression [, arguments]
等价于
if not expression:
    raise AssertionError(arguments)
"""

#2 每一个用户的名字 list
users = list(users)
assert type(users) == list

#3 有多少个2012年11月发布的tweets
lines_from_2012_11 = filter(lambda line: line[keys['created_at']].startswith('2012-11'), lines)

lines_total_from_2012_11 = len(list(lines_from_2012_11))

assert type(lines_total_from_2012_11) == int

"""
filter() 
函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。

该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

filter(function, iterable)
function -- 判断函数。 
iterable -- 可迭代对象。 
返回值 -- 返回列表
"""

"""
lambda 
创建匿名函数。
lambda只是一个表达式，函数体比def简单很多。 
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。 
lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
语法
    lambda函数的语法只包含一个语句，如下：
    lambda [arg1 [,arg2,.....argn]]:expression
"""

"""
startswith()
Python startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。
语法
    startswith()方法语法：
    str.startswith(str, beg=0,end=len(string));
参数
    str -- 检测的字符串。
    strbeg -- 可选参数用于设置字符串检测的起始位置。
    strend -- 可选参数用于设置字符串检测的结束位置。
返回值
    如果检测到字符串则返回True，否则返回False。
"""

#4  该文本里，有哪几天的数据？ 

users_by_date = [line[keys['created_at']].split(' ')[0] for line in lines]

lines_by_created = list(set(users_by_date)) # 去重

lines_by_created.sort()

assert type(lines_by_created) == list

"""
split()
语法
    str.split(str="", num=string.count(str))
参数
    str – 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    num – 分割次数。默认为 -1, 即分隔所有。
返回值
    Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
    返回分割后的字符串列表。
例题
    输入
        str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
        print str.split( );          # 以空格为分隔符，包含 \n
        print str.split(' ', 1 );    # 以空格为分隔符，分隔成两个
    输出
        ['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
        ['Line1-abcdef', '\nLine2-abc \nLine4-abcd']

split()[0]
输入输出
    >>> str="hello boy<[www.doiido.com]>byebye"
    >>> str.split("[")[1].split("]")[0]
    'www.doiido.com'
    >>> str.split("[")[1].split("]")[0].split(".")
    ['www', 'doiido', 'com']
    >>> str.split("o")[0]
    'hell'
    >>> str.split("o")[1]
    ' b'(这里有空格)
    >>> str.split("o")[3]
    'iid'(这里得到的iid是第3个o后和第4个o前之间的内容)
    >>> str.split("[")[0]
    'hello boy<'
解析
    str.split("[")[1]. split("]")[0]输出的是 [ 后的内容以及 ] 前的内容。
    str.split("[")[1]. split("]")[0]. split(".") 是先输出 [ 后的内容以及 ] 前的内容，然后通过 . 作为分隔符对字符串进行切片。
    str.split(“o”)[0]得到的是第一个o之前的内容
    str.split(“o”)[1]得到的是第一个o和第二个o之间的内容
    str.split(“o”)[3]得到的是第三个o后和第四个o前之间的内容
    str.split("[")[0]得到的是第一个 [ 之前的内容
注意：[ ]内的数值必须小于等于split("")内分隔符的个数，否则会报错.
"""

#5 该文本里，在哪个小时发布的数据最多？ 
# todo 这里用time模块做时间转换最好。下例只为讲解拆分方法

hours = [int(line[keys['created_at']][11:13]) for line in lines]

total_by_hour = [(h,hours.count(h)) for h in range(0,24)]

total_by_hour.sort(key=lambda k:k[1],reverse=True)

max_hour = total_by_hour[0][0]

assert type(max_hour) == int


#6 该文本里，输出在每一天发表tweets最多的用户

dateline_by_user = {k:dict() for k in lines_by_created}

for line in lines:
    dateline = line[keys['created_at']].split(' ')[0]
    username = line[keys['username']]
    if username in dateline_by_user[dateline]:
        dateline_by_user[dateline][username] += 1
    else:
        dateline_by_user[dateline][username] = 1

for k,v in dateline_by_user.items():
    us = list(v.items())
    us.sort(key=lambda k:k[1],reverse=True)
    dateline_by_user[k] = {us[0][0]:us[0][1]}

assert type(dateline_by_user) == dict

"""
items()
语法
    dict.items()
参数
    NA
返回值
    返回可遍历的(键, 值) 元组数组。
输入
    #!/usr/bin/python3
    
    dict = {'Name': 'Runoob', 'Age': 7}
    
    print ("Value : %s" %  dict.items())
输出
    Value : dict_items([('Age', 7), ('Name', 'Runoob')])
"""

#7 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率

lines_from_2012_11_03 = filter(lambda line:line[keys['created_at']].startswith('2012-11-03'),lines)

hourlines_from_2012_11_03 = {str(i):0 for i in range(0,24)}

for line in lines_from_2012_11_03:
    hour = line[keys['created_at']][11:13]
    hourlines_from_2012_11_03[str(int(hour))] += 1 

hour_timeline_from_2012_11_03 = [(k,v) for k,v in hourlines_from_2012_11_03.items()]
hour_timeline_from_2012_11_03.sort(key=lambda k:int(k[0]))

assert type(hour_timeline_from_2012_11_03) == list


#8 统计该文本里，来源的相关信息和次数

source = set([k[keys['source']] for k in lines])
source_dict = {s:0 for s in source}
for line in lines:
    source_name = line[keys['source']]
    source_dict[source_name] += 1
source_list = [(k,v) for k,v in source_dict.items()]
source_list.sort(key=lambda k:k[1],reverse=True)
assert type(source_list) == list


#9 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个

umi_total = 0
for line in lines:
    if line[keys['rt_v_url']].startswith('https://twitter.com/umiushi_no_uta'):
        umi_total += 1
assert type(umi_total) == int


#10 UID为573638104的用户 发了多少个微博

tweets_total_from_573638104 = 0
for line in lines:
    if line[keys['uid']] == '573638104' :
        tweets_total_from_573638104 += 1
assert type(tweets_total_from_573638104) == int


#11 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。

def get_user_by_max_tweets(*uids):
    
    '''
    @deprecated:参数可为字符串或者数字
    '''
    if len(uids) > 0:
        uids = filter(lambda u:type(u) == int or u.isdigit(),uids)
        uids = list(map(str,uids))
        if len(uids) > 0:
            uids_dict = {x:0 for x in uids}
            for line in lines:
                uid = line[keys['uid']]
                if uid in uids:
                    uids_dict[uid] += 1
            uids_and_tweets_total = [(x,y) for x,y in uids_dict.items()]
            uids_and_tweets_total.sort(key=lambda k:k[1],reverse=True)
            return uids_and_tweets_total[0][0]
    return "null"


assert get_user_by_max_tweets() == 'null'
assert get_user_by_max_tweets('ab','cds') == 'null'
assert get_user_by_max_tweets('ab','cds','123b') == 'null'
assert get_user_by_max_tweets('12342','cd') == '12342'
assert get_user_by_max_tweets('28803555',28803555) == '28803555'
assert get_user_by_max_tweets('28803555',28803555,'96165754') == '28803555'

"""
str.isdigit()
返回值
    如果字符串只包含数字则返回 True 否则返回 False。
"""

"""
map()
会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
语法：
    map(function, iterable, ...)
参数
    function -- 函数
    iterable -- 一个或多个序列
返回值
    python3返回迭代器
"""


#12 该文本里，谁发的微博内容长度最长 

lines_by_content_length = [(line[keys['username']],len(line[keys['content']])) for line in lines]
lines_by_content_length.sort(key=lambda k:k[1],reverse=True)
user_by_max_content = lines_by_content_length[0][0]
# todo 如果有多个最多怎么办？
assert type(user_by_max_content) == str


#13 该文本里，谁转发的URL最多 

lines_by_rt = [(line[keys['uid']],int(line[keys['rt_num']])) for line in lines if line[keys['rt_num']] != '']
lines_by_rt.sort(key=lambda k:k[1],reverse=True)
user_by_max_rt = lines_by_rt[0][0]
assert type(user_by_max_rt) == str


#14 该文本里，11点钟，谁发的微博次数最多。

lines_on_hour11 = filter(lambda line:line[keys['created_at']].startswith('11',11,13),lines)
lines_by_uid_on_hour11 = {k[keys['uid']]:0 for k in lines_on_hour11}
for line in lines_on_hour11:
    uid = line[keys['uid']]
    lines_by_uid_on_hour11[uid] += 1
d = [(k,v) for k,v in lines_by_uid_on_hour11.items()]
d.sort(key=lambda k:k[1],reverse=True)
uid_by_max_tweets_on_hour11 = d[0][0]
# todo 如果有多个最多怎么办？
assert type(uid_by_max_tweets_on_hour11) == str


#15 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）

uid_by_v_url = {k[keys['uid']]:0 for k in lines}
for line in lines:
    uid = line[keys['uid']]
    if lines[keys['v_url']] != '':
        uid_by_v_url[uid] += 1
uid_sort_by_v_url = [(k,v) for k,v in uid_by_v_url.items()]
uid_sort_by_v_url.sort(key=lambda k:k[1],reverse=True)
uid_by_max_v_url = uid_sort_by_v_url[0][0]
# todo 如果有多个最多怎么办？
assert type(uid_by_max_v_url) == str

print('运算时间：%s' % (time.time() - now)) #整体运行时间
