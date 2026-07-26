inventory = ["меч", "зелье здоровья", "щит"]

print("--- ТВОЙ ИНВЕНТАРЬ ---")
print(inventory)

items_count = len(inventory)
print(f"Всего предметов в рюкзаке: {items_count}")


print(f"Твое главное оружие: {inventory[0]}")

print("\n...Вы открыли сундук и нашди золото!...")
inventory.append("золото")

print("Теперь твой инвентарь выглядить так:")
print(inventory)
