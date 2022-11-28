import random

while True:
    user_action = input("Kirjuta valiku (kivi, paber, käärid): ")
    possible_actions = ["kivi", "paber", "käärid"]
    computer_action = random.choice(possible_actions)
    print(f"\nSa valisid {user_action}, arvuti valis {computer_action}.\n")

    if user_action == computer_action:
        print(f"Kaks mängijad valisid {user_action}. see on viik!")
    elif user_action == "kivi":
        if computer_action == "käärid":
            print("Kivi lõi käärid! Saa võitsid!")
        else:
            print("Paber sõi kivi! Saa kaotasid.")
    elif user_action == "paber":
        if computer_action == "kivi":
            print("Paber sõi kivi! Saa võitsid!")
        else:
            print("Käärid lõikasid paberi! Saa kaotasid.")
    elif user_action == "käärid":
        if computer_action == "paber":
            print("Käärid lõikasid paberi! Saa võitsid!")
        else:
            print("Kivi lõi käärid! Saa kaotasid.")

    play_again = input("Mängid jälle? (j/e): ")
    if play_again.lower() != "j":
        break