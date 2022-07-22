from random import randint, sample, choice
from tabnanny import check
from highlowlogo import vs, logo, data

# generate two person
is_game_over = False
score = 0

print(logo)
A = choice(data)


while is_game_over != True:
    B = choice(data)

    print(
        f"Compare A :  {A['name']}  a, {A['description']} from {A['country']}")
    print(vs)
    print(
        f"Compare B :  {B['name']}  a, {B['description']} from {B['country']}")
    if A['follower_count'] > B['follower_count']:
        greater = 'a'
    else:
        greater = 'b'
    print(greater)
    A = B

    check_user = input(
        "Who is more popular over the internet ? Type 'a' or 'b' ")
    if check_user == greater:
        score += 1
        print(f"You're right! Current score: {score}")
    elif check_user == greater:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"You are wrong ! your final score is {score}")
        is_game_over = True
