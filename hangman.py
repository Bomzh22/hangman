import time as t
import random

player_score = 0
computer_score = 0


def word():
    word_list = open("words.txt", "r").readlines()
    random_number = random.randint(0, len(word_list))
    word = word_list[random_number].rstrip()
    return word


def hanged(man):
    graphic = [
    '''
       +------+
       | /
       |/
       |
       |
       |
    ==============
    ''',
    '''
       +------+
       | /    |
       |/     O
       |
       |
       |
    ==============
    ''',
    '''
       +------+
       | /    |
       |/     O
       |      |
       |
       |
    ==============
    ''',
    '''
       +------+
       | /    |
       |/     O
       |     -|
       |
       |
    ==============
    ''',
    '''
       +------+
       | /    |
       |/     O
       |     -|-
       |
       |
    ==============
    ''',
    '''
       +------+
       | /    |
       |/     O
       |     -|-
       |     /
       |
    ==============
    ''',
    '''
       +------+
       | /    |
       |/     O
       |     -|-
       |     / \\
       |
    ==============
    '''
    ]
    return graphic[man]


def start():
    print("")
    print("HangMan")
    print("=======")
    print("")
    t.sleep(0.5)
    while game():
        pass
    print("")
    scores()

def game():
    the_word = word()
    word_list = the_word.split()
    print("В Слове {} Букв".format(len(the_word)))
    t.sleep(0.5)
    clue = len(the_word) * ["-"]
    print("")
    print("".join(clue))
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    while (letters_wrong != tries) and ("".join(clue) != the_word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print("Буква", letter, " Уже Была Введена")
            else:
                letters_tried += letter
                first_index = the_word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print("Сори Чел Буква {} Не Та".format(letter))
                else:
                    print("Правильно Буква {} Входит В Состав Слова".format(letter))
                    for i in range(len(the_word)):
                        if letter == the_word[i]:
                            clue[i] = letter
        else:
            print("Неправильное Значение!!!")

        print(hanged(letters_wrong))
        print("".join(clue))
        print("")
        print("Введенные Буквы :", letters_tried)

        if letters_wrong == tries :
            print("Ты Проиграл")
            print("Загадонное Слово: {}".format(the_word))
            computer_score += 1
            break
        if "".join(clue) == the_word:
            print("Ты Выиграл")
            print("Разгаданное Слово: {}".format(the_word))
            player_score += 1
            break

    return play_again() 

def guess_letter():
    print("")
    letter = input("Введи Букву: ")
    letter.strip()
    letter.lower()
    print("")
    return letter


def play_again():
    print("")
    answer = input("Сыграть Еще Раз ? y/n: ")
    if answer in ("y", "Y", "Yes", "yes", "YES", "да", "Да", "ДА", "д", "Д"):
        return answer
    else:
        print("Спасибо За Использование. Скоро Увидимся!")


def scores():
    print("")
    global player_score, computer_score
    print("Счет:")
    print("Выигрышей: ", player_score)
    print("Проигрышей: ", computer_score)


if __name__ == "__main__":
    start()
