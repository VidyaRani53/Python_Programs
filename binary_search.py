''' write a program to search an element using using binary search'''
def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if key==arr[mid]:
            return "found"
        elif key<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return "not found"

arr=list(map(int,input().split()))
key=int(input())
print(binary_search(arr,key))
        
