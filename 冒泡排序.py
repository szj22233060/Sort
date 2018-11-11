#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/25 10:38
'''
1.比较相邻的元素。如果第一个比第二个大，就交换它们两个；
2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
3.针对所有的元素重复以上的步骤，除了最后一个；
4.重复步骤1~3，直到排序完成。
[3,2,7,5,9,10,4,]

'''
import time

def bubbleSort(arr):
    print(arr)
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    print(arr)

# 优化，减少比较次数，设置一个flag，
def bubbleSort1(arr):
    print(arr)
    k = len(arr)-1
    #设置pos位置标记，j后面没有进行排序，pos=j，下一趟扫描就只循环到pos
    pos = 0
    for i in range(len(arr)-1):
        #设置flag标记,如果发生了交换flag=1
        flag = 0
        for j in range(k):
            if arr[j]>arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                flag = 1
                pos = j
        k = pos
        #没有发生交换就推出循环
        if flag == 0:
            break
    return arr
now = time.clock()
bubbleSort1([1,2,3,4,5,6,7])
print(time.clock()-now)


