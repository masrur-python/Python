grade = int(input("Какую оценку ты получил? (1-10): "))

if grade > 10 or grade < 1:
    print("Wrong number! Enter a grade from 1 to 10.")
elif grade >= 9:
    print("Excellent! You are a genius!")
elif grade >= 7:
    print("Good job! Keep it up!")
elif grade >= 5: 
    print("Not bad, but you can do better!") 
else:
    print("Oh no! No computer games today!")
