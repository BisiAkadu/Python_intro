import random
upper_bound = 20
lower_bound = 1
#to_be_guessed = int(n * random.random()) + 1
jack = random.randint(lower_bound, upper_bound)
guess = 0
while guess != jack:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > jack:
            print("Number too large")
        elif guess < jack:
            print("Number too small")
        elif guess == jack:
            print("congrats u got me")
    else:
        # 0 means giving up
        print("Sorry that you're giving up!")
        break   # break
 