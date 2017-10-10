#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import infoInit
import datetime

userInfoList = infoInit.getAllUserInfoList()
behaviorInfoList = infoInit.getAllBehaviorInfoList()
productInfoList = infoInit.getProductInfoList()

d1 = datetime.datetime(1970, 1, 1, 0)
d2 = datetime.datetime(2017, 7, 26, 0)

dayBehaviorInfoList = [[] for i in range(31)]  #31天某一天所有用户的行为数据
day = range(31)
dayCnt = [0 for i in range(31)]  #31天某天行为数据的个数
productCnt = [0 for i in range(485144)]  #48w多商品数据的月销量
for behaviorInfo in behaviorInfoList:
    d3 = d1 + datetime.timedelta(seconds=int(behaviorInfo[2]))
    if ((d3 - d2).days in day):
        dayBehaviorInfoList[(d3 - d2).days].append(behaviorInfo)
        dayCnt[(d3 - d2).days] = dayCnt[(d3 - d2).days] + 1
    if (behaviorInfo[3] == '3'):
        productCnt[int(behaviorInfo[1])] = productCnt[int(behaviorInfo[1])] + 1

print dayCnt
print len(productInfoList)
cnt = 0  #选出的热门商品的总月销量数据  所有商品总月销量有10w多
for c in sorted(productCnt, reverse=True)[0:200]:  #选出月销量前多少的热门商品
    cnt = cnt + c
print cnt, c