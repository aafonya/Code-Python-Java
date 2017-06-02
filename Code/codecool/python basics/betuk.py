def countLetters(word):
    betuk = []
    for i in word:
        if i in betuk:
            continue
        betuk.append([i, 0])

    for i in betuk:
        for j in list(word):
            if i[0] == j:
                i[1] += 1

    for i in betuk:
        i = tuple(i)
    return betuk

print(countLetters("google"))
