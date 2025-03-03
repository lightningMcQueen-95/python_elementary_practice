import random



no_of_remaning_chance = 0

print("Dice Rolling Game")



print("Start Game")

print("How many chance's you should play\n")

n=input()



while no_of_remaning_chance<int(n):

  input("rolling dice(press any keyword):")



  no_of_remaning_chance = no_of_remaning_chance + 1



  d1 = random.randint(1,6)

  d2 = random.randint(1,6)



  print(d1,d2)



  if d1==d2:

    print("you win\n")

    break

  else:

    print("Not win")



  print(f"{int(n) - no_of_remaning_chance} chance left out of {int(n)}\n")



print("Game Over")
