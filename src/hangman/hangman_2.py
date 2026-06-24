import wordfreq

solution = wordfreq.random_words(lang="de", nwords=1)
indicator = ["_"]*len(solution)

while ("_" in indicator):
    print(" ".join(indicator))
    char = input("Buchstabe: ").lower()

    if (char in solution):
        for i in range(len(solution)):
            if(solution[i] == char):
                indicator[i] = char
        print("richtig")
    else:
        print("falsch")

print("Lösung: " + solution)