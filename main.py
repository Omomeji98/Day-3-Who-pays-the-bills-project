import random
# todo 1 import random module
list_of_names = []
# todo 2 create and empty list and user and input() to get names from user.


# todo 3 create an infinite loop that keeps asking for names until the user doesn't give input anymore
while True:
    names = input("What is your name?\n")
    if names == "":
        break
    list_of_names.append(names)

# todo 4 Check if list is not empty
if list_of_names:
    name = random.choice(list_of_names)
    print(f"This is the list {list_of_names}")
    print(f"{name} will pay the bills")
else:
    print(f"No names in the list")
# todo 5: randomly choose who pays the bills


