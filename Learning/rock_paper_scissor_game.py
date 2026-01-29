import random
import time

options =("rock","paper","scissor")
playing=True

while playing:
    player=None
    computer = random.choice(options)

    while player not in options:
        player = input("\nPlease enter a choice (rock,paper,scissor): ")

    print(f"\nYour Choice: {player}")
    print(f"Computer's Choice: {computer}")
    time.sleep(1)

    if player==computer:
        print(f"\nBoth players selected {player}. It's a tie!")
    elif player=="paper" and computer=="rock":
        print(f"\nPaper covers rock! You win!")
    elif player=='rock' and computer=='scissor':
        print(f"\nRock crushes scissor! You win!")
    elif player=='scissor' and computer=='paper':
        print(f"\nScissor cuts paper! You win!")
    else:
        print("\nYou Lost!! Computer wins!")

    play_again=input("\nPlay again? (y/n): ")

    if play_again=='n':
        playing=False

        