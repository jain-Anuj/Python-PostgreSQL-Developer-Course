import random
def ask_user_and_check_number():
    user_number = int(input("Enter your number between 0 and 9 "))
    if user_number not in magic_numbers:
      return "You didn't quite get it."
    else :
      return "You got the number right!"

magic_numbers = [random.randint(0,9),random.randint(0,9)]
def run_program_x_times(chances):
    for i in range(chances):
        print("This is attempt "+str(i+1))
        print(ask_user_and_check_number())

run_program_x_times(int(input("Enter the number of time you want to play ")))
