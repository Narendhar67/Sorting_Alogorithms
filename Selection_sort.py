""" Selection Sort """

def Selection_sort(list_a):
    l = len(list_a)
    for i in range(l):
        min_value_index = i
        for j in range(i+1,l):
            if list_a[j] < list_a[min_value_index] :
                min_value_index = j
        temp = list_a[i]
        list_a[i]= list_a[min_value_index]
        list_a[min_value_index] = temp
    return list_a

def main():
    list_a = list(map(int, input().split()))
    print(Selection_sort(list_a))
main()