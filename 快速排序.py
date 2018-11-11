#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/28 9:49

#设置i，j作为指针，指向要排序数组的头尾，找一个基准，一般是数组开头。
#在i<j的情况下，大于基准key的交换到后面，小于key的交换到前面，直到i=j。
#将前后数组继续递归调用排序，直到排序完成。

def quickSort(arr,start,end):
    if start<end:
        #i,j指针指向数组起始位置
        i, j = start, end
        key = arr[i]
        while i<j:
            #小于key时，交换到前面
            while i<j and arr[j]>=key:
                j -= 1
            arr[i] = arr[j]
            while i<j and arr[i]<=key:
                i += 1
            arr[j] = arr[i]
        #将中间的数替换为key
        arr[i] = key
        #递归调用
        quickSort(arr,start,i-1)
        quickSort(arr,j+1,end)
    return arr

arr = [3,5,1,2,7,4,8,9]
print(quickSort(arr,0,len(arr)-1))













