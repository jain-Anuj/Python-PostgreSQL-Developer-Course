# User can pick 6 numbers
# Lottery Calculate 6 random numbers(betwwen 1 and 20)
# Then we match the user number to the lottery numbers
# Calculate the winning based on how mani numbers the user matched
import random
def get_player_numbers():
    number_csv = input("Enter 6 numbers, seperated by commas: ")
    number_list = number_csv.split(",")
    integer_set = {int(number) for number in number_list}
    return integer_set

def create_lottery_number():
    values =set()
    while len(values)<6:
        values.add(random.randint(1,20))
    return values

def menu():
    player_numbers = get_player_numbers()
    lottery_number = create_lottery_number()
    matched_numbers = lottery_number.intersection(player_numbers)
    print("You Matched numbers {}.\nYou won {} ".format(matched_numbers,100 ** len(matched_numbers)))


menu()
