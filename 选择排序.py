#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/25 11:40

'''
n个记录的直接选择排序可经过n-1趟直接选择排序得到有序结果。具体算法描述如下：

1.初始状态：无序区为R[1..n]，有序区为空；
2.第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。该趟排序从当前无序区中-选出关键字最小的记录 R[k]，
将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
3.n-1趟结束，数组有序化了。
[3,2,7,5,9,10,4]

'''

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min = j
        #交换顺序
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    print(arr)
    return arr

selectionSort([3,2,7,5,9,10,4])











