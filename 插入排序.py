#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/26 16:09

def insertionSort(arr):

    for i in range(1,len(arr)):
        preIndex = i-1
        current = arr[i]
        #从已排序的数组最后一个元素开始比较，依次向前，找到位置后插入
        while preIndex>=0 and arr[preIndex]>current:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current
    print(arr)
    return arr

insertionSort([2,4,3,1,7,5,8,6])














