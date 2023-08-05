""" Inserting element at the right position """

def Insertion_sort(list_a):
    l = len(list_a)
    for i in range(1,l):
        current =  list_a[i]
        j= i-1
        while(j >= 0 and current < list_a[j]):
            
            list_a[j+1] = list_a[j]   # Moving element towards right position
            j -= 1

        list_a[j+1] = current # Inserting element to it's correct position

    return list_a


def main():
    list_a = list(map(int, input().split()))
    print(Insertion_sort(list_a))
main()