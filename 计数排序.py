#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/29 12:36

def countingSort(arr,max):

    result = [0 for i in range(len(arr))]
    mid = [0 for i in range(max+1)]
    for i in arr:
        mid[i] = mid[i]+1

    #累加，A0,A1,A2....Ai：相应位置的值在结果中哪一位,i的值在Ai位
    for i in range(1,len(mid)):
        mid[i] = mid[i]+mid[i-1]

    for i in arr:
        result[mid[i]-1] = i
        mid[i] -= 1
    return result

arr = [3,4,3,7,8,5,6,7,1,2,4,5,2,6,7,5,1,9]
countingSort(arr,9)





