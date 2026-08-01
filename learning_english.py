import random

print("--- БОЛЬШОЙ АНГЛИЙСКИЙ ТРЕНАЖЕР ---")
print("Пиши переводы слов на русском. Чтобы выйти, напиши: exit\n")

# Огромный продвинутый словарь для хардкорного режима
dictionary = {
    # === ХИТЫ ALAN WALKER ===
    "faded": "выцветший",
    "ignite": "воспламенять",
    "alone": "один",
    "darkside": "темная сторона",
    "spectre": "призрак",
    "tired": "уставший",
    "sing me to sleep": "спой мне перед сном",
    "where are you now": "где ты сейчас",
    "heading home": "направляюсь домой",
    "fake a smile": "притворно улыбаться",
    "diamond heart": "бриллиантовое сердце",
    "end of time": "конец времени",
    "not you": "не ты",
    "lily": "лилия",
    
    # === РАЗГОВОРНЫЙ АНГЛИЙСКИЙ (Для встречи с Аланом) ===
    "hello": "привет",
    "how are you": "как дела",
    "nice to meet you": "рад знакомству",
    "thank you": "спасибо",
    "i'm you fan": "я твой фанат",
    "your music is awesome": "твоя музыка классная",
    "can i take a photo": "можно сделать фото",
    "excuse me": "извините",
    "where are you from": "откуда ты",
    "have a nice day": "хорошего дня",
    "you are a legend": "ты легенда",
    "sign here please": "распишись здесь пожалуйста",
    
    # === КОРЛЕВСКАЯ БИТВА (Free Fire и PUBG) ===
    "safe zone": "безопасная зона",
    "gloo wall": "ледяная стена",
    "airdrop": "аирдроп",
    "headshot": "выстрел в голову",
    "booyah": "победа",
    "enemy ahead": "враг впереди",
    "need ammo": "нужны патроны",
    "weapon": "оружие",
    "skills": "навыки",
    "victory": "победа",
    "squad": "отряд",
    "survive": "выжить",
    "danger": "опасность",
    
    # === ТЕХНОЛОГИИ И КОД (VS Code) ===
    "laptop": "ноутбук",
    "code": "код",
    "game": "игра",
    "winner": "победитель",
    "team": "команда",
    "mask": "маска",
    "hoodie": "худи",
    "error": "ошибка",
    "variable": "переменная",
    "loop": "цикл"
}

words_list = list(dictionary.keys())
score = 0 # Добавим счетчик очков для интереса!

while True:
    random_word = random.choice(words_list)
    
    user_answer = input(f"Как переводится '{random_word}'?: ").lower().strip()
    
    if user_answer == "exit":
        print(f"\n👋 Тренировка окончена! Твой счет: {score} очков. See you later!")
        break
        
    if user_answer == dictionary[random_word]:
        score += 1
        print(f"🎉 Правильно! (Очки: {score}). Идем дальше...\n")

    else:
        score -= 1
        print(f"❌ Ошибка! Правильный перевод: '{dictionary[random_word]}'.")
        print(f"Штраф: -1 очко! Текущий счет: {score}\n")
        
        # Проверяем, не ушел ли счет в минус
        if score < 0:
            print("💀 GAME OVER! 💀")
            print("Ты сделал слишком много ошибок.")
            print("Попробуй запустить игру еще раз и победить. Booyah! 🏆")
            break # Останавливает цикл while и закрывает игру


