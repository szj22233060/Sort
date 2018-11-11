#coding=utf-8
#milo22233060@gmail.com
#2018/10/29 13:25

#范围为1~max的桶排序
def bucketSort1(arr,max):
    mid = [0 for i in range(max+1)]
    for i in arr:
        mid[i] = mid[i]+1
    print(mid)
    result = []
    for i in range(len(mid)):
        while mid[i] > 0:
            result.append(i)
            mid[i] -= 1
    print(arr)
    print(result)

#区间[0,1)均匀分布的桶排序
def bucketSort2(arr):
    result = []
    n = len(arr)
    #嵌套数组，n个元素
    s = [[] for i in range(n)]
    #将每个元素放进对应的桶中
    for i in arr:
        s[int(i*n)].append(i)

    #两种排序相结合
    for i in s:
        insert(i)
        result.extend(i)
    print(result)
    return result
#辅助函数，插入排序
def insert(arr):
    for i in range(1,len(arr)):
        pre = i-1
        key = arr[i]
        while pre >= 0 and arr[pre] >= key:
            arr[pre+1] = arr[pre]
            pre -= 1
        arr[pre+1] = key

# arr = [3,4,3,7,8,5,6,7,1,2,4,5,2,6,7,5,1,9]
# bucketSort1(arr,9)

arr1 = [0.2,0.4,0.5,0.8,0.3,0.7]
bucketSort2(arr1)











