import wordfreq
import tkinter

solution = wordfreq.random_words(lang="de", nwords=1)
indicator = ["_"]*len(solution)
errors = 0

#print(solution)
"""
while("_" in indicator):

    print((" ").join(indicator))
    char = input("Buchstabe: ").lower()

    if(char in solution):
        for i in range(len(solution)):
            if(solution[i] == char):
                indicator[i] = char
        print("richtig")
    else:
        print("falsch")
        errors += 1
        if(errors == 7):
            break

print("Lösung: "+ solution)
"""
root = tkinter.Tk()
root.title("Galgenmännchen")

label_indicator = tkinter.Label(root)
label_indicator.pack()
label_indicator.config(text=" ".join(indicator))

eingabe = tkinter.Entry(root, justify="center")
eingabe.pack()

button = tkinter.Button(root, text="senden")
button.pack()

root.mainloop()
