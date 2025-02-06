from ordered_list import get_ordered_list 
def search_ordered_list(lst, target):
    ordered_list = get_ordered_list(lst)
    low = 0
    high = len(ordered_list) - 1
    while low<=high:
        mid = (low+high)//2
        if ordered_list[mid] == target:
            return True
        elif ordered_list[mid]<target:
            low = mid+1
        else:
            high = mid-1
    return False
    
print(search_ordered_list([5,3 ,2, 7, 1, 9], 5))