T = int(input())
word = []
for i in range(T):
    w = input();
    if (w in word):
        word.remove(w);
    word.append(w);
    
word.sort();

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = len(arr[len(arr) // 2])
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if len(num) < pivot:
            lesser_arr.append(num)
        elif len(num) > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

word = quick_sort(word);
for i in word:
    print(i)