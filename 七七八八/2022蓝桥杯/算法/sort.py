import random
def bubble_sort(list):
    for i in range(len(list)-1):
        for x in range(len(list)-1-i):
            if list[x] > list[x+1]:
                list[x],list[x+1] = list[x+1],list[x]
list = [random.randint(1,10000) for x in range(100)]
#bubble_sort(list)
def select_sort(list):
    for i in range(len(list)-1):
        min_index = i
        for x in range(i+1,len(list)):
            if list[min_index] > list[x]:
                min_index = x
        if min_index != i:
            list[i],list[min_index] = list[min_index],list[i]

def insert_sort(list):
    for i in range(1,len(list)):
        key = list[i]
        hand = i-1
        while key < list[hand] and hand >=0:
            list[hand+1] = list[hand]
            hand -= 1
        list[hand+1] = key

def partition(list,left,right):
    temp = list[left]
    while left < right:
        while left < right and list[right] >= temp : # 从右面找比temp小的数
            right -= 1     # 往左走一步
        list[left] = list[right]  # 把右边的值写到左边的空位上
        while left < right and list[left] <= temp:
            left += 1
        list[right] = list[left]   # 把左边的值写到右边的空位上
    list[left] = temp
    return left
def quick_sort(list,left,right):
    if left < right:  # 至少两个元素
        mid = partition(list, left, right)
        quick_sort(list, left, mid-1)
        quick_sort(list, mid+1, right)

def sift(lst, low, high):
    i = low
    j = (2 * i) + 1
    temp = lst[i]
    while j <= high:
        if j < high and lst[j] > lst[j + 1]:
            j += 1
        if lst[j] < temp:
            lst[i] = lst[j]
            i = j
            j = (2 * i) + 1
        else:
            break
    lst[i] = temp

def topk(lst, k):
    heap = lst[:k]
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)
    for i in range(k, len(lst)):
        if lst[i] > heap[0]:
            heap[0] = lst[i]
            sift(heap, 0, k - 1)
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap


def heap_sort(list):
    n = len(list)
    for i in range((n//2)-1,-1,-1):
        sift(list, i, n-1)
    for i in range(n-1,-1,-1):
        list[0],list[i] = list[i],list[0]
        sift(list,0, i-1)

def merge(arr, low, mid, high):
    i = low
    j = mid + 1
    list1 = []
    while i <= mid and j <= high:
        if arr[i] < arr[j] :
            list1.append(arr[i])
            i += 1
        else:
            list1.append(arr[j])
            j += 1
    while i <= mid:
        list1.append(arr[i])
        i += 1
    while j <= high:
        list1.append(arr[j])
        j += 1
    arr[low:high+1] = list1
def merge_sort(list,low,high):
    if low < high : # 至少有两个元素
        mid = (low + high) // 2
        merge_sort(list,low,mid)
        merge_sort(list,mid+1,high)
        merge(list,low,mid,high)

def insert_sort_gap(list,gap):
    for i in range(gap,len(list)):
        key = list[i]
        hand = i-gap
        while key < list[hand] and hand >=0:
            list[hand+gap] = list[hand]
            hand -= gap
        list[hand+gap] = key
def shell_sort(list):
    gap = len(list)//2
    while gap >=1 :
        insert_sort_gap(list,gap)
        gap //= 2

def count_sort(list,count):
    list4 = [0 for i in range(count+1)]
    for x in list :
        list4[x] += 1
    list.clear()
    for ind,val in enumerate(list4):
        for x in val:
            list.append(ind)





