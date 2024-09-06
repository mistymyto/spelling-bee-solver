def main():
    print("Welcome to the spelling bee solver!")
    interChar = interCharCheck()
    outerCharsList = outerCharsCheck(interChar)
    absoluteSolver(interChar, outerCharsList)

def interCharCheck():
    while True:
        interChar = input("Type the center letter: ").lower()
        if len(interChar) == 1 and interChar.isalpha():
            return interChar
        else:
            print("You have not typed a valid letter")
    
def outerCharsCheck(interChar):
    while True:
        outerChars = input("Type 6 outer letters: ").lower()
        outerCharsList = list(outerChars)
        if len(outerChars) == 6 and len(outerCharsList) == len(set(outerCharsList)) and interChar not in outerChars and outerChars.isalpha():
            return outerCharsList
        else:
            print("You have not typed 6 unique letters")

def absoluteSolver(interChar, outerCharsList):
    with open("words.txt", "r") as file:
        vocab = [item.strip().lower() for item in file.readlines()]

    for word in vocab:
        wordLen = len(word)
        if wordLen < 4 or interChar not in word or any(char not in outerCharsList and char not in interChar for char in word):
            continue
        else:
            print(word)
            
if __name__ == "__main__":
    main()
