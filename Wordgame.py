import random
def readtext():
    with open("Words.txt", "r") as f:
        words=f.readlines()
    return [word.strip() for word in words]
def showword(word, guesses):
    target=""
    for l in word:
        if l in guesses:
            target += l
        else:
            target += "_"
    return target 
def playgame(words):
    word= random.choice(words)
    word_guess = 0
    guesses=set()
    count=0
    while True:
        print(f"the secret word is{showword(word, guesses)}")
        choice=input("guess a letter")
        if len(choice)==1:
            count += 1
            guesses.add(choice)
        elif len(choice)>1:
            word_guess += 1
            if choice == word:
                print("Correct!")
                return
            else:
                print("Try again!")
        else:
            print("Please type a letter")
        if all(l in guesses for l in word):
            print("you guessed the word!")
if __name__ == "__main__":
    words= readtext()
    playgame(words)