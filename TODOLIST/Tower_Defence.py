import random

tower = 50
player = 20
def tower_image():
    print("|----------|")
    print("|      /   |")
    print("| /        |")
    print("|----------|")
    print("|      /   |")
    print("| /        |")
    print("|----------|")

tower_image()
print("    ")
print("Welcome to Tower Defence")
print("    ")
bullet = int(input("How may armour will you carry: "))

while True:
    random_shoot = random.randint(0, bullet)
    shot = int(input("How many bullets will you shoot: "))
    bullet -= shot
    if shot == random_shoot:
        tower -= shot*2
        print("Tower is hit with", shot*2, "shots")
        print("Tower is left with", tower, "life")
    else:
        player -= shot/2
        print("Tower defends, Player is hit with", shot/2,"shots")
        print("You have", player, "life left")

    if tower < 1:
        print("You won the Game")
        break
