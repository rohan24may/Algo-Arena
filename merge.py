def merge_sort(arr,low,high):
    if low < high :
        mid=(low + high ) // 2
        merge_sort(arr,low ,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)


def merge(arr,low,mid,high):
    temp=[]
    i=low
    j=mid+1

    while i <=mid and j <=high :
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i+=1

        else:
            temp.append(arr[j])
            j+=1

    while i <=mid :
        temp.append(arr[i])
        i+=1
    while j <=high:
        temp.append(arr[j])
        j+=1

    for k in range(len(temp)) :
       arr[low + k ] = temp[k] 



# Main
arr = [5, 2, 8, 1, 3]

merge_sort(arr, 0, len(arr) - 1)

print(arr)