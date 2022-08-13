# Who are you in horror a movie?
# This application is a game simulation of who you would be in a movie, based
# on data such age.

def main():
    try:
        print("\nHorror Movie v0.1.1, by Carlos Moura")
        print("\nStarting the game... Press Ctrl+C to stop.\n")
        begin_loop()
    except KeyboardInterrupt:
        print("\n\nInterrupted by the user!")

def begin_loop():
    while True:
        play()


def play(): #test conditional for ages
    answer = input("Are you READY? ")
    if answer.lower() == "no":
        print ("All right, let's begin!")
        try:
            age = int(input("What is your age? "))
            if age >= 90:
                print ("You will probably die very soon...")
            elif age <= 18:
                print ("You need to hide.")
            else:
                print ("You live!")
        except ValueError:
            print("You informed a invalid data... Get out of here!")
    else:
        print("No, you are not ready!")


if __name__ == "__main__":
  main()

