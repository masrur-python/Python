coins = int(input("How many coins do you have? "))

if coins < 500:
    print("Not enough coins! Go play more.")
elif coins == 500:
    print("Perfect! You have exactly enough for the skin.")
else:
    print("You are rich! Buy the skin and save the rest.")
