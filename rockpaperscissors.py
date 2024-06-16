import random
print("ROCK PAPER SCISSORS")
print("Instructions:")
print(" ROCK beats SCISSORS\n SCISSORS beats PAPER\n PAPER beats ROCK")
comp_score=0
user_score=0
play=True
while play:
    print("Enter option :")
    user=input()

    d=("Rock","Paper","Scissors")
    comp=random.choice(d)
    print("Computer Choice: ",comp)
    if comp==user:
        print("PLAY AGAIN")
        continue
    elif comp=="ROCK" and user=="PAPER" :
        print("YOU WIN")
        user_score+=1
    elif comp=="ROCK" and user=="SCISSORS" :
        print("YOU LOSE")
        comp_score+=1
    elif comp=="PAPER" and user=="ROCK" :
        print("YOU LOSE")
        cp+=1
    elif comp=="PAPER" and user=="SCISSORS":
        print("YOU WIN")
        user_score+=1
    elif comp=="SCISSORS" and user=="ROCK":
        print("YOU WIN")
        user_score+=1
    else :
        print("YOU LOSE")
        comp_score+=1
    print("DO U WANNA PLAY AGAIN? (YES OR NO) : ")
    yn=input()
    if yn=="YES":
        continue
    else:
        print("GAME OVER")
        play=False
print("SCORECARD:")
print("YOU: ",user_score)
print("COMPUTER: ",comp_score)
