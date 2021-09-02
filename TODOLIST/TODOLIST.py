import random

user = "Jude"

task = ["Give Donation to the needy", "Help your neighbour", "Join Public Services", "Read a new Book"]
taskx = int(input(f"Hello {user}, There are 4 tasks from the task menu \nHow many task do which to accomplish today: "))



while True:
    if taskx == 1:
        print(random.sample(task, k=1))
        break
    elif taskx == 2:
        print(random.sample(task, k=2))
        break
    elif taskx == 3:
        print(random.sample(task, k=3))
        break
    elif taskx == 4:
        print(random.sample(task, k=4))
        break
    elif taskx > 4:
        print(r"Sorry there ar only 4 task in the task menu, Please select between 1 to 4 task")
        break
    else:
        print("No task to be done today")
        break