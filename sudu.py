# coding=utf-8
#/usr/bin/python
import os
suduArray_ok = [
    [5, 0, 0, 0, 3, 9, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 0, 6, 5, 0, 8, 2, 0, 0],
    [6, 0, 0, 8, 0, 0, 3, 0, 0],
    [0, 9, 5, 0, 1, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 3, 5, 0, 6],
    [0, 0, 8, 7, 0, 6, 0, 0, 0],
    [0, 2, 9, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 9, 8, 0, 0, 0, 7]
];


suduArray = [
    [5, 1, 0, 2, 3, 9, 4, 6, 0],
    [0, 0, 1, 0, 0, 0, 0, 9, 0],
    [0, 0, 6, 5, 0, 8, 2, 0, 0],
    [6, 0, 0, 8, 0, 0, 3, 0, 0],
    [0, 9, 5, 0, 1, 0, 0, 2, 0],
    [0, 0, 2, 0, 0, 3, 5, 0, 6],
    [0, 0, 8, 7, 0, 6, 0, 0, 0],
    [0, 2, 9, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 9, 8, 0, 0, 0, 7]
];

'''
确定某一行是否全为1
'''
def CalColIsFine(array,colnum):
    for i in range(1,10):
        pass
        if i in array[colnum]:
            continue;
        else:
            print "error"
            return False;
    return True;

'''
确定某一列是否全为1
'''
def CalRowIsFine(array,Rownum):
    v = [x[Rownum] for x in array];
    #print v
    for i in range(1,10):
        #print i
        pass
        if i in v:
            continue;
        else:
            print "error"
            return False;
    return True;

'''
从上到下 , 找到为0的位置，并且返回其坐标
'''
def GetZeroIndex(array):
    ZeroIndex = [];
    for index in range(0,9):
        for i in array[index]:
            if i == 0:
                ZeroIndex.append([index,array[index].index(i)]);
                suduArray[index][array[index].index(i)]= 'A';
    #print ZeroIndex
    return ZeroIndex


'''
处理完一个0的情况后,接着处理两个0的情况
'''	

	
'''
给定坐标,然后求出该index所在的位置的行和列元素的交集
如果只缺一个数, 就能确定该位置的确切值
#index[0] 代表行坐标 
#index[1] 代表列坐标 
'''
def JudgeNumberByIndex(array,index):
    v = [x[index[1]] for x in array];
    union =  set(array[index[0]]).union(set(v));
    MissNumber = set();
    for num in range(1,10):
        if num not in union:
            MissNumber.add(num);
    return MissNumber


'''
从上至下, 递归确定0所在位置的值，首先确定只缺一个数的值
'''
def ConfirmResultOnlyMissOneNumber(array):
    pass
    ZeroCoordinate = GetZeroIndex(array);
    #print ZeroCoordinate
    for Coordinate in ZeroCoordinate:
        temp = JudgeNumberByIndex(array,Coordinate);
        if len(temp) == 0:
            return;
        if len(temp) == 1:
            pass
            #print temp
            #print JudgeNumberByIndex(array,Coordinate)
            #将该值填补到原始数组中
            array[Coordinate[0]][Coordinate[1]]=temp.pop();
        else:
            ConfirmResultOnlyMissOneNumber(suduArray);

#将替换的A 变为0
def ReplaceAwith0(array):
    ZeroIndex = [];
    for index in range(0,9):
        for i in array[index]:
            if i == 'A':
                suduArray[index][array[index].index(i)]= 0;
    #print ZeroIndex
    return ZeroIndex


if __name__ == '__main__':
    pass
	#首先确定只有一个数字的空位,然后将其补齐
    ConfirmResultOnlyMissOneNumber(suduArray);
    ReplaceAwith0(suduArray);
    for i in suduArray:
        print i
	
	


