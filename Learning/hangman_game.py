import random
import animals

words=animals.word

hangman_art={
    0:("   ",
       "   ",
       "   "),
    1:(" O ",
       "   ",
       "   "),
    2:(" O ",
       " | ",
       "   "),
    3:(" O ",
       "/| ",
       "   "),
    4:(" O ",
       "/|\\",
       "   "),
    5:(" O ",
       "/|\\",
       "/  "),
    6:(" O ",
       "/|\\",
       "/ \\")       
}


def display_man(wrong_guesses):
    print("\n*************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*************\n")
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("".join(answer))
    print()

def main():
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrong_guesses=0
    guessed_letters=set()
    is_running=True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        
        guess=input("\nEnter a letter of Animal: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.\n")
            continue

        if not guess.isalpha():
            print("\nPlease enter a letter.")

        if guess in guessed_letters:
            print("\nYou already guessed this letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess

        else:
            wrong_guesses+=1

        if "_" not in hint:
            display_man(wrong_guesses)
            print("Correct Answer: ",end="")
            display_answer(answer)
            print("You Win!")
            is_running=False
        elif wrong_guesses>=len(hangman_art)-1:
            display_man(wrong_guesses)
            print("Correct Answer: ",end="")
            display_answer(answer)
            print("You Lose!")
            is_running=False



if __name__=='__main__':
    main()
