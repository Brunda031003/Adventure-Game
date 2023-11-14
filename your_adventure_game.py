print("Welcome!")

start=input("Do you want to experience some Adventure?... Type yes to start.").lower()

if start=="yes":
    print("Buckle-up for your adventure!")
else:
    quit()

print("You wake up to find yourself in a spaceship, tied to a chair. You don't remember how you got there and you try to escape.")
choice = input("Do you try to break the ties or call for help? (break/call): ")

if choice == "break":
    print("You struggle against the ties, but they are too strong. You give up and call for help.")
    choice = input("A voice tells you to remain calm and that they will help you. Do you trust them? (trust/not): ")

    if choice == "trust":
        print("The voice opens the door to your cell and leads you out of the spaceship. You are grateful for their help and return to your home.")
    elif choice == "not":
        print("You refuse to trust the voice and continue to struggle against the straps. Eventually, the voice gets impatient and leaves you in the cell.")
        print("You are stuck in the spaceship, with no way to escape. You starve to death.")
else:
    print("You call for help, and a few minutes later, a door opens to your cell. A guard enters and asks you what you are doing here.")
    choice = input("Do you tell the guard the truth or lie? (truth/lie): ")

    if choice == "truth":
        print("You tell the guard that you don't remember how you got there, but you know you don't belong on the spaceship. The guard believes you and helps you escape.")
        print("You return to your home, safe and sound.")
    elif choice == "lie":
        print("You tell the guard that you are a crew member, but you just lost your memory. The guard takes you to the crew quarters, but you are soon discovered to be an imposter.")
        print("You are thrown into the spaceship's brig, where you are eventually executed.")

print("Hope you had FUN!\nSee You Again!")
