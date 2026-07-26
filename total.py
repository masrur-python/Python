# initial — это золото, которое уже лежит в кармане
# *quest_rewards — мешок с наградами за обычные квесты
# **boss_rewards — мешок с наградами за убийство боссов
def calculate_gold(initial=5, *quest_rewards, **boss_rewards):
    total_gold = initial
    
    # Считаем обычные награды (одна звёздочка в книге)
    for gold in quest_rewards:
        total_gold += gold
        
    # Считаем награды за боссов (две звёздочки в книге)
    for boss_name in boss_rewards:
        total_gold += boss_rewards[boss_name]
        
    return total_gold

# --- ИГРОВОЙ ВЫЗОВ ---
# У тебя в кармане 10 золотых.
# Ты прошёл 3 маленьких квеста (дали 1, 2 и 3 золота)
# И убил двух боссов: Дракона (50 золота) и Зомби (100 золота)
final_score = calculate_gold(10, 1, 2, 3, dragon=50, zombie=100)

print(f"Всего золота у игрока: {final_score}")
