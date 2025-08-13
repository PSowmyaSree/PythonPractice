import random

min_number=int(input("Enter Min range number:"))
max_number=int(input("Enter Max range number:"))
ran_number=random.randint(min_number,max_number)
count=5
match=False
for i in range(count):
    print(f"Attempt {i+1} :Enter number")
    try:
        guess = int(input())
    except ValueError:
        print("Please enter a valid number within the range")
        continue
    if guess in range(min_number,max_number+1 ):
        if guess==ran_number:
            print("Success!! Exact Match")
            match=True
            break
        elif guess<ran_number:
            print("Your guess is lower than the actual number")
        elif guess>ran_number:
            print("Your guess is higher than the actual number")
    else:
        print("your number is not within the range")
if match==False:
   print("Number of attempts exceeded, try again later")    
