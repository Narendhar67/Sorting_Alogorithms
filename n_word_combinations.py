def n_word_combinations(words,n):
    combinations = []

    for i in range(len(words)):
        combinations.append([i])
    
    iteration = 0
    while iteration < n-1:
        new_combinations = []
        for combination in combinations:
            for i in range(combination[-1]+1 , len(words)):
                new_combination = combination + [i]
                new_combinations.append(new_combination)
        combinations = new_combinations
        iteration += 1
    # print(combinations)

    word_combinations = []
    for combination in combinations:
        word_combination = []
        for i in combination:
            word_combination.append(words[i])
        word_combinations.append(word_combination)
        print(*word_combination)
    
    return word_combinations

def main():
    words = input("Enter list of words(space separated) : ").split()
    n = int(input("enter number of words per combinations: "))
    n_word_combinations(words,n)
main()