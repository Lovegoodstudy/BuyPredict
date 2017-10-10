#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def getAllUserInfoList():
    f = open("data/user_info.txt", "r")
    data = f.readlines()  #txt中所有字符串读入data
    userInfoList = []

    for line in data:
        line = line[:len(line) - 1]
        userInfo = line.split("\t")        #将单个数据分隔开存好
        userInfoList.append(userInfo)

    return userInfoList

def getAllBehaviorInfoList():
    f = open("data/behavior_info.txt", "r")
    data = f.readlines()  #txt中所有字符串读入data
    behaviorInfoList = []

    for line in data:
        line = line[:len(line) - 1]
        behaviorInfo = line.split("\t")        #将单个数据分隔开存好
        behaviorInfoList.append(behaviorInfo)

    return behaviorInfoList

def getProductInfoList():
    f = open("data/product_info.txt", "r")
    data = f.readlines()  #txt中所有字符串读入data
    productInfoList = []

    for line in data:
        line = line[:len(line) - 1]
        productInfo = line.split("\t")        #将单个数据分隔开存好
        productInfoList.append(productInfo)

    return productInfoList