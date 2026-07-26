import random

print("---НАЧАЛО БИТВЫ ---")
print("Нажимаи Enter, чтобы ударить. Для выхода напиши 'exit'.")

while True:
    action = input("\n[Твой ход]: ")
    if action == "exit":
        print("Вы вышли из боя. Конец игры!")
        break 

    chance = random.randint(1,100)
    base_damage = 20

    print(f"Выброшено число удачи: {chance}")

    if chance > 80:
        critical_damage = base_damage * 2
        print(f"CRITICAL HIT!!! Вы нанесли {critical_damage} урона!")
    else:
        print(f"Обычный удар. Вы нанесли {base_damage} урона!")

