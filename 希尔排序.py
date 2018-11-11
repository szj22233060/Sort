#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/26 16:31

'''
void shellSort(vector<int> &nums) {
    int n = nums.size();
    int gap, i, j;

    for(gap = n/2; gap > 0; gap /= 2) {
        //插入排序简洁写法
        for(i = gap; i < n; i++) {
            int num = nums[i];
            for(j = i-gap; j>=0 && nums[j]>num; j-=gap)
                nums[j+gap] = nums[j];
            nums[j+gap] = num;
        }
    }
}
'''
#动态定义间隔序列
def shellSort(arr):
    gap = len(arr) // 2
    while gap >= 1:
        for j in range(gap,len(arr)):
            i = j
            while i-gap >= 0:
                if arr[i]<arr[i-gap]:
                    arr[i],arr[i-gap] = arr[i-gap],arr[i]
                    i -= gap
                else:
                    break
        gap //= 2
    print(arr)
    return arr
shellSort([3,2,4,5,1,8,6,7])






