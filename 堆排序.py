#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/29 10:49
'''
通常堆是通过一维数组来实现的。在阵列起始位置为0的情况中
(1)父节点i的左子节点在位置(2*i+1);
(2)父节点i的右子节点在位置(2*i+2);
(3)子节点i的父节点在位置(i-1)//2;
'''

#调整堆
def MAX_Heapify(heap,HeapSize,root):
    left = 2*root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right <HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:
        heap[larger],heap[root] = heap[root],heap[larger]
        MAX_Heapify(heap,HeapSize,larger)


#构建堆
def Build_MAX_Heap(heap):
    HeapSize = len(heap)
    for i in range((HeapSize-2)//2,-1,-1):
        MAX_Heapify(heap,HeapSize,i)

#取堆顶元素
def HeapSort(heap):
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        MAX_Heapify(heap,i,0)
        print(heap)
    return heap


arr = [2,3,5,4,1,8,6,7,9]
HeapSort(arr)
print(arr)
