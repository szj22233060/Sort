#coding=utf-8
#milo22233060@gmail.com
#2018/10/29 16:36
'''
基数排序一般用于长度相同的元素组成的数组。首先按照最低有效数字进行排序，然后由低位向高位进行。
长度给出,基数排序可以看做是进行多趟桶排序。每个有效数字都在0-9之间，很适合桶排序，建10个桶很方便.
'''

def radixSort(arr,length):
    for i in range(length):
        s = [[] for j in range(10)]
        for k in arr:
            #求相应位的值
            s[int(k/(10**i)%10)].append(k)
        #将每一个桶里的元素取出,可以放进原数组
        arr = []
        for a in s:
            arr.extend(a)
    print(arr)
    return arr

arr = [221,234,233,445,556,123,1,3,13,14,15,112]
radixSort(arr,3)










