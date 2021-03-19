win_check = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}
flag = True

while(flag):
    p1 = input("Player 1, Rock,Paper or Scissors?: ").lower()
    p2 = input("Player 2, ROck, paper or Scissors?: ").lower()

    if(p1 == p2):
        print("Draw")

    elif(win_check.get(p1) == p2):
        print("Player 1 wins !")

    else:
        print("Player 2 wins !")

    input_ = input("Do you want to start a new game ? [Y/N]")
    if(input_ == "Y" or input_ == "y"):
        flag = True
    elif(input_ == "N" or input_ == "n"):
        flag = False
