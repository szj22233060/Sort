#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/28 8:53

'''
归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。
若将两个有序表合并成一个有序表，称为2-路归并。
'''

def mergeSort(arr):
    if len(arr)<2:
        return arr
    mid = len(arr)//2
    left = arr[0:mid]
    right = arr[mid:]
    print(left,'---',right)
    #递归调用本身，进行排序
    return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
    result = []
    while len(left)>0 and len(right)>0:
        print(left,'--',right)
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left)>0:
        result.extend(left)
    if len(right):
        result.extend(right)
    print(result)
    return result

print(mergeSort([3,5,7,6,4,2,1,9,0]))









