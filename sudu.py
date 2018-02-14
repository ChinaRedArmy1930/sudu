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
    [0, 9, 5, 0, 1, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 3, 0, 0, 6],
    [0, 0, 8, 7, 0, 6, 1, 3, 4],
    [0, 2, 9, 0, 0, 0, 6, 8, 9],
    [0, 5, 0, 9, 8, 0, 0, 2, 7]
];
A = [ 
	  [5, 1, 8, 2, 3, 9, 4, 6, 7],
	  [4, 0, 7, 2, 2, 8, 3, 5, 9] 
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
检查每一行或者每一列中是否有相同的数字
'''
def CheckSudu(array):
	for i in range(0,len(array)):
		#每一列
		v = [x[i] for x in array];
		#set 元组会自动去除重复的数据,如果长度相同就说明没有重复的数据
		if len(v) == len(set(v)):
			continue;
		else:
			print "array error!!!!"
			print len(v)
			print set(v)
			return False;
		
		#每一行
		if len(array[i]) == len(set(array[i])):
			continue;
		else:
			print v
			return False;

	
	


'''
处理完一个0的情况后,接着处理多个0的情况
'''	
def ConfirmResultMissMoreThanOneNumber(array):
	#首先保证已经将missOneZero的情况处理完了
	#然后 从上到下 从左到右 确认0所在的空格需要的数
	pass
	ZeroCoordinate = GetZeroIndex(array);
	for Coordinate in ZeroCoordinate:
		temp = JudgeNumberByIndex(array,Coordinate);
		print temp
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
	#GetZeroIndex 会将0 替换成A,防止求0的index, 每一行都是第一个的问题,这里需要将其换回
	ReplaceAwith0(suduArray);
	#if ZeroCoordinate:
	#	print ZeroCoordinate
	for Coordinate in ZeroCoordinate:
		#根据坐标得到该坐标空位的交集
		temp = JudgeNumberByIndex(array,Coordinate);
		if len(temp) == 0:
			return;
		if len(temp) == 1:
			pass
			#print temp
			#print '%d  %d '%(Coordinate[0],Coordinate[1])
			#将该值填补到原始数组中
			#因为只缺一个数字，因此可以直接将其POP到array中,当填写一个数后
			#重新执行该函数,防止本来A空位 Miss 多个数字,但是B空位补全后,本可以补全
			#A空位,但是却没有补全的问题。
			array[Coordinate[0]][Coordinate[1]]=temp.pop();
			ConfirmResultOnlyMissOneNumber(suduArray);
		else:
			pass

'''
确定Miss多个数的情况
'''
def ConfirmServerNumber(array):
    pass

'''
确认9宫格中的缺一个的情况
'''
def ConfirmOneNumIn99Matrix(array, index):
    pass
    #首先需要使用查表法确认给定的坐标在9宫格中的哪个位置
    MatrixArrayTable = [
                        [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]],
                        [[0,3],[0,4],[0,5],[1,3],[1,4],[1,6],[2,3],[2,4],[2,5]],
                        [[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]],
                        [[3,0],[3,1],[3,2],[4,0],[4,1],[5,2],[5,0],[5,1],[5,2]],
                        [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]],
                        [[3,6],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]],
                        [[6,0],[6,1],[6,2],[7,0],[7,1],[7,2],[8,0],[8,1],[8,2]],
                        [[6,3],[6,4],[6,5],[7,3],[7,4],[7,5],[8,3],[8,4],[8,5]],
                        [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]],
                       ];
    ind = [index[0],index[1]];
    arrayindex = 0;
    missindex = [];
    #sudumissindex 得到的是缺失的空格位置的确切坐标
    sudumissindex = [];
    for i in range(0,9):
        if ind in MatrixArrayTable[i]:
            arrayindex = i;
            #print arrayindex
    #print MatrixArrayTable[arrayindex];
    #计算给定的坐标集合的坐标缺几个数
    #得到index所在的矩阵的所有数
    sudu33MatrixArray = [];
    for i in MatrixArrayTable[arrayindex]:
        sudu33MatrixArray.append(suduArray[i[0]][i[1]]);
    #print sudu33MatrixArray

    #如果只有一个数缺失,就将填写到数组中 如果没有则不管
    print len(set(sudu33MatrixArray))
    if (len(set(sudu33MatrixArray)) == 9) and (0 in set(sudu33MatrixArray)):
        for i in range(0,9):
          if i not in sudu33MatrixArray:
              #这里得知i就是当前矩阵缺失的数字,将i填写到原始数组中
              #得到当前3*3矩阵的数组0的index
              #MatrixArrayTable[arrayindex] 得到的是数独数组的某一行的坐标集合
              #print "i:%d"%i
              missindex = sudu33MatrixArray.index(0) 
              #print "missindex:%d"%missindex
              #print MatrixArrayTable[arrayindex][missindex]
              sudumissindex = MatrixArrayTable[arrayindex][missindex];
              array[sudumissindex[0]][sudumissindex[1]] = i
    else:
        pass

    #将得到的坐标位置填写缺失的数字

	













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
    for i in suduArray:
    	print i
    #CheckSudu(A);
    #首先确定只有一个数字的空位,然后将其补齐
    #ConfirmResultOnlyMissOneNumber(suduArray);
    #ReplaceAwith0(suduArray);
    #for i in suduArray:
    #	print i
    #ConfirmResultMissMoreThanOneNumber(suduArray);
    v = [8,7];
    ConfirmOneNumIn99Matrix(suduArray,v);
    for i in suduArray:
        print i
    
	
	


