""" Bubble Sort """
""" Compare consicutive numbers and sort them """

def Bubble_sort(list_a):
    l = len(list_a)
    for i in range(l):
        for j in range(l-i-1):
            temp  = list_a[j+1]
            if (list_a[j] > list_a[j+1]):
                list_a[j+1] = list_a[j]
                list_a[j] = temp
    return list_a

def main():
    list_a = list(map(int, input().split()))
    print(Bubble_sort(list_a))

main()