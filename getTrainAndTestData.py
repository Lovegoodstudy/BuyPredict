import infoInit
import random

def getTrainAndTestUserInfoList():
    userInfoList = infoInit.getAllUserInfoList()
    testUserInfoList = random.sample(userInfoList, 5000)

    trainUserInfoList = []
    for userInfo in userInfoList:
        if (userInfo not in testUserInfoList):
            trainUserInfoList.append(userInfo)

    print len(userInfoList)
    print len(testUserInfoList)
    print len(trainUserInfoList)

    return trainUserInfoList,testUserInfoList

def getTrainAndTestBehaviorInfoList(trainUserInfoList, testUserInfoList):
    trainUserIdList = []
    testUserIdList = []
    for userInfo in trainUserInfoList:
        trainUserIdList.append(userInfo[0])
    for userInfo in testUserInfoList:
        testUserIdList.append(userInfo[0])

    behaviorInfoList = infoInit.getAllBehaviorInfoList()
    trainBehaviorInfoList = []
    testBehaviorInfoList = []
    for behaviorInfo in behaviorInfoList:
        if (behaviorInfo[0] in trainUserIdList):
            trainBehaviorInfoList.append(behaviorInfo)
        if (behaviorInfo[0] in testUserIdList):
            testBehaviorInfoList.append(behaviorInfo)

    return trainBehaviorInfoList, testBehaviorInfoList

trainUserInfoList, testUserInfoList = getTrainAndTestUserInfoList()

f = open("data/train_user_info.txt", "w")
for userInfo in trainUserInfoList:
    line = "\t".join(userInfo) + '\n'
    f.write(line)
f.close()

f = open("data/test_user_info.txt", "w")
for userInfo in testUserInfoList:
    line = "\t".join(userInfo) + '\n'
    f.write(line)
f.close()

trainBehaviorInfoList, testBehaviorInfoList = getTrainAndTestBehaviorInfoList(trainUserInfoList, testUserInfoList)

f = open("data/train_behavior_info.txt", "w")
for behaviorInfo in trainBehaviorInfoList:
    line = "\t".join(behaviorInfo) + '\n'
    f.write(line)
f.close()

f = open("data/test_behavior_info.txt", "w")
for behaviorInfo in testBehaviorInfoList:
    line = "\t".join(behaviorInfo) + '\n'
    f.write(line)
f.close()
