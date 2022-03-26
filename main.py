questions = ["My name __ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
correct = 0

print("Привет! Предлагаю проверить свои знания английского! Наберите 'ready', чтобы начать!")

user_input = input()

if user_input.lower() != "ready":
    print("Кажется, вы не хотите играть. Очень жаль.")
else:
    print(questions[0])
    user_answer1 = input()
    if user_answer1 == answers[0]:
        print("Ответ верный!")
        correct += 1
    else:
        print(f"Неправильно. Правильный ответ: {answers[0]}")

    print(questions[1])
    user_answer2 = input()
    if user_answer2 == answers[1]:
        print("Ответ верный!")
        correct += 1
    else:
        print(f"Неправильно. Правильный ответ: {answers[1]}")

    print(questions[2])
    user_answer3 = input()
    if user_answer3 == answers[2]:
        print("Ответ верный!")
        correct += 1
    else:
        print(f"Неправильно. Правильный ответ: {answers[2]}")

print(f"Вот и все! Вы ответили на {correct} вопроса из {len(questions)} верно")
