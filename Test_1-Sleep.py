hours_of_sleep = int(input("How many hours did you sleep today? "))

if hours_of_sleep < 7:
    print('You need more sleep!') 
elif hours_of_sleep > 9:
    print('You need less sleep!')  
else:
    print('Well-done!')           