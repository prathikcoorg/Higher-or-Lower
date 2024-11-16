from game_data import data
import random
from art import logo,vs



def format_data(account):
    account_name = account("name")
    account_descr = account("description")
    account_country = account("country")
    return f"{account_name}, a {account_descr} ,from {account_country}"

#
def check_answer(user_guess,a_follower,b_follower):
   if a_follower > b_follower:
       return user_guess == 'a'
   else:
       return user_guess =='b'

print(logo)
game_continue = True
score = 0
account_b = random.choice(data)

while game_continue:

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

        print(f"comapre a :{format_data(account_a)}")
        print(vs)
        print(f"against b:{format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B").lower()

        print("\n"*20)
        print(logo)

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess,a_follower_count,b_follower_count)

        if is_correct:
            score += 1
            print(f"you are right correct score is {score}")

        else:
            print(f"sorry that's wrong final score is {score}")
