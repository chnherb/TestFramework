# encoding=utf-8
import copy
import os
import datetime

start = datetime.datetime.now()

#存储图的字典
graph = dict()
#存储简单路径列表的列表
simplePath = []
#存储基本路径列表的列表
primePath =[]

#初始化存储图的字典
def Init(fileName):
    path = os.path.dirname(__file__)
    filePath = path + "/" + fileName
    print filePath
    with open(filePath, 'r') as fr:
        i = 0
        for line in fr:
            if line[-1] == '\n':
                line = line[:-1]
            if line.strip() != "": 
                line = line.strip().replace(' ','')
                if line != '-1':
                    data = map(int, line.split(','))
                    graph[i] = data
                else:
                    graph[i] = []
                i += 1
    print graph
    return
#判断节点x是否为路径列表的第一个节点
#path：列表  x：节点
def IsHead(path, x):
    if len(path) == 0:
        return False
    if path[0] == x:
        return True
    return False

#判断节点x是否与路径列表中除第一个节点外是否重复
#path：列表  x：节点
def Repetitive(path, x):
    p = copy.deepcopy(path)
    if len(p) > 0:
        p.pop(0)
    while len(p) > 0:
        if p[0] == x:
            return True
        p.pop(0)
    return False
#深度遍历找出所有的简单路径
#path：当前路径的列表 x：当前已经遍历过的最新节点
def DFS(path, key):
    value = graph[key]
    for t in value:
        while Repetitive(path,t) == False:
            path.append(t)
            simplePath.append(copy.deepcopy(path))
            # print path
            if IsHead(path,t) == False:
                DFS(copy.deepcopy(path),t)
        while path[-1] != key:
            path.pop()
    path.pop()
    return

#获取所有的简单路径列表，并加入到列表simplePath变量中
def GetSimplePath():
    # print 'hahah'
    for key in graph.keys():     
        path = []
        path.append(key)
        simplePath.append(copy.deepcopy(path))
        # print path
        DFS(copy.deepcopy(path),key)
        path.pop()       
    return

#使用简单的模式匹配算法判断路径列表path1是否是路径列表path2的子路径
def IsSub(path1, path2):
    len1 = len(path1)
    len2 = len(path2)
    if len1 > len2:
        return False
    i=0
    j=0
    while (i<len1 and j<len2):
        if path1[i] == path2[j]:
            i+=1
            j+=1
        else:
            j = j - i + 1
            i = 0
    if i >= len1:
        return True
    return False

def getNext(pattern):
    next = []
    j = 0
    plen = len(pattern)
    next.append(0)
    for i in range(1, plen):
        while ((j > 0) and (pattern[j] != pattern[i])):
            j = next[j-1]
        if (pattern[i] == pattern[j]):
            j = j + 1
        next.append(j)
    return next
 
def kmpSearch(text, pattern, next):
    j = 0
    plen = len(pattern)
    tlen = len(text)
 
    for i in range(0, tlen):
        while j > 0 and text[i] != pattern[j]:
            j = next[j-1]
 
        if text[i] == pattern[j] :
            j = j + 1
 
        if j == plen :
            # print "from ", i-j+1, "to ", i
            # j = next[j-1]
            return True
    return False

#获取所有的基本路径列表，并加入到列表primePath变量中
def GetPrimePath():
    global primePath
    primePath = copy.deepcopy(simplePath)
    i = 0
    while(i != len(primePath)):
        for j in range(0, len(primePath)):
            flag = False
            if i == j:
                pass
            else:
                # if IsSub(primePath[i], primePath[j]) == True:
                if kmpSearch(primePath[j], primePath[i], getNext(primePath[i])) == True:
                    del(primePath[i])
                    flag = True
                    break
        if flag == False:
            i += 1
     
#将结果输出到文件
def Output(fileName):
    path = os.path.dirname(__file__)
    filePath = path + "/" + fileName
    print filePath
    with open(filePath, 'w') as fr:
        fr.write("graph = {\n")
        for g in graph.items():
            fr.write('\t' + str(g)[1:-1] + '\n')
        fr.write("}\n")
        fr.write("primePath-size:%d"%(len(primePath)) + '\n')
        i = 0
        for path in primePath:
            i += 1
            fr.write("path" + str(i) + ': ' + str(path) + '\n')
    return   

Init('case15.txt')#中文文件名会出错，
#原因：获取当前路径类型是str，中文文件名保存需转成Unicode格式，str和Unicode不能直接拼接，转化成同一类型又乱码，暂时不解决
GetSimplePath()
print simplePath
print("simplePath-size:%d"%(len(simplePath)))
GetPrimePath()
print primePath
print("primePath-size:%d"%(len(primePath)))
Output('output15_2.txt')
end = datetime.datetime.now()
print("run time:%s"%(end - start))




