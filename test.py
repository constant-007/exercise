#coding=utf-8

import linecache
import time

now = time.time()

data_keys = ('bid','uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')

keys = {data_keys[k] : k for k in range(0, len(data_keys))}

f = linecache('t.txt')

lines = [x[1:-1].split('","') for x in f]

#输出用户总数

users = set([line[keys['username']]] for line in lines)

user_total = len(users)

assert type(user_total) == int

# 每一个用户的名字

users = list(users)

assert type(users) == list

#3
lines_total_from_2012_11 = len(list(filter(lambda line: line[keys['created_at']].startswith('2012-11'),lines)))

assert type(lines_total_from_2012_11) == int

#4
users_by_date = [line[keys['created_at']].split('')[0] for line in lines]

lines_by_created = list(set(users_by_date))

lines_by_created.sort()

assert type(lines_by_created) == list

#5 哪个小时发布的数据最多
'''
第一步，以小时为key整理数据
第二步，count统计
第三步，排序
第四步，取最大
'''
hours = [int(line[keys['created_at']][11:13]) for line in lines]

total_by_hour = 
